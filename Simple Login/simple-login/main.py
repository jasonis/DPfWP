
'''
Jason Slocum
5.6.14
DPW
Classes
'''

import webapp2 # use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): # function that starts everything
        page_head = """
        <!DOCTYPE HTML>
        <html>
            <head>
                <title>Simple Login</title>
            </head>
            <body>"""
        page_body = """
                <form method="GET">
                    <label>Name: </label><input type="text" name="user" />
                    <label>Email: </label><input type="text" name="email" />
                    <input type="submit" value="Submit" />"""
        page_close = """
                </form>
            </body>
        </html>
        """
        if self.request.GET:
            #storing info we got from the user
            user = self.request.GET["user"]
            email = self.request.GET["email"]
            self.response.write(page_head + user + ' ' + email + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close)#printing to the webpage


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
