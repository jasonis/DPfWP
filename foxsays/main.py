
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
