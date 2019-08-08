from datetime import datetime
from sqlalchemy.sql import func
from project import db


class SimpleUser(db.Model):
    __tablename__ = 'simple_users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<SimpleUser {}>'.format(self.email)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    subscription = db.Column(db.Boolean(), default=False, nullable=False)
    terms_and_conditions = db.Column(db.Boolean(), default=False, nullable=False)
    firstname = db.Column(db.String(128), nullable=False)
    middlename = db.Column(db.String(128), nullable=True)
    lastname = db.Column(db.String(128), nullable=False)
    address1 = db.Column(db.String(128), nullable=False)
    address2 = db.Column(db.String(128), nullable=True)
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zipcode = db.Column(db.String(15), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(128), unique=True, nullable=True)
    birthmonth = db.Column(db.String(10), nullable=True)
    birthday = db.Column(db.String(2), nullable=True)
    birthyear = db.Column(db.String(4), nullable=True)
    online = db.Column(db.Boolean(), default=True, nullable=False)
    lastlogin = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
    lastlogout = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)

    def __init__(self, email, subscription,terms_and_conditions, firstname, middlename, lastname, address1, address2, city, state, zipcode, country, phone, birthmonth, brithday, birthyear, online, lastlogin, lastlogout, created_at):
        self.email = email
        self.subscription = subscription
        self.terms_and_conditions = terms_and_conditions
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country
        self.phone = phone
        self.birthmonth = birthmonth
        self.birthday = birthday
        self.birthyear = birthyear
        self.online = online
        self.lastlogin = lastlogin
        self.lastlogout = lastlogout
        self.created_at = created_at

    def __repr__(self):
        return '<User {}>'.format(self.email)