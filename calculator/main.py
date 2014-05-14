
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
        page_close = """
    </body>
</html>"""

        j = Family_Member()
        j.name = "Jason"
        j.status = "father"
        j.water_morning = 50
        j.water_afternoon = 30
        j.water_evening = 30
        j.total_water()



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
