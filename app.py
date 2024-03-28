from flask import Flask, render_template, request, redirect, flash, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
import datetime
import random

app = Flask(__name__)

db_name = 'data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    coins = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user_id


class Events(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    first_opponent = db.Column(db.String(100))
    second_opponent = db.Column(db.String(100))
    tournoment = db.Column(db.String(100))
    date = db.Column(db.DateTime)
    first_score = db.Column(db.Integer)
    second_score = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.event_id

class Bets(db.Model):
    bet_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime)
    first_score = db.Column(db.Integer, nullable=False)
    second_score = db.Column(db.Integer, nullable=False)
    coins = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.bet_id

class Sessions(db.Model):
    session_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    session_key = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return '<Session %r>' % self.session_id


@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        if check_cookies():
            return jsonify(1)
        else:
            return jsonify(0)
    return render_template("main.html")
def check_cookies():
    if request.cookies.get('username') and request.cookies.get('session_key'):
        username = request.cookies.get('username')
        print(username)
        user_id = Users.query.filter_by(username = username).first()
        if user_id is None:
            return False
        user_id = user_id.user_id
        session_key = Sessions.query.filter_by(user_id = user_id).first()
        if session_key is None:
            return False
        session_key = session_key.session_key
        print(session_key)
        real_session_key = request.cookies.get('session_key')
        print(real_session_key)
        if (session_key == real_session_key):
            return True
        else:
            return False


@app.route('/login', methods=["POST", "GET"])
def login():
    if check_cookies():
        abort(404)
    if request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        check = Users.query.filter_by(username = username, password = password).first()
        if check is not None:
            user_id = Users.query.filter_by(username = username).first()
            if user_id is not None:
                user_id = user_id.user_id
                delete = Sessions.query.filter_by(user_id = user_id).all()
                for i in delete:
                    db.session.delete(i)
                db.session.commit()
                session_key = generate_session_key()
                session = Sessions(user_id = user_id, session_key = session_key)
                db.session.add(session)
                db.session.commit()
                cookie = make_response(redirect("/"))
                cookie.set_cookie('username', username)
                cookie.set_cookie('session_key', session_key)
                return cookie
    return render_template("login.html")

def generate_session_key():
        res = ''
        chars = [chr(i) for i in range(33, 127)]
        for _ in range(15):
            res += chars[random.randint(0, len(chars) - 1)]
        return res


@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    if check_cookies():
        abort(404)
    if request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        if (len(username) > 25 or len(password) > 25):
            print("mistake, username and password must include less than 25 letters")
        else:
            check = Users.query.filter_by(username = username).first()
            if (check is None):
                user = Users(username = username, password = password, coins = 100)
                db.session.add(user)
                db.session.commit()
                user_id = Users.query.filter_by(username = username).first().user_id
                session_key = generate_session_key()
                session = Sessions(user_id = user_id, session_key = session_key)
                db.session.add(session)
                db.session.commit()
                cookie = make_response(redirect("/"))
                cookie.set_cookie('username', username)
                cookie.set_cookie('session_key', session_key)
                return cookie
            else:
                print("username has already been used")
    return render_template("sign_up.html")


@app.route('/profile', methods=["POST", "GET"])
def profile():
    if not check_cookies():
        abort(404)
    if request.method == "POST":
        if check_cookies():
            return jsonify(1)
        else:
            return jsonify(0)
    return render_template("profile.html")


@app.route('/log_out_button', methods=["POST", "GET"])
def log_out_button():
    if not check_cookies():
        abort(404)
    username = request.cookies.get('username')
    user_id = Users.query.filter_by(username = username).first()
    if user_id is not None:
        user_id = user_id.user_id
        delete = Sessions.query.filter_by(user_id = user_id).all()
        for i in delete:
            db.session.delete(i)
        db.session.commit()
        cookie = make_response(redirect("/"))
        cookie.set_cookie('username', 'delete', max_age=0)
        cookie.set_cookie('session_key', 'delete', max_age=0)
        return cookie


if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.52', port=1234)

