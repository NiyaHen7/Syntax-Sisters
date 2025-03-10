#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:30:54 2025

@author: madisonskinner
"""

from flask import Flask, render_template, request, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/school_reviews'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

# Create tables explicitly in app context (only run once on startup)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    professors = Professor.query.all()
    return render_template('index.html', professors=professors)

@app.route('/add_professor', methods=['POST'])
def add_professor():
    name = request.form['name']
    new_professor = Professor(name=name)
    db.session.add(new_professor)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_review', methods=['POST'])
def add_review():
    user_id = request.form['user_id']
    professor_id = request.form['professor_id']
    rating = request.form['rating']
    comment = request.form.get('comment', '')

    new_review = Review(user_id=user_id, professor_id=professor_id, rating=rating, comment=comment)
    db.session.add(new_review)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
