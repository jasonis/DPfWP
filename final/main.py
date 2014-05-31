"""
Jason Slocum
5.28.2014
DPW
Final API
"""
import webapp2
from pages import Page
import urllib2 #open url, request receive and open info obtained there
from xml.dom import minidom#parse xml

class MainHandler(webapp2.RequestHandler):
    """controls the interaction between the model and the view"""
    def get(self):
        p = FormPage()#creating the page
        p.inputs = [['city', 'text', 'City'], ['state', 'text', 'State'], ['Submit', 'submit']]#creates the form inputs and contains their name, type and placeholder

        if self.request.GET:
            em = EstateModel()#creating the model
            em.city = self.request.GET['city']#this sends the city that the user enters from the view to the model
            em.state = self.request.GET['state']#this sends the state that the user enters from the view to the model
            em.callApi()#calls the callAPI function

            ev = EstateView()#creating the view
            ev.edos = em.dos#takes data objects from EstateModel and gives them to the EstateView
            p._body = ev.content#takes the content from the view and adds it to the body
        self.response.write(p.print_out())#displays the form


class EstateView(object):
    ''' this class handles how the info is shown to the user'''
    def __init__(self):
        self.__edos = []
        self.__content = '<br />'

    def update(self):#this function goes through the array self.__edos and updates the info with the content from the api
        for do in self.__edos:
            self.__content += "<div id='maincontent'>"
            self.__content += "<h2 id='cta'>" + "Enter a location to find out where you belong&excl;" + "</h2>"
            self.__content += "<div class='box'>"
            self.__content += "<h2>" + "Affordability of Homes in " + do.location + "</h2>"
            self.__content += "<h3>" + "Single Family Homes" + "</h3>"
            self.__content += "<p>" + "The average single family home is valued at: $" + do.value + "<br />"
            self.__content += "While the national average for a comparable home is: $" + do.value2 + "</p>"
            self.__content += "<h3>" + "Two Bedroom Homes" + "</h3>"
            self.__content += "<p>" + "The average two bedroom home is valued at: $" + do.value5 + "<br />"
            self.__content += "While the national average for a comparable home is: $" + do.value6 + "</p>"
            self.__content += "<h3>" + "Three Bedroom Homes" + "</h3>"
            self.__content += "<p>" + "The average three bedroom home is valued at: $" + do.value7 + "<br />"
            self.__content += "While the national average for a comparable home is: $" + do.value8 + "</p>"
            self.__content += "<h3>" + "Four Bedroom Homes" + "</h3>"
            self.__content += "<p>" + "The average four bedroom home is valued at: $" + do.value9 + "<br />"
            self.__content += "While the national average for a comparable home is: $" + do.value10 + "</p>"
            self.__content += "<h3>" + "Condos" + "</h3>"
            self.__content += "<p>" + "The average condo is valued at: $" + do.value3 + "<br />"
            self.__content += "While the national average for a comparable condo is: $" + do.value4 + "</p>"
            self.__content += "<a href='" + do.forSale + "'>Check Out Current Home Listings&excl;</a>" + "</div>"
            self.__content += "</div>"

    #getters and setter that return the content and call the update function
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
    '''this model will handle fetching parsing and sorting data from the Zillow api '''
    def __init__(self):#this function gets the api and hold the users city and state info
        self.__url = "http://www.zillow.com/webservice/GetDemographics.htm?zws-id=X1-ZWz1dtxmglnsi3_4aijl&state="#api url with the key
        self.__city = ""
        self.__state = ""
        self.__xmldoc = ""

    def callApi(self):
        request = urllib2.Request(self.__url+self.__state+"&city="+self.__city)#requests and loads data from the api
        opener = urllib2.build_opener()#use urllib2 to create an object to get the url
        result = opener.open(request)#use the url to get a result - request info from the api

        self.__xmldoc = minidom.parse(result)#parsing the data

        list = self.__xmldoc.getElementsByTagName('response')#creates the variable 'list' and gets the tag 'response' from the xml
        self._dos = []#holds the info collected from the api
        for tag in list:
            do = EstateData()#calls the EstateData function
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
            self._dos.append(do)#adds all of the data objects to _dos

    #getters and setters that return the city, state and objects
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
    '''this data object holds the data fetched by the model and shown by the view '''
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

class FormPage(Page):#FormPage class, inherits from the Page class
    """this page sets up the basic html"""
    def __init__(self):
        super(FormPage, self).__init__()#Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''

    @property#getter
    def inputs(self):
        pass

    @inputs.setter#setter
    def inputs(self, arr):
        self.__inputs = arr

        for item in arr:#loops through the items in the array, if there is a third item it will be added otherwise it will close the tag
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            except:
                self._form_inputs += '" />'

    def print_out(self):#this function creates the html by returning the necessary attributes
        return self._head + self._form_open + self._form_inputs + self._form_close + self._body + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
