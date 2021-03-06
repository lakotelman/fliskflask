from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(250))

    def hash_my_pass(self, password):
        self.password = generate_password_hash(password)

    def check_my_pass(self, password):
        return check_password_hash(self.password, password)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    make = db.Column(db.String(25))
    model = db.Column(db.String(25))
    year = db.Column(db.Integer)
    color = db.Column(db.String(25))
    price = db.Column(db.Float) 
    description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def get_user(self):
        return User.query.get(self.user_id)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)