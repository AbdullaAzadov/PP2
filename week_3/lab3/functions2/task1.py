from films import movies

def is_imdb_high(movies):
    for i in movies:
        imdb = i["imdb"]
        if imdb > 5.5:
            print(i["name"], "→", True)
        else:
            print(i["name"], "→", False)


is_imdb_high(movies)        