from .__init__ import db

class Results(db.Model):
    __tablename__ = "results"

    id = db.Column(db.Integer, nullable=True, primary_key=True, autoincrement=True)
    point = db.Column(db.String(10), unique=False, nullable=True)
    addressMail = db.Column(db.String(128), unique=True, nullable=True)
    quizName= db.Column(db.String(128), unique=False, nullable=True)

    def __repr__(self):
        return "<Result id: %d, point: %s, addressMail:%s, quizName:%s>" % (self.id, self.point, self.addressMail, self.quizName)

db.create_all()