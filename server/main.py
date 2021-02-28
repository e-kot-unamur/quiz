from os import path
from flask import Flask, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from .__init__ import app, db
from .models import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///results.sqlite3'
db = SQLAlchemy( app )


# Path for our main Svelte page
@app.route("/")
@app.route("/about")
@app.route("/IST-MST/help")
@app.route("/IST-MST", methods=["POST", "GET"])
def base():
    if request.method == "POST":
        address = request.form["address"]
        print(address)
        result = Results.query.filter_by(addressMail=address).first()
        if result is None:
            result = Results(point=0, addressMail=address, quizName="jsp")
            db.session.add(result)
            db.session.commit()
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('../client/public', path)

""" @app.rout("/results")
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