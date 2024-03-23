from flask import Flask, render_template, request, redirect, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

db_name = 'data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    coins = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user_id



@app.route('/')
def main():
    return render_template("main.html")

# @app.route('/help')
# def help():
#     # user = User(username = 'peterpodrez', password = 'Iamsnitchtoo', coins = 98)
#     # db.session.add(user)
#     # db.session.commit()
#     tim = User.query.filter_by(username='timsytsko').first()
#     print(tim.password)
#     daun = User.query.all()
#     print(daun[0].password)
#     delete = User.query.filter_by(username='peterpodrez').all()
#     for i in delete:
#         db.session.delete(i)
#     db.session.commit()
#     return "ok"

if __name__ == "__main__":
    app.run(debug=True)