from flask_restx import Namespace, Resource, fields
from app.services import facade

ns = Namespace('reviews', description='Review operations')

# Define the review model for input valida* and documenta*
review_model = ns.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@ns.route('/')
class ReviewList(Resource):
    @ns.expect(review_model)
    @ns.response(201, 'Review successfully created')
    @ns.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        # Placeholder for the logic to register a new review
        pass

    @ns.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        # Placeholder for logic to return a list of all reviews
        pass

@ns.route('/<review_id>')
class ReviewResource(Resource):
    @ns.response(200, 'Review details retrieved successfully')
    @ns.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        # Placeholder for the logic to retrieve a review by ID
        pass

    @ns.expect(review_model)
    @ns.response(200, 'Review updated successfully')
    @ns.response(404, 'Review not found')
    @ns.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        # Placeholder for the logic to update a review by ID
        pass

    @ns.response(200, 'Review deleted successfully')
    @ns.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        # Placeholder for the logic to dl a review
        if facade.delete_review(review_id):
            return {"message": "Review deleted successfully"}, 200


        return {"message": "Review not found"}, 404
