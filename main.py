from flask import Flask, send_from_directory, request, flash
from flask_sqlalchemy import SQLAlchemy
from tools import adresseChecker
#from models import *
from datetime import time
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///results.sqlite3'
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
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
    total = db.Column(db.Integer, unique=False, nullable=False)
    quizName= db.Column(db.String(128), unique=False, nullable=False)
    timeQuizz= db.Column(db.Float)
    address_id = db.Column(db.Integer, db.ForeignKey('results.id'), nullable=False)
    address = db.relationship('Results', backref=db.backref('quizz', lazy=True))

    def __init__(self, point, total, quizName, timeQuizz, address):
        self.point = point
        self.quizName = quizName
        self.total = total
        self.timeQuizz = timeQuizz
        self.address = address

    def __repr__(self):
        return "<Result id: %d, point: %d, quizName:%s, timeQuizz:%f>" % (self.id, self.point, self.quizName, self.timeQuizz)

# Path for our main Svelte page
@app.route("/")
@app.route("/about")
@app.route("/quizz2")
@app.route("/quizzMaisonInter")
def base():      
    return send_from_directory('client/public', 'index.html')

@app.route("/Results", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        if request.is_json:
            address=request.json.get('address', None)
            point=request.json.get('point', None)
            total=request.json.get('total', None)
            quizname=request.json.get('quizname', None)
            timequizz=request.json.get('timequizz', None)
            if not(adresseChecker(address)):
                flash('Veuillez entrer un bon format d\'adresse email', 'info') #TODO
                return send_from_directory('client/public', 'index.html')
            result = Results.query.filter_by(addressMail=address).first()
            if result is None:
                result = Results(addressMail=address)
                quiz = Quiz(point=point, total=total, quizName=quizname, timeQuizz=timequizz, address=result)
                db.session.add(result)
                db.session.add(quiz)
            else:
                quizzez = result.quizz  #Get all quizzez of the addresse mail
                for quiz in quizzez:
                    if quiz.quizName == quizname:   #check that the user already did the quiz
                        """ quizUser = Quiz.query.filter_by(id=quiz.id).first() #Get the quiz table for a quizz for a user
                        quizUser.point=point
                        quizUser.timeQuizz=timequizz
                        db.session.commit() """
                        return send_from_directory('client/public', 'index.html')
                quiz = Quiz(point=point, total=total, quizName=quizname, timeQuizz=timequizz, address=result)
            db.session.commit()
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)