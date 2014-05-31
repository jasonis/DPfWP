"""
Jason Slocum
5.28.2014
DPW
Final API
"""
#the class Page contains html for the page
class Page(object):
    def __init__(self):
        self._head ="""
<!DOCTYPE>
<html>
    <head>
        <title>Belong</title>
        <link href="css/style.css" rel="stylesheet" type"text/css" />
        <link href='http://fonts.googleapis.com/css?family=Lobster' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Merriweather' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Cabin' rel='stylesheet' type='text/css'>
    </head>
    <header>
        <ul>
            <li class="logolink"><a href='http://zillow.com'>Search Homes</a></li>
            <li id="logo">Belong</li>
            <li class="logolink"><a href=''>About Us</a></li>
        </ul>
    </header>
    <body>"""
        self._body ='Property Info'
        self._close ="""
    </body>
</html>"""
    def print_out(self):#this function returns the head, body and close of the html that was created
        return self._head + self._body + self._close