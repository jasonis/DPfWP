#data objects
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        luke = Character()
        luke.profession = "Jedi Knight"
        luke.age = 26
        luke.home_planet = "tattooine"

        leia = Character()
        leia.name = "Princess Leia"
        leia.profession = "princess"
        leia.age = luke.age
        leia.home_planet = "Alderan"

        yoda = Character()
        yoda.name = "master Yoda"
        yoda.profession = "jedi Knight"
        yoda.age = 762
        yoda.home_planet = "Dagobah"

class Character(object):
    def __init__(self):#constructor function
        self.name = ""
        self.profession = ""
        self.age = 0
        self.home_planet = ""

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
