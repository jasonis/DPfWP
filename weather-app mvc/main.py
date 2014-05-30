
import webapp2
import urllib2 #python code to open url request receive and open info
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'zip code'], ['Submit', 'submit']]

        if self.request.GET:
            #get info from the api
            wm = WeatherModel()#creates the model
            wm.zip = self.request.GET['zip']#sends the zip from the view to the model
            wm.callApi()

            wv = WeatherView()#creates the view
            wv.wdos = wm.dos#takes data objects from the model and gives them to the view
            p._body = wv.content
        self.response.write(p.print_out())

class WeatherView(object):
    ''' this class handles how the info is shown to the user'''
    def __init__(self):
        self.__wdos = []
        self.__content = '<br/>'

    def update(self):
        for do in self.__wdos:
            self.__content += do.day
            self.__content += do.high + "  High:  "

    @property
    def content(self):
        return self.__content

    @property
    def wdos(self):
        pass

    @wdos.setter
    def wdos(self, arr):
        self.__wdos = arr
        self.update()

class WeatherModel(object):
    '''this model will handle fetching parsing and sorting data from yahoo weathers api '''
    def __init__(self):
        self.__url = "http://xml.weather.yahoo.com/forecastrss?p="
        self.__zip = ''
        self.__xmldoc = ''

    def callApi(self):
        #assemble the request

        #requests and loads data from the api
        request = urllib2.Request(self.__url+self.__zip)
        #use urllib2 to create an object to get the url
        opener = urllib2.build_opener()
        #use the url to get a result - request info from the api
        result = opener.open(request)
        #parse the xml

        #parsing data
        self.__xmldoc = minidom.parse(result)

        #sorting data
        list = self.__xmldoc.getElementsByTagName('yweather:forecast')
        self._dos = []
        for tag in list:
            do = WeatherData()
            do.day = tag.attributes['day'].value
            do.high = tag.attributes['high'].value
            do.low = tag.attributes['low'].value
            do.date = tag.attributes['date'].value
            do.code = tag.attributes['code'].value
            do.condition = tag.attributes['text'].value
            self._dos.append(do)

    @property
    def dos(self):
        return self._dos

    @property
    def zip(self):
        pass

    @zip.setter
    def zip(self, z):
        self.__zip = z



class WeatherData(object):
    '''this data object holds the data fetched by the model and shown by the view '''
    def __init__(self):
        self.day = ''
        self.high = ''
        self.low = ''
        self.code = ''
        self.condition = ''
        self.date = ''

class Page(object):
    def __init__(self):
        self._head ="""
<!DOCTYPE>
<html>
    <head>
        <title></title>
    </head>
    <body>"""
        self._body ='Weather-App MVC'
        self._close ="""
    </body>
</html>"""
    def print_out(self):
        return self._head + self._body + self._close

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
