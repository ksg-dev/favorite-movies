from sqlalchemy.orm import Mapped, mapped_column
from app import app, db

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)

def validate_title(title):
    check = db.session.execute(db.select(Book).filter_by(title=title)).first()
    return check