"""
Jason Slocum
5.28.2014
DPW
Final API
"""

class Page(object):
    def __init__(self):
        self._head ="""
<!DOCTYPE>
<html>
    <head>
        <title>Belong</title>
    
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
    def print_out(self):
        return self._head + self._body + self._close