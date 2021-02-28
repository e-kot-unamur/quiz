from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import urandom, path
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)



from . import main
if __name__ == "__main__":
    app.run(debug=True)