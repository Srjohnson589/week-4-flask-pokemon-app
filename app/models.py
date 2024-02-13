from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

class Pokemon(db.Model):
    name = db.Column(db.String, primary_key=True)
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    sprite_img = db.Column(db.String, nullable=False)
    abilities = db.Column(db.String, nullable=False)

    def __init__(self, name, hp, attack, defense, sprite_img, abilities):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sprite_img = sprite_img
        self.abilities = abilities

    def save(self):
        db.session.add(self)
        db.session.commit()

