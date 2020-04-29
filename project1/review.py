import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
db = SQLAlchemy()


class reviews(db.Model):
    __tablename__ = "reviews"
    isbn = Column(Integer, primary_key = True)
    user = Column(String, primary_key = True)
    rate = Column(Integer, nullable = False)
    review = Column(String, nullable = False)

    def __init__(self, isbn, user, rate, review):
        self.isbn = isbn
        self.user = user
        self.rate = rate
        self.review = review
        # self.createtimestamp = datetime.now()

