
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['first_name', 'text', 'First Name'], ['last_name', 'text', 'Last Name'], ['Submit', 'submit']]
        self.response.write(p.print_out())

class Page(object):
    def __init__(self):
        self._head ="""
<!DOCTYPE>
<html>
    <head>
        <title></title>
    </head>
    <body>"""
        self._body ='Filler'
        self._close ="""
    </body>
</html>"""
    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()#Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_open = '</form>'
        self.__inputs = []

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr

        for item in arr:
            print item



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
