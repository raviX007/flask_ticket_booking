from flask_restful import Resource, reqparse
from models import db, Movie
from datetime import datetime

class MovieResource(Resource):
    def get(self, movie_id):
        movie = Movie.query.get(movie_id)
        if not movie:
            return {'error': 'Movie not found'}, 404
        return movie.to_dict()

    def put(self, movie_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('director', required=True)
        parser.add_argument('genre', required=True)
        parser.add_argument('release_date', required=True)
        parser.add_argument('duration', type=int, required=True)
        parser.add_argument('synopsis', required=True)
        args = parser.parse_args()

        movie = Movie.query.get(movie_id)

        movie.title = args['title']
        movie.director = args['director']
        movie.genre = args['genre']
        try:
            movie.release_date = datetime.strptime(args['release_date'], '%Y-%m-%d').date()
        except ValueError:
            return {'error': 'Invalid date format. Please use YYYY-MM-DD.'}, 400
        movie.duration = args['duration']
        movie.synopsis = args['synopsis']
        db.session.commit()
        return movie.to_dict()

    def delete(self, movie_id):
        movie = Movie.query.get(movie_id)
        if not movie:
            return {'error': 'Movie not found'}, 404
        db.session.delete(movie)
        db.session.commit()
        return {'message': 'Movie deleted'}, 200

class MovieListResource(Resource):
    def get(self):
        movies = Movie.query.all()
        return [movie.to_dict() for movie in movies]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('director', required=True)
        parser.add_argument('genre', required=True)
        parser.add_argument('release_date', required=True)
        parser.add_argument('duration', type=int, required=True)
        parser.add_argument('synopsis', required=True)
        args = parser.parse_args()

        try:
            release_date = datetime.strptime(args['release_date'], '%Y-%m-%d').date()
        except ValueError:
            return {'error': 'Invalid date format. Please use YYYY-MM-DD.'}, 400

        movie = Movie(
            title=args['title'],
            director=args['director'],
            genre=args['genre'],
            release_date=release_date,
            duration=args['duration'],
            synopsis=args['synopsis']
        )
        db.session.add(movie)
        db.session.commit()
        return movie.to_dict(), 201
