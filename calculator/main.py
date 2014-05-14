
import webapp2

from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        ji = Family_Member()
        ji.name = "Jason"
        ji.status = "father"
        ji.water_morning = 50
        ji.water_afternoon = 30
        ji.water_evening = 30
        ji.total_water()

        ka = Family_Member()
        ka.name = "Katie"
        ka.status = "mother"
        ka.water_morning = 30
        ka.water_afternoon = 30
        ka.water_evening = 20
        ka.total_water()

        ij = Family_Member()
        ij.name = "Isaac"
        ij.status = "son"
        ij.water_morning = 20
        ij.water_afternoon = 20
        ij.water_evening = 40
        #ij.total_water()

        ea = Family_Member()
        ea.name = "Ella"
        ea.status = "daughter"
        ea.water_morning = 10
        ea.water_afternoon = 20
        ea.water_evening = 20
        ea.total_water()

        ch = Family_Member()
        ch.name = "Chewie"
        ch.status = "dog1"
        ch.water_morning = 3
        ch.water_afternoon = 4
        ch.water_evening = 2
        ch.total_water()

        ot = Family_Member()
        ot.name = "Otis"
        ot.status = "dog2"
        ot.water_morning = 4
        ot.water_afternoon = 4
        ot.water_evening = 3
        ot.total_water()

        family = [ji, ka, ij, ea, ch, ot]

        if self.request.GET:
            self.response.write(p.page_head + p.page_body + p.page.close)
        else:
            self.response.write(p.page_head + p.page_body + p.page_close)


class Family_Member(object):
    def __init__(self):
        self.name = ""
        self.status = ""
        self.water_morning = 0
        self.water_afternoon = 0
        self.water_evening = 0
        #self.total_water = 0

    def total_water(self):
        self.__water_consumed = self.water_morning + self.water_afternoon + self.water_evening


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
