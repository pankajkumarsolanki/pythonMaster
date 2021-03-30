# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

def addMovie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def listMovie():
    if len(movies)<1:
        print("No Movies in DB")
    else:
        for movie in movies:
            print_movie(movie)

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")

def findMovie():
    a = input("Enter the Movie Title: ")
    for movie in movies:
        if a == movie["title"]:
            print_movie(movie)
        else:
            print("Not Found")


user_options = {
    "a": addMovie,
    "l": listMovie,
    "f": findMovie
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()