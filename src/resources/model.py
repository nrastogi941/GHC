from src.databases import db

class Checkout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    checkout_time = db.Column(db.DateTime, nullable=False)
    order_placed = db.Column(db.Boolean, default=False)
    messages_sent = db.Column(db.Integer, default=0)
    order_items = db.Column(db.JSON, default=[])
