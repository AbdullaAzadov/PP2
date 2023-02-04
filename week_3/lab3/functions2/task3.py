from films import movies

def sort_by_category(movies, category):
    sorted_movies = []
    for i in movies:
        if category == i["category"]:
            sorted_movies.append(i)
    print(sorted_movies)

print("Type available category")
print("Thriller, Action, Adventure, Drama, Romance, War, Crime, Comedy, Suspense")
category = input()

sort_by_category(movies, category)        