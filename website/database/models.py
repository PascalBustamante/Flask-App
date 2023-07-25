from . import db ##this might be bad practice

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))

    def __repr__(self):
        return '<User {}>'.format(self.username)