#from . imports from __init__.py (imports from within this package) (same as saying from Website)
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10,000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #foreign key is a column in your database that always references a column of another database
    #by specifying our foreign key means we must pass a valid ID of an existing user to this column
        #this is known as a one-to-many relationship. One object has many children(one user has many notes)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))



class User(db.Model, UserMixin):
    #this sets up schema for storing the data on each user
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship("Note")
