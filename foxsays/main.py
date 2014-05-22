
import webapp2

from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()

        dog = Canis()
        dog.name = 'Yorkshire Terrier'

        horse = Equus()
        horse.name = 'Horse'

        raccoon = Procyon()
        raccoon.name = 'Raccoon'

        animals = [dog, horse, raccoon]

        self.response.write(page.header())
        self.response.write(page.form())
        if self.request.GET:
            animal = (int(self.request.GET['animal']))-1
            print animal
            self.response.write(page.template(animals[animal]))
        self.response.write(page.footer())

class abstract_animal(object):
    def __init__(self):
        self._phy = 'Chordata'
        self._say = ''

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

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
