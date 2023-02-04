from films import movies

def imdb_high_list(movies):
    sorted_movies = []
    for i in movies:
        imdb = i["imdb"]
        if imdb > 5.5:
            sorted_movies.append(i)
    print(sorted_movies)

imdb_high_list(movies)        