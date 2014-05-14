
import webapp2

from p import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
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
                <li><button>Jason</button></li>
                <li><button>Katie</button></li>
                <li><button>Isaac</button></li>
                <li><button>Ella</button></li>
                <li><button>Chewie</button></li>
                <li><button>Otis</button></li>
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

        k = Family_Member()
        k.name = "Katie"
        k.status = "mother"
        k.water_morning = 30
        k.water_afternoon = 30
        k.water_evening = 20
        k.total_water()

        i = Family_Member()
        i.name = "Isaac"
        i.status = "son"
        i.water_morning = 20
        i.water_afternoon = 20
        i.water_evening = 40
        i.total_water()

        e = Family_Member()
        e.name = "Ella"
        e.status = "daughter"
        e.water_morning = 10
        e.water_afternoon = 20
        e.water_evening = 20
        e.total_water()

        c = Family_Member()
        c.name = "Chewie"
        c.status = "dog1"
        c.water_morning = 3
        c.water_afternoon = 4
        c.water_evening = 2
        c.total_water()

        o = Family_Member()
        o.name = "Otis"
        c.status = "dog2"
        o.water_morning = 4
        o.water_afternoon = 4
        o.water_evening = 3
        o.total_water()

        family = [j, k, i, e, c, o]

class Family_Member(object):
    def __init__(self):
        self.name = ""
        self.status = ""
        self.water_morning = 0
        self.water_afternoon = 0
        self.water_evening = 0
        self.__total_water = 0


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
