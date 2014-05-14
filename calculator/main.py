
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Family Water Consumption</title>
        <link href="css/style.css" rel="stylesheet" type"text/css" />
    </head>
    <body>"""
        page_body = """
        <h1>Family Water Consumption</h1>
        <div>
            <ul>
                <li>Jason</li>
                <li>Katie</li>
                <li>Isaac</li>
                <li>Ella</li>
                <li>Chewie</li>
                <li>Otis</li>
            </ul>
        </div>
"""


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
