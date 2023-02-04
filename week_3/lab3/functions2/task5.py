from films import movies

def average_imdb_category(movies, category):
    cnt = 0
    imdb_sum = 0
    for i in movies:
        if category == i["category"]:
            cnt+=1  
            imdb_sum += i["imdb"]
    return(imdb_sum/cnt)

print("Type available category")
print("Thriller, Action, Adventure, Drama, Romance, War, Crime, Comedy, Suspense")
category = input()    

print(average_imdb_category(movies, category))    