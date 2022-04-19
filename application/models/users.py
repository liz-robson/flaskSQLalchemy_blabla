from application import db

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    profile_image = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(30), nullable=False)
    social_media_account = db.Column(db.String(50), nullable=False)
    # delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.id'), nullable=False)
    # billing_id = db.Column(db.Integer, db.ForeignKey('billing.id'), nullable=False)
    # bank_id = db.Column(db.Integer, db.ForeignKey('bank_details.id'), nullable=False)



