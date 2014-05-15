
# Jason Slocum
# 5.9.2014
# DPW
# Simple Form
import webapp2
from form import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        #conditional that will display the results of the form when the send button is pressed
        if self.request.GET:
            firstname = self.request.GET["firstname"]
            lastname = self.request.GET["lastname"]
            email = self.request.GET["email"]
            weburl = self.request.GET["weburl"]
            message = self.request.GET["message"]
            results = """
            <h1>Thanks for requesting more info&excl;</h1>
            <p>First Name: {firstname}</p>
            <p>Last Name: {lastname}</p>
            <p>Email: {email}</p>
            <p>Current Web URL: {weburl}</p>
            <p>Message: {message}</p>
            """
            results = results.format(**locals())
            self.response.write(p.page_head + results + p.page_close)
        #If the button isn't pressed, this will display the blank form
        else:
            self.response.write(p.page_head + p.page_body + p.page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
