from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy()

class schema(db.Model):
    __tablename__="schema"
    name = db.Column(db.String, primary_key = True)
    email = db.Column(db.String, primary_key=True)
    pwd = db.Column(db.String, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.pwd = password
    