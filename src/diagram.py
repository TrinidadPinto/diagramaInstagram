from app import app, db
from models import User, Follower, Comment, Post, Media
from eralchemy import render_er

with app.app_context():
    db.create_all()
    render_er(db.Model.metadata, 'diagram.png')
    print("✅ Diagrama generado con éxito en diagram.png")