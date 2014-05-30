"""
Jason Slocum
5.28.2014
DPW
Final API
"""
import webapp2
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

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
