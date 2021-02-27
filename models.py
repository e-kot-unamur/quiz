from main import db

class Results(db.Model):
    __tablename__ = "results"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    point = db.Column(db.String(10), unique=False, nullable=False)
    addressMail = db.Column(db.String(128), unique=True, nullable=False)
    quizName= db.Column(db.String(128), unique=False, nullable=False)

    def __repr__(self):
        return "<Result id: %d, point: %s, addressMail:%s, quizName:%s>" % (self.id, self.point, self.addressMail, self.quizName)
    db.create_all()