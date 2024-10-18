import pandas as pd

def load_movies():
    return pd.read_csv('data/movies.csv')

def load_ratings():
    return pd.read_csv('data/ratings.csv')