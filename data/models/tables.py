from sqlalchemy import Integer, String
from flask_sqlalchemy import SQLAlchemy
from controller.config import db


class CookedDish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    prepTime = db.Column(db.Integer)

    def __init__(self, name, price, prepTime):
        self.name = name
        self.price = price
        self.prepTime = prepTime

    def __repr__(self):
        return f'New CookedDish with the Name: {self.name}'


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    alcohol = db.Column(db.Integer)

    def __init__(self, name, price, alcohol):
        self.name = name
        self.price = price
        self.alcohol = alcohol

    def __repr__(self):
        return f'New CookedDish with the Name: {self.name}'


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer)
    dishIds = db.Column(db.String(100))
    drinkIds = db.Column(db.String(100))
    total = db.Column(db.Integer)

    def __init__(self, customerId, dishIds, drinkIds, total):
        self.customerId = customerId
        self.dishIds = dishIds
        self.drinkIds = drinkIds
        self.total = total

    def __repr__(self):
        return f'New Order with the ID: {self.id}'


class Customer(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100))
    address = db.Column(String(100))

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return f'New Customer with the Name: {self.name}'
