from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from passlib.hash import sha256_crypt
db = SQLAlchemy()

class schema(db.Model):
    __tablename__="schema"
    name = db.Column(db.String, primary_key = True)
    email = db.Column(db.String, primary_key=True)
    pwd = db.Column(db.String, nullable=False)
    createtimestamp = db.Column(db.DateTime(timezone=True),nullable = False)
    
    def __init__(self, name, email, pwd):
        self.name = name
        self.email = email
        self.pwd = sha256_crypt.encrypt("password")
        self.createtimestamp = datetime.now()
