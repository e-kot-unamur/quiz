from flask import Flask, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
#from models import *
from datetime import time
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///results.sqlite3'
db = SQLAlchemy( app )

class Results(db.Model):
    __tablename__ = "results"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    addressMail = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, addressMail):
        self.addressMail = addressMail

    def __repr__(self):
        return "<Result id: %d, addressMail:%s>" % (self.id,self.addressMail)

class Quiz(db.Model):
    __tablename__ = "quiz"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    point = db.Column(db.Integer, unique=False, nullable=False)
    quizName= db.Column(db.String(128), unique=False, nullable=False)
    timeQuizz= db.Column(db.Float)
    address_id = db.Column(db.Integer, db.ForeignKey('results.id'), nullable=False)
    address = db.relationship('Results', backref=db.backref('quizz', lazy=True))

    def __init__(self, point, quizName, timeQuizz, address):
        self.point = point
        self.quizName = quizName
        self.timeQuizz = timeQuizz
        self.address = address

    def __repr__(self):
        return "<Result id: %d, point: %d, quizName:%s, timeQuizz:%f>" % (self.id, self.point, self.quizName, self.timeQuizz)

# Path for our main Svelte page
@app.route("/")
@app.route("/about")
@app.route("/IST-MST/help", methods=["POST", "GET"])
@app.route("/IST-MST", methods=["POST", "GET"])
def base():      
    return send_from_directory('client/public', 'index.html')

@app.route("/Results", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        address = request.form["address"]
        result = Results.query.filter_by(addressMail=address).first()
        if result is None:
            result = Results(addressMail=address)
            quiz = Quiz(point=0, quizName="jsp", timeQuizz=1.2, address=result)
            db.session.add(result)
            db.session.add(quiz)
        else:
            quizzez = result.quizz  #Get all quizzez
            for quiz in quizzez:
                if quiz.quizName == "test2":
                    quizUser = Quiz.query.filter_by(quizName="test2").first() #Get the quiz table for a quizz of the user
                    quizUser.point=1
                    quizUser.timeQuizz=11
                    db.session.commit()
                    return send_from_directory('client/public', 'index.html')
            quiz = Quiz(point=2, quizName="test2", timeQuizz=8, address=result)
        db.session.commit()
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)