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

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
