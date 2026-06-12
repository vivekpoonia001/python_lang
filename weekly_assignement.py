movies = [ { "name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },
{ "name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action",
"Adventure", "Drama"] }, { "name": "Back to the Future", "year": 1985, "duration": 114,
"genres": ["Adventure", "Comedy", "Sci-Fi"] } ]
print("Welcome!!")
def input_int(prompt):
    while True :
        num= int(input(prompt))
        if num>=1:
            return num 
        else:
            print("enter valid number")

def input_something(prompt):
    while True:
        str = input(prompt).strip()
        if str:
            return str
        else:
            print("enter a valid string")
    
while True:
    print("enter your choice")
    choice = input("Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit").lower()
    if choice=="a":
        movies_name = input_something("enter movie name")
        release_year = input_int("enter year ")
        duration = input_int("enter duration in minutes")
        geners = input_something("enter genres")
        genres = [genres.strip() for genres in genres.split(",")]
        movie = {"name": movie, "year": year, "duration":duration, "genres" : genres}
        movies.append(movie)
        print("movies added succsfully")
        print(movie)
    elif choice =="l":
       if not movies:
           print("invalid choice")
       else:
           for index, movies in enumerate(movies, start = 1):
               print(f"{index} {movie['name']} {movie['year']}")
    elif choice == "s":
        if len(movies==0):
            print("no movies saved")
        else:
            search = input_something("enter search term").lower()
            for index , movies in enumerate(movies, start = 1):
                if search in movies['name'].lower():
                    print(f"{index}) {movie['name']} {movie['year']}")

    elif choice == "v":
        if len(movies==0):
            print("no movies saved")
        else: 
            index = input_int("enter index number")   
            if index <0:
                print("invalid index")
            else: movie = movies[index-1]
            print(f"{index}{movies['name']} {movies['year']}{movies['duration']}{movies['genres']}")

    elif choice == "d":
        if len(movies==0):
            print("movies not saved")
        else:
            index = input_int("enter index you want to delete ")
            if 1<=index<=len(movies):
                del_movies = movie[index-1]
                del movies[index-1]
                print("the movie is deleted",{del_movies})
            else:
                print("invalid index number")
    elif choice== "q":
        print("good bye")
    else:
        print("invalid choice")

                








    