
import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "my page"
        p.body = "Miss piggy likes Kermit the Frog"
        p.update()
        self.response.write(p.whole_page)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
