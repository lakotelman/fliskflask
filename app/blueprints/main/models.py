from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(100))


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    make = db.Column(db.String(25))
    model = db.Column(db.String(25))
    year = db.Column(db.Integer)
    color = db.Column(db.String(25))
    price = db.Column(db.Integer) 
    description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def get_user(self):
        return User.query.get(self.user_id)
