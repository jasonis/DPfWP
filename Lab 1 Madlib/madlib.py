# Jason Slocum
# 5.7.2014
# Lab 1 Madlib

"""
Finding out about the users favorite movie,
how much they watch it
and what they like to snack on when they view it
"""

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

lv = lifetime_views(current_year, movie_year, frequency)

if frequency < 1:
    print "But I though it was your favorite?!"
elif frequency < 5:
    print "You definitely do like " + str(fav_movie) + " ! At that rate, you have seen it approximately " + str(lv) + " times in your life!"
else:
    print "Wow! You sure do love " + str(fav_movie) + " ! At that rate, you have seen it approximately " + str(lv) + " times in your life!"

foods = ["popcorn", "nachos", "candy"]

your_foods = response = raw_input("A couple of common movie foods are " + str(foods[0]) + " and " + str(foods[2]) + ". " " What else do you like?")

foods.append(your_foods)

print "Now we've got a pretty good selection to choose from!"

for i in foods:
    print i

print "The tough part now is trying to decide!"

pairings = dict()
pairings = {"popcorn":"soda", "nachos":"beer", "candy":"water"}
print "If you get thirsty eating all of this, I would recommend "  + str(pairings['popcorn']) + " with your popcorn, " + str(pairings['nachos']) + " with your nachos and " + str(pairings['candy']) + " with your candy."

satisfaction = response = raw_input("Did you find this questionnaire enjoyable? ('yes' or 'no')")

if satisfaction == "yes":
    print "Thanks, I'm glad you liked it!"
else:
    print "Maybe if you tried it once more it would change your mind"
