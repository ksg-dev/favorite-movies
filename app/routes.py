from flask import Flask, render_template, request, redirect, url_for, flash
from app import app, db
from app.forms import RateMovieForm
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


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)

    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)