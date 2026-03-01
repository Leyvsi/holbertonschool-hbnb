#!/usr/bin/python3
"""Place API endpoints"""
from flask_restx import Namespace, Resource, fields
from app.services import facade

# Use 'ns' as agreed for consistency
ns = Namespace('places', description='Place operations')

# Related entity models using 'ns'
amenity_model = ns.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = ns.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name'),
    'last_name': fields.String(description='Last name'),
    'email': fields.String(description='Email')
})

review_model = ns.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Review text'),
    'rating': fields.Integer(description='Rating (1-5)'),
    'user_id': fields.String(description='User ID')
})

# Main Place model for input and documentation
place_model = ns.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude'),
    'longitude': fields.Float(required=True, description='Longitude'),
    'owner_id': fields.String(required=True, description='ID of the owner')
})

@ns.route('/')
class PlaceList(Resource):
    @ns.expect(place_model)
    @ns.response(201, 'Place successfully created')
    @ns.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        try:
            new_place = facade.create_place(ns.payload)
            return {
                'id': new_place.id,
                'title': new_place.title,
                'price': new_place.price,
                'owner_id': new_place.owner.id
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @ns.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve all places"""
        places = facade.get_all_places()
        return [{
            'id': p.id,
            'title': p.title,
            'price': p.price
        } for p in places], 200

@ns.route('/<place_id>')
class PlaceResource(Resource):
    @ns.response(200, 'Place details retrieved successfully')
    @ns.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'email': place.owner.email
            }
        }, 200
