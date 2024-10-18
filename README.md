# Movie Recommendation API

This is a RESTful API for movie recommendations using collaborative filtering.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/movie-recommendation-api.git
   cd movie-recommendation-api
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Download the MovieLens dataset:
   - Go to https://grouplens.org/datasets/movielens/latest/
   - Download the small dataset (ml-latest-small.zip)
   - Extract the contents and place `movies.csv` and `ratings.csv` in the `data` folder

5. Run the Flask application:
   ```
   python run.py
   ```

## API Usage

To get movie recommendations, send a POST request to `/api/recommend` with the following JSON payload:
```
{
"user_id": 1,
"movies": ["Toy Story", "Jurassic Park", "Forrest Gump"]
}

```

The API will return a list of recommended movies with their estimated ratings.