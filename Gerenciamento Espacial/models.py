from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    launch_date = db.Column(db.Date, nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    crew = db.Column(db.String(200), nullable=True)
    payload = db.Column(db.String(500), nullable=True)
    duration = db.Column(db.String(50), nullable=True)
    cost = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.Text, nullable=True)
