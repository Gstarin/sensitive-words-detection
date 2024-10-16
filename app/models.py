from .extensions import db


class Word(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(250), nullable=False)
    regex = db.Column(db.UnicodeText, nullable=False)
    type = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Word %r>' % self.word
