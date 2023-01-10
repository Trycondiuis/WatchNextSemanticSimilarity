import spacy


"""
    Function that takes one argument from main program and will return a list with new values. the function will 
    have the 'en_core_web_md' model from spacy, which will be use to create tokens of the string passed and compare
    these to the tokens created when reading each line in the movie file. A conditional statement will check if
    the word vectors from the argument passed and the data in the file are greater or equal than 0.85 and will return
    all the data in the file if the condition is true.    
"""


def movies_similarity(movie_similarity):
    nlp = spacy.load('en_core_web_md')

    # tokenizing the argument passed, and declaring an empty list
    movie_s = nlp(movie_similarity)
    suggested_movie = []

    # try exception to prevent an error if the file is non-existent or was accidentally deleted, and will print a
    # user-friendly message to the user
    try:

        # open the file and read its contents
        with open('./movies.txt', 'r', encoding='utf-8-sig') as movie_file:

            # for loop to iterate the contents of the file and tokenize the results.
            for lines in movie_file:
                movie_token = nlp(lines)

                # below print statement was not use as it was not requested in the task criteria, but its purpose is
                # to print out in a user-friendly format all the movie names in file with their similarity to the
                # argument passed.
                # print(movie_token[0], movie_token[1], movie_token[2], movie_token[3:].similarity(movie_s))

                # conditional statement to check if the similarity between movies description in file and
                # the description passed as an argument are equal or greater than 0.85. If they are, the movies
                # in file with word vectors greater than 0.85 will be appended to a new list along with the movie names.
                if movie_token[3:].similarity(movie_s) >= 0.85:
                    new_movies = movie_token[0], movie_token[1], movie_token[2], movie_token[3:].similarity(movie_s)
                    suggested_movie.append(new_movies)

        # return a list of new movies.
        return suggested_movie

    except FileNotFoundError as error:

        print("\nThe file that you are trying to open does not exist")
        print(error)
        print()


# declaring two variables that will store the title and the description of the movie recently watched by the user.
movie_title = "Planet Hulk"
movie_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,\n" \
        "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live\n" \
        "in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained\n" \
        "as a gladiator."

# prints user-friendly message showing the user the title and the description of the movie recently watched.
print("You have watched", movie_title)
print(movie_description)
print()
print("\tMovies that we think you may like to watch next:")
print("="*57)

"""
    The below for loop will call the function above passing one argument that contains the description of the movie seen
    by the user. it will then iterate the returned list of movies from the file to print a user-friendly message.
"""

# for loop to iterate the returned list that contains all the movies in the file that are similar to the movie watched
# by the user, and prints a user-friendly message with the name of the movies in the file, the similarity vector,
# and the name of the movie just watched
for num, suggested_movies in enumerate(movies_similarity(movie_description), start=1):
    print("[", num, "]", *suggested_movies[:-2], "with", *suggested_movies[-1:], "similarity to", movie_title)
