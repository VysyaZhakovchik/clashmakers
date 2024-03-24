from flask import Flask, render_template, request, redirect, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
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
    first_score = db.Column(db.Integer)
    second_score = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.event_id

class Bets(db.Model):
    bet_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(25), nullable=False)
    first_score = db.Column(db.Integer, nullable=False)
    second_score = db.Column(db.Integer, nullable=False)
    coins = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.bet_id


@app.route('/')
def main():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)