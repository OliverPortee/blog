
from app import db

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), unique = True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)

    def __repr__(self):
        return "BlogPost {} {}".format(self.id, self.title)
