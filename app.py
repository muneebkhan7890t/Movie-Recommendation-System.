from recommender import recommend_movies

print("Movie Recommendation System")

genre = input(
    "Choose Genre (Action, Comedy, Romance, Horror, Sci-Fi): "
)

results = recommend_movies(genre)

if len(results) > 0:
    print("\nRecommended Movies:")

    for movie in results["Movie"]:
        print(movie)

else:
    print("No recommendation found")