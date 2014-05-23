"""
Jason Slocum
5.22.2014
DPW
What Does the Fox Say?
"""
import webapp2

from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()# Instantiate Page()

        dog = Canis()# creating instance of dog sub class
        dog.name = 'Yorkshire Terrier'

        horse = Equus()#creating an instance of horse sub class
        horse.name = 'Horse'

        raccoon = Procyon()#creating an instance of raccoon sub class
        raccoon.name = 'Raccoon'

        animals = [dog, horse, raccoon]#array of animals

        #displays the html page and displays the appropriate info for the requested animal
        self.response.write(page.header())
        self.response.write(page.form())
        if self.request.GET:
            animal = (int(self.request.GET['animal']))-1
            print animal
            self.response.write(page.template(animals[animal]))
        self.response.write(page.footer())

class abstract_animal(object):   #superclass
    def __init__(self):
        self._phy = 'Chordata'
        self._say = 'RAWR'

    #getters
    @property
    def phy(self):
        return self._phy

    @property
    def url(self):
        return self._url

    @property
    def avg_life(self):
        return self._avg_life

    @property
    def hab(self):
        return self._hab

    @property
    def geo(self):
        return self._geo

    @property
    def say(self):
        return self._say

# animal orders
class Mammalia(abstract_animal):
    def __init__(self):
        abstract_animal.__init__(self)#initializes and inherits info from abstract_animal
        self._class = 'Mammalia'

    #Getter for Class
    def classes(self):
        return self._class

class Carnivora(Mammalia):
    def __init__(self):
        Mammalia.__init__(self)#initializes and inherits info from Mammalia
        self._order = 'Carnivora'

    #Getter for Class
    @property
    def order(self):
        return self._order

class Perissodactlya(Mammalia):
    def __init__(self):
        Mammalia.__init__(self)#initializes and inherits info from Mammalia
        self._order = 'Perissodactlya'

    #Getter for Class
    @property
    def order(self):
        return self._order

class Procyonidae(Mammalia):
    def __init__(self):
        Mammalia.__init__(self)#initializes and inherits info from Mammalia
        self._order = 'Procyonidae'

    #Getter for Class
    @property
    def order(self):
        return self._order

# --------- Dog Object ---------
class Canidae(Carnivora):
    def __init__(self):
        Carnivora.__init__(self)#initializes and inherits info from Carnivora
        self._fam = 'Canidae'

    #Getter
    @property
    def fam(self):
        return self._fam

class Canis(Canidae):
    def __init__(self):
        Canidae.__init__(self)#initializes and inherits info from Canidae
        self._gen = 'Canis'
        self._url = 'images/dog.jpg'
        self._avg_life = '12.8 years'
        self._hab = 'In your home'
        self._geo = 'Worldwide'
        self._say = 'Woof'

    #Getter
    @property
    def gen(self):
        return self._gen

# --------- Horse Object ---------
class Equidae(Perissodactlya):
    def __init__(self):
        Perissodactlya.__init__(self)#initializes and inherits info from Perissodactlya
        self._fam = 'Equidae'

    #Getter
    @property
    def fam(self):
        return self._fam

class Equus(Equidae):
    def __init__(self):
        Equidae.__init__(self)#initializes and inherits info from Equidae
        self._gen = 'Equus'
        self._url = 'images/horse.jpg'
        self._avg_life = '28 years'
        self._hab = 'Farms and Natural Prairies'
        self._geo = 'Non-arctic regions worldwide'
        self._say = 'Neigh'

    #Getter
    @property
    def gen(self):
        return self._genus

# --------- Racoon Object ---------
class Procyonidae(Carnivora):
    def __init__(self):
        Carnivora.__init__(self)#initializes and inherits info from Carnivora
        self._fam = 'Procyonidae'

    #Getter
    @property
    def fam(self):
        return self._fam

class Procyon(Procyonidae):
    def __init__(self):
        Procyonidae.__init__(self)#initializes and inherits info from Procyonidae
        self._gen = 'Procyonidae'
        self._url = 'images/raccoon.jpg'
        self._avg_life = '2-3 years'
        self._hab = 'Tree cavities and burrows'
        self._geo = 'Native to N. America and now also northern Europe'
        self._say = 'Chitter Chitter'

    #Getter
    @property
    def gen(self):
        return self._genus

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
