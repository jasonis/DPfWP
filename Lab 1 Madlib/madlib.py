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