from data import load_movies

def recommend_movies(user_genre):
    movies = load_movies()

    recommendations = movies[
        movies["Genre"].str.lower() ==
        user_genre.lower()
    ]

    return recommendations