from sqlalchemy.orm import Mapped, mapped_column
from app import app, db


class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=True)
    ranking: Mapped[int] = mapped_column(nullable=True)
    review: Mapped[str] = mapped_column(nullable=True)
    img_url: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return '<Movie {}>'.format(self.title)


# Create table schema in db. Requires app context
with app.app_context():
    db.create_all()

def validate_title(title):
    check = db.session.execute(db.select(Movie).filter_by(title=title)).first()
    return check

