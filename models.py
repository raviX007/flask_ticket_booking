from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    synopsis = db.Column(db.Text, nullable=False)
    showtimes = db.relationship('Showtime', backref='movie', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'director': self.director,
            'genre': self.genre,
            'release_date': self.release_date.isoformat(),
            'duration': self.duration,
            'synopsis': self.synopsis
        }

class Theater(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    showtimes = db.relationship('Showtime', backref='theater', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'capacity': self.capacity
        }

class Showtime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    theater_id = db.Column(db.Integer, db.ForeignKey('theater.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'movie': self.movie.to_dict(),
            'theater': self.theater.to_dict(),
            'date_time': self.date_time.isoformat(),
            'available_seats': self.available_seats
        }