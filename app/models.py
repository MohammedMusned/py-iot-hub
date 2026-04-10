from flask_sqlalchemy import SQLAlchemy
from app import db
import uuid





class Test(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(80), unique=True, nullable=False)
    
    def __repr__(self):
        return f"Test('{self.name}')"