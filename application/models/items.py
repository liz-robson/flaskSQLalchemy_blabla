from dataclasses import dataclass

from application import db


# the annotation below will help to turn the Python object into a JSON object
@dataclass
class Items(db.Model):
    # the declarations below are important for turning the object into JSON
    id: int
    item_name: str
    brand: str
    size: str
    category: str
    sub_category: str
    colour: str
    item_description: str
    price: int
    collection: str
    item_type: str
    item_location: str
    # owner_id: int
    rental_price: int

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50), nullable=True)
    size = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(70), nullable=False)
    sub_category = db.Column(db.String(70), nullable=True)
    colour = db.Column(db.String(20), nullable=False)
    item_description = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer)
    collection = db.Column(db.String(70), nullable=True)
    item_type = db.Column(db.String(20), nullable=False)
    item_location = db.Column(db.String(20), nullable=False)
    # owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rental_price = db.Column(db.Integer)



