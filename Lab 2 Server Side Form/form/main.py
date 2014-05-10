
# Jason Slocum
# 5.9.2014
# DPW
# Simple Form
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" ?>
    </head>
    <body>"""
        page_body = """
        <form method="GET">
            <label>First Name* </label><input type="text" name="firstname" />
            <label>Last Name* </label><input type="text" name="lastname" />
            <label>Email* </label><input type="text" name="email" />
            <label>Website URL </label><input type="text" name="weburl" />
            <label>How Can We Help&#63;</label><textarea rows="15" cols="50" name="message" ></textarea>
            <input type="submit" value="Send" />"""
        page_close = """
        </form>
    </body>
</html
"""
        if self.request.GET[]:
            firstname = self.request.GET["firstname"]
            self.response.write(page_head + firstname + page_body + page_close)
        else:
            self.response.write(page_head + firstname + page_body + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
