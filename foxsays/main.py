
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

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
