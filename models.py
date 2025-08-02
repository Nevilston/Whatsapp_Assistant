from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    height_cm = db.Column(db.Float)
    weight_kg = db.Column(db.Float)
    goal_weight_kg = db.Column(db.Float)
    activity_level = db.Column(db.String(50))
    diet_type = db.Column(db.String(50))
    medical_issues = db.Column(db.String(200))
    reminder_time = db.Column(db.String(5))  
    current_step = db.Column(db.String(50)) 
