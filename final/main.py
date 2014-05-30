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

        if self.request.GET:
            em = EstateModel()
            em.city = self.request.GET['city']
            em.state = self.request.GET['state']
            em.callApi()

            ev = EstateView()
            ev.edos = em.dos
            p._body = ev.content
        self.response.write(p.print_out())


class EstateView(object):
    def __init__(self):
        self.__edos = []
        self.__content = '<br />'

    def update(self):
        for do in self.__edos:
            self.__content += "<div id='maincontent'>"
            self.__content += "</div>"

    @property
    def content(self):
        return self.__content

    @property
    def edos(self):
        pass

    @edos.setter
    def edos(self, arr):
        self.__edos = arr
        self.update()

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

        list = self.__xmldoc.getElementsByTagName('response')
        self._dos = []
        for tag in list:
            do = EstateData()
            do.value = tag.getElementsByTagName('value')[2].firstChild.nodeValue
            do.value2 = tag.getElementsByTagName('value')[3].firstChild.nodeValue
            do.value5 = tag.getElementsByTagName('value')[6].firstChild.nodeValue
            do.value6 = tag.getElementsByTagName('value')[7].firstChild.nodeValue
            do.value7 = tag.getElementsByTagName('value')[8].firstChild.nodeValue
            do.value8 = tag.getElementsByTagName('value')[9].firstChild.nodeValue
            do.value9 = tag.getElementsByTagName('value')[10].firstChild.nodeValue
            do.value10 = tag.getElementsByTagName('value')[11].firstChild.nodeValue
            do.value3 = tag.getElementsByTagName('value')[4].firstChild.nodeValue
            do.value4 = tag.getElementsByTagName('value')[5].firstChild.nodeValue
            do.forSale = tag.getElementsByTagName('forSale')[0].firstChild.nodeValue
            do.location = tag.getElementsByTagName('city')[0].firstChild.nodeValue
            self._dos.append(do)

    @property
    def dos(self):
        return self._dos

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
        self.value = ''
        self.value2 = ''
        self.value3 = ''
        self.value4 = ''
        self.forSale = ''
        self.value5 = ''
        self.value6 = ''
        self.value7 = ''
        self.value8 = ''
        self.value9 = ''
        self.value10 = ''
        self.location = ''

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
