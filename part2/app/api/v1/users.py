#!/usr/bin/python3
"""User API endpoints"""
from flask_restx import Namespace, Resource, fields
from app.services import facade

ns = Namespace('users', description='User operations')

user_model = ns.model('User',{
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
    'password': fields.String(description='User password')
})

@ns.route('/')
class UserList(Resource):
    @ns.expect(user_model, validate=True)
    @ns.response(201, 'User successfully created')
    @ns.response(400, 'Email already registered')
    @ns.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = ns.payload


        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        try:
            # Create the user through the facade
            new_user = facade.create_user(user_data)
            return {
                'id': new_user.id,
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email
            }, 201
        except ValueError as e:
            # Handle validation errors
            return {'error': str(e)}, 400
