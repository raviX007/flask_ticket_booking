from flask_restful import Resource, reqparse
from models import db, Theater

class TheaterResource(Resource):
    def get(self, theater_id):
        theater = Theater.query.get(theater_id)
        if not theater:
            return {'error': 'Theater not found'}, 404
        return theater.to_dict()

    def put(self, theater_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('location', required=True)
        parser.add_argument('capacity', type=int, required=True)
        args = parser.parse_args()

        theater = Theater.query.get(theater_id)
        if not theater:
            return {'error': 'Theater not found'}, 404

        theater.name = args['name']
        theater.location = args['location']
        theater.capacity = args['capacity']
        db.session.commit()
        return theater.to_dict()

    def delete(self, theater_id):
        theater = Theater.query.get(theater_id)
        if not theater:
            return {'error': 'Theater not found'}, 404
        db.session.delete(theater)
        db.session.commit()
        return {'message': 'Theater deleted'}, 200

class TheaterListResource(Resource):
    def get(self):
        theaters = Theater.query.all()
        return [theater.to_dict() for theater in theaters]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('location', required=True)
        parser.add_argument('capacity', type=int, required=True)
        args = parser.parse_args()

        theater = Theater(
            name=args['name'],
            location=args['location'],
            capacity=args['capacity']
        )
        db.session.add(theater)
        db.session.commit()
        return theater.to_dict(), 201
