from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.forms import RateMovieForm, AddMovie
from app.models import Movie
from flask_bootstrap import Bootstrap5
from app.movie import GetMovie, get_details

bootstrap = Bootstrap5(app)


def rank_movies():
    top_movies = []
    ranked = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().yield_per(10)

    start = 10
    for movie in ranked:
        movie = db.get_or_404(Movie, movie.id)
        movie.ranking = start
        db.session.commit()
        top_movies.append(movie)
        start -= 1
    return top_movies


@app.route('/', methods=["GET", "POST"])
def home():
    top_movies = rank_movies()[:10]

    return render_template('index.html', library=top_movies)


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

    return render_template("add.html", form=form)


@app.route("/find")
def get_movie_details():
    data = get_details(request.args.get("id"))

    new_movie = Movie(
        title=data["title"],
        year=data["year"],
        description=data["description"],
        img_url=data["img_url"]
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("edit", id=new_movie.id))


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)

    db.session.delete(movie)
    db.session.commit()

    flash("Record Deleted")

    return redirect(url_for("home"))
