from flask import Flask, render_template, request, redirect, url_for, flash
from app import app, db
from app.forms import RateMovieForm, AddMovie
from app.models import Movie, validate_title
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from movie import GetMovie

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
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    form = RateMovieForm(obj=movie)

    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if request.method == "POST":
        if form.validate_on_submit():
            title = form.title.data.title()
            print(title)

            # Call on API with title
            search = GetMovie(title)
            movie_list = search.movie_details

            for movie in movie_list:
                search_id = movie["id"]
                overview = movie["overview"]
                poster_path = movie["poster_path"]
                release_date = movie["release_date"]
                title = movie["title"]

            return render_template("select.html", results=movie_list)

        # print(search.movie_details)

    return render_template("add.html", form=form)



@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)

    db.session.delete(movie)
    db.session.commit()

    flash("Record Deleted")

    return redirect(url_for("home"))