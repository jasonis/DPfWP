# Jason Slocum
# 5.7.2014
# Lab 1 Madlib

current_year = 2014
current_age = response = input("How old are you currently?")
fav_movie = response = raw_input("What is your favorite movie?")
movie_year = response = input("What year did it come out?")

def calculate_age(cy, my, ca):
    movie_age = cy - my
    your_age = ca - movie_age
    return your_age
a = calculate_age(current_year, movie_year, current_age)

print "You were approximately " + str(a) + " years old when " + fav_movie + " was released"

if a < 16:
    print "If you saw it in the theater, your parents must have taken you!"
else:
    print "If you saw it in the theater, you could have driven yourself!"

frequency = response = input("How many times did you watch " + str(fav_movie) + " in the last year?")

def lifetime_views(cy, my, f):
    movie_age = cy - my
    times_watched = movie_age * f
    return times_watched