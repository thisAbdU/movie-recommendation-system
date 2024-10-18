from flask import Blueprint, request, jsonify
from app.services.recommendation_service import RecommendationService

api = Blueprint('api', __name__)
recommendation_service = RecommendationService()

@api.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_id = data.get('user_id')
    movie_titles = data.get('movies', [])
    
    if not user_id or not movie_titles:
        return jsonify({'error': 'Missing user_id or movies'}), 400
    
    recommendations = recommendation_service.recommend_movies(user_id, movie_titles)
    return jsonify({'recommendations': recommendations})