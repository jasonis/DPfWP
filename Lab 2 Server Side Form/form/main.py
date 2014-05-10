
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
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>"""
        page_body = """
        <h1>Want to learn more about us&#63;<h1>
        <p>Sign up today and find out how we help businesses and individuals make their dream websites a reality<p>
        <form method="GET">
            <div>
                <ul>
                    <li>
                        <label>First Name* </label>
                        <input type="text" name="firstname" />
                    </li>
                    <li>
                        <label>Last Name* </label>
                        <input type="text" name="lastname" />
                    </li>
                    <li>
                        <label>Email* </label>
                        <input type="text" name="email" />
                    </li>
                    <li>
                        <label>Website URL </label>
                        <input type="text" name="weburl" />
                    </li>
                    <li>
                        <label>How Can We Help&#63;</label>
                        <textarea rows="15" cols="50" name="message" ></textarea>
                    </li>
                    <li>
                        <input type="checkbox" name="alertsbox" value="albox">Sign me up for email alerts
                    </li>
                    <li>
                        <input type="submit" value="Send" />
                    </li>
                </ul>
            </div>"""
        page_close = """
        </form>
    </body>
</html
"""
        if self.request.GET:
            firstname = self.request.GET["firstname"]
            lastname = self.request.GET["lastname"]
            email = self.request.GET["email"]
            weburl = self.request.GET["weburl"]
            message = self.request.GET["message"]
            self.response.write(page_head + firstname + " " + lastname + " " + email + " " + weburl + " " + message + " " + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
