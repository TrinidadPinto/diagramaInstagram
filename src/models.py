from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), index=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    email = db.Column(db.String(), unique=True)

    posts = db.relationship('Post', backref='user', lazy=True, cascade="all, delete-orphan")
    comments = db.relationship('Comment', backref='author', lazy=True, cascade="all, delete-orphan")
    followers = db.relationship('Follower', foreign_keys='Follower.user_to_id', back_populates='user_to', lazy=True, cascade="all, delete-orphan")
    following = db.relationship('Follower', foreign_keys='Follower.user_from_id', back_populates='user_from', lazy=True, cascade="all, delete-orphan")

class Follower(db.Model):
    __tablename__ = 'follower'
    id = db.Column(db.Integer, primary_key=True)
    user_from_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_to_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user_from = db.relationship('User', foreign_keys=[user_from_id], back_populates="following")
    user_to = db.relationship('User', foreign_keys=[user_to_id], back_populates="followers")

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    comments = db.relationship('Comment', backref='post', lazy=True, cascade="all, delete-orphan")
    media = db.relationship('Media', backref='post', lazy=True, cascade="all, delete-orphan")

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String())
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

class Media(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(Enum('image', 'video', name='media_type'))
    url = db.Column(db.String())
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
