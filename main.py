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
    point = db.Column(db.String(10), unique=False, nullable=False)
    addressMail = db.Column(db.String(128), unique=True, nullable=False)
    quizName= db.Column(db.String(128), unique=False, nullable=False)
    timeQuizz= db.Column(db.Float)

    def __init__(self, point, addressMail, quizName, timeQuizz):
        self.point = point
        self.addressMail = addressMail
        self.quizName = quizName
        self.timeQuizz = timeQuizz
    def __repr__(self):
        return "<Result id: %d, point: %s, addressMail:%s, quizName:%s>" % (self.id, self.point, self.addressMail, self.quizName)
# Path for our main Svelte page
@app.route("/")
@app.route("/about")
@app.route("/IST-MST/help", methods=["POST", "GET"])
@app.route("/IST-MST", methods=["POST", "GET"])
def base():
    if request.method == "POST":
        address = request.form["address"]
        result = Results.query.filter_by(addressMail=address).first()
        if result is None:
            result = Results(point=0, addressMail=address, quizName="jsp", timeQuizz=10.5)
            db.session.add(result)
            db.session.commit()
        
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)
""" 
 @app.rout("/results")
def main():
    if request.method == "POST":
        content = request.form["content"]  #Take the content of the user (the task)
        description = request.form["description"]
        result = Result(point=content, addressMail=False, quizId=description)
        db.session.add(task)    #add the task in the database
        db.session.commit()
    return render_template('index.html', tasks=current_user.tasks, admin = current_user.isAdmin()) """

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)