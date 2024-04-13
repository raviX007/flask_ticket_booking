from flask import Flask
from flask_restful import Api
from resources.movie import MovieResource, MovieListResource
from resources.theater import TheaterResource, TheaterListResource
from resources.showtime import (
    ShowtimeResource, ShowtimeListResource,
    AvailableSeatsResource, ReserveSeatsResource
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

from models import db
db.init_app(app)

api.add_resource(MovieResource, '/movies/<int:movie_id>')
api.add_resource(MovieListResource, '/movies')

api.add_resource(TheaterResource, '/theaters/<int:theater_id>')
api.add_resource(TheaterListResource, '/theaters')

api.add_resource(ShowtimeResource, '/showtimes/<int:showtime_id>')
api.add_resource(ShowtimeListResource, '/showtimes')
api.add_resource(AvailableSeatsResource, '/showtimes/<int:showtime_id>/available_seats')
api.add_resource(ReserveSeatsResource, '/showtimes/<int:showtime_id>/reserve_seats')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
