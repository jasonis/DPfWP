
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

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
