
# Jason Slocum
# 5.9.2014
# DPW
# Simple Form
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = """

        page_body = """

        page_close = """

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
