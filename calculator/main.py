# Jason Slocum
# DPW
# 5.15.14
# encapsulated calculator
import webapp2

from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        ji = FamilyMember()
        ji.name = "Jason"
        ji.status = "father"
        ji.water_morning = 50
        ji.water_afternoon = 30
        ji.water_evening = 30

        ka = FamilyMember()
        ka.name = "Katie"
        ka.status = "mother"
        ka.water_morning = 30
        ka.water_afternoon = 30
        ka.water_evening = 20

        ij = FamilyMember()
        ij.name = "Isaac"
        ij.status = "son"
        ij.water_morning = 20
        ij.water_afternoon = 20
        ij.water_evening = 40

        ea = FamilyMember()
        ea.name = "Ella"
        ea.status = "daughter"
        ea.water_morning = 10
        ea.water_afternoon = 20
        ea.water_evening = 20

        ch = FamilyMember()
        ch.name = "Chewie"
        ch.status = "dog1"
        ch.water_morning = 3
        ch.water_afternoon = 4
        ch.water_evening = 2

        ot = FamilyMember()
        ot.name = "Otis"
        ot.status = "dog2"
        ot.water_morning = 4
        ot.water_afternoon = 4
        ot.water_evening = 3

        family = [ji, ka, ij, ea, ch, ot]

        self.response.write(p.header())
        self.response.write(p.form())

        if self.request.GET:
            member = (int(self.request.GET['member']))-1
            print member
            self.response.write(self.html(members[member]))
        self.response.write(p.footer())
    def display(self,obj):

        total = obj.water_morning + obj.water_afternoon + obj.water_evening

        result = '''
        <div class = 'container' id='result'>
            <h1>{obj.name}</h1>
            <ul>
                <li>Name: ${obj.status}</li>
                <li>Water Drank in the Morning: {obj.water_morning}</li>
                <li>Water Drank in the Afternoon: {obj.water_afternoon}</li>
                <li>Water Drank in the Evening: {obj.water_evening}</li>
                <li id='total'>Daily Total: {total} ounces of water</li>
            </ul>
        </div>'''
        result = result.format(**locals())
        return result



class FamilyMember(object):
    def __init__(self):
        self.name = ""
        self.status = ""
        self.__water_morning = 0
        self.__water_afternoon = 0
        self.__water_evening = 0
        self.__total = 0

    @property
    def water_morning(self):
        return self.__water_morning

    @water_morning.setter
    def water_morning(self, new_water_morning):
        self.__water_morning = new_water_morning

    @property
    def water_afternoon(self):
        return self.__water_afternoon

    @water_afternoon.setter
    def water_afternoon(self, new_water_afternoon):
        self.__water_morning = new_water_afternoon

    @property
    def water_evening(self):
        return self.__water_evening

    @water_evening.setter
    def water_morning(self, new_water_evening):
        self.__water_evening = new_water_evening

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, new_total):
        self.__total = new_total


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
