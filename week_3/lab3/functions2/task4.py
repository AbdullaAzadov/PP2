from films import movies

def average_imdb(movies):
    cnt = 0
    imdb_sum = 0
    for i in movies:
        cnt+=1
        imdb_sum += i["imdb"]
    return(imdb_sum/cnt)

print(average_imdb(movies))      