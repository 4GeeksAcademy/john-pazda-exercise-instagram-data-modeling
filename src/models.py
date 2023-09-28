import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(12), nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    posts = relationship("Post", backref="authored_posts")
    mentions = relationship("Post", backref="mentioned_user")
    

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    comments = relationship("Comment", backref="post")
    mentioned_id = Column(Integer, ForeignKey("user.id"))
    


    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))

class Follower(Base):
    __tablename__='follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"))

class Media(Base):
    __tablename__='media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    url = Column(String(250), nullable=False)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
