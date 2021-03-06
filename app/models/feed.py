
from sqlalchemy import Column, Integer, String, Text, ForeignKey,  Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
import uuid
import app
import jwt
import os
import sys
from flask import current_app as app

from app.models import db
from .dogear_model import DogearMixin





class Feed( DogearMixin,db.Model):
    __tablename__ = 'feed'


    id = Column(Integer(), primary_key=True)
    from_user_id = Column(Integer(), nullable=False)
    user_id = Column(Integer(),nullable=False)
    from_group_id = Column(Integer(),nullable=False)
    news_id = Column(Integer(),nullable=False)


    def __init__(self, from_user_id=from_user_id, from_group_id=from_group_id, user_id=user_id, news_id=news_id):
        self.uuid = str(uuid.uuid4())
        self.from_user_id = from_user_id
        self.from_group_id = from_group_id
        self.user_id = user_id
        self.news_id = news_id

    def feed_for_user(self, user_id):
        return Feed.query.filter(Feed.user_id==user_id).all()



