from flask import Flask, render_template, request, redirect, url_for, flash
from app import app, db

from app.models import Movie, validate_title
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

bootstrap = Bootstrap5(app)

@app.route('/', methods=["GET", "POST"])
def home():
    query = request.args.get("q")

    if query is not None:
        return redirect(url_for('search', terms=query))

    else:
        return render_template('index.html', library=Movie.query.all(), query=None)