from flask_restful import Resource, reqparse
from models import db, Showtime, Movie, Theater
from datetime import datetime

class ShowtimeResource(Resource):
    def get(self, showtime_id):
        showtime = Showtime.query.get(showtime_id)
        if not showtime:
            return {'error': 'Showtime not found'}, 404
        return showtime.to_dict()

    def put(self, showtime_id):
        parser = reqparse.RequestParser()
        parser.add_argument('movie_id', type=int, required=True)
        parser.add_argument('theater_id', type=int, required=True)
        parser.add_argument('date_time', required=True)
        parser.add_argument('available_seats', type=int, required=True)
        args = parser.parse_args()

        showtime = Showtime.query.get(showtime_id)
        if not showtime:
            return {'error': 'Showtime not found'}, 404

        showtime.movie_id = args['movie_id']
        showtime.theater_id = args['theater_id']
        try:
            showtime.date_time = datetime.strptime(args['date_time'], '%Y-%m-%d').date()
        except ValueError:
            return {'error': 'Invalid date format. Please use YYYY-MM-DD.'}, 400

        
        showtime.available_seats = args['available_seats']
        db.session.commit()
        return showtime.to_dict()

    def delete(self, showtime_id):
        showtime = Showtime.query.get(showtime_id)
        if not showtime:
            return {'error': 'Showtime not found'}, 404
        db.session.delete(showtime)
        db.session.commit()
        return {'message': 'Showtime deleted'}, 200

class ShowtimeListResource(Resource):
    def get(self):
        showtimes = Showtime.query.all()
        return [showtime.to_dict() for showtime in showtimes]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('movie_id', type=int, required=True)
        parser.add_argument('theater_id', type=int, required=True)
        parser.add_argument('date_time', required=True)
        parser.add_argument('available_seats', type=int, required=True)
        args = parser.parse_args()

        movie = Movie.query.get(args['movie_id'])
        if not movie:
            return {'error': 'Movie not found'}, 404

        theater = Theater.query.get(args['theater_id'])
        if not theater:
            return {'error': 'Theater not found'}, 404
        try:
            date_time = datetime.strptime(args['date_time'], '%Y-%m-%d').date()
        except ValueError:
            return {'error': 'Invalid date format. Please use YYYY-MM-DD.'}, 400

        showtime = Showtime(
            movie_id=args['movie_id'],
            theater_id=args['theater_id'],
            date_time=date_time,
            available_seats=args['available_seats']
        )
        db.session.add(showtime)
        db.session.commit()
        return showtime.to_dict(), 201

class AvailableSeatsResource(Resource):
    def get(self, showtime_id):
        showtime = Showtime.query.get(showtime_id)
        if not showtime:
            return {'error': 'Showtime not found'}, 404
        if showtime.date_time < datetime.now():
            return {'error': 'Showtime has already passed'}, 400
        return {'available_seats': showtime.available_seats}

class ReserveSeatsResource(Resource):
    def post(self, showtime_id):
        parser = reqparse.RequestParser()
        parser.add_argument('num_seats', type=int, required=True)
        args = parser.parse_args()

        showtime = Showtime.query.get(showtime_id)
        if not showtime:
            return {'error': 'Showtime not found'}, 404
        if showtime.date_time < datetime.now():
            return {'error': 'Showtime has already passed'}, 400
        if args['num_seats'] > showtime.available_seats:
            return {'error': 'Requested number of seats exceeds available seats'}, 400

        showtime.available_seats -= args['num_seats']
        db.session.commit()
        return {'message': f'{args["num_seats"]} seats reserved successfully'}, 200
