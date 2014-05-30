"""
Jason Slocum
5.28.2014
DPW
Final API
"""
import webapp2
from pages import Page
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['city', 'text', 'City'], ['state', 'text', 'State'], ['Submit', 'submit']]


class EstateView(object):
    def __init__(self):

class EstateModel(object):
    def __init__(self):
        self.__url = "http://www.zillow.com/webservice/GetDemographics.htm?zws-id=X1-ZWz1dtxmglnsi3_4aijl&state="
        self.__city = ""
        self.__state = ""
        self.__xmldoc = ""

    def callApi(self):
        request = urllib2.Request(self.__url+self.__state+"&city="+self.__city)
        opener = urllib2.build_opener()
        result = opener.open(request)

    @property
    def state(self):
        pass

    @state.setter
    def state(self, s):
        self.__state = s

    @property
    def city(self):
        pass

    @city.setter
    def city(self, c):
        self.__city = c

class EstateData(object):
    def __init__(self):

class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()#Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr

        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            except:
                self._form_inputs += '" />'

    def print_out(self):
        return self._head + self._form_open + self._form_inputs + self._form_close + self._body + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
