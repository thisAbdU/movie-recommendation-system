import numpy as np
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split

class MovieRecommender:
    def __init__(self, ratings_df):
        self.model = SVD()
        self.train_model(ratings_df)

    def train_model(self, ratings_df):
        reader = Reader(rating_scale=(0.5, 5))
        data = Dataset.load_from_df(ratings_df[['userId', 'movieId', 'rating']], reader)
        trainset, _ = train_test_split(data, test_size=0.2, random_state=42)
        self.model.fit(trainset)

    def predict_rating(self, user_id, movie_id):
        return self.model.predict(user_id, movie_id).est