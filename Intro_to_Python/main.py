# one line comments
'''
multiple line comments
doc strings
'''
'''
first_name = "Kermit"
last_name = "De Frog"

#response = raw_input("enter your name  ")
#print "hello there, ", response

birth_year = 1923
current_year = 2014
age = current_year - birth_year
#print "your are " + str(age) + " years old"

budget = 900

if budget > 100:
    shoes = "nike"
    print "yay, I get cool " + shoes + " shoes to wear!"
elif budget > 50:
    print "at least I can get some generic sneakers"
else:
    print "aww, no cool shoes for me"

characters = ["leia", "luke", "chewie", "lando"]
characters.append("obi wan")
#print characters[0]

movies = dict() #creates dictionary object
movies = {"star wars":"darth vader", "silence of the lambs":"hanibal lecter"}
print movies['silence of the lambs']

# while loop
i = 0

while i < 9:
    print "the value of i is ", i
    i = i + 1

# for loop
for i in range(0, 10):
    print "the value of i is ", i
    i = i + 1

'''

# for each loop
rappers = ["Tupac", "Nas", "Biggie Smalls"]
for r in rappers:
    #print "One of the best rappers is " + r
    pass

# functions
def calcArea(h, w):
    area = h * w
    return area

a = calcArea(20, 40)
print "my area is " + str(a) + " square feet"

weight = 200
height = 63
message = '''
Your height is {height} and your weight is {weight}
'''

message = message.format(**locals())
print message



