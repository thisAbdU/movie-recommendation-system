import numpy as np
from app.utils.data_loader import load_movies, load_ratings
from app.models.recommender import MovieRecommender

class RecommendationService:
    def __init__(self):
        self.movies_df = load_movies()
        self.ratings_df = load_ratings()
        self.recommender = MovieRecommender(self.ratings_df)

    def get_movie_id(self, movie_title):
        movie = self.movies_df[self.movies_df['title'].str.contains(movie_title, case=False, na=False)]
        if not movie.empty:
            return movie.iloc[0]['movieId']
        return None

    def recommend_movies(self, user_id, movie_titles, n=5):
        user_id = int(user_id)
        movie_ids = [self.get_movie_id(title) for title in movie_titles if self.get_movie_id(title) is not None]
        
        all_movie_ids = self.movies_df['movieId'].unique()
        user_rated_movies = self.ratings_df[self.ratings_df['userId'] == user_id]['movieId'].unique()
        movies_to_predict = np.setdiff1d(all_movie_ids, user_rated_movies)
        
        predictions = [(movie_id, self.recommender.predict_rating(user_id, movie_id)) for movie_id in movies_to_predict]
        predictions.sort(key=lambda x: x[1], reverse=True)
        
        top_n = predictions[:n]
        recommended_movies = []
        for movie_id, est_rating in top_n:
            movie_title = self.movies_df[self.movies_df['movieId'] == movie_id]['title'].values[0]
            recommended_movies.append((movie_title, est_rating))
        
        return recommended_movies