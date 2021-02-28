from os import urandom, path
basedir = path.abspath(path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATION = False