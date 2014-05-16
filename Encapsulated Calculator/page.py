# Jason Slocum
# DPW
# 5.15.14
# encapsulated calculator

class Page():
    def __init__(self):
        self.__header = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Family Water Consumption</title>
        <link href="css/style.css" rel="stylesheet" type"text/css" />
        <link href='http://fonts.googleapis.com/css?family=Pompiere' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Yanone+Kaffeesatz:200' rel='stylesheet' type='text/css'>
    </head>
    <header>
        <h1>Hydration.com</h1>
    </header>
    <body>"""
        self.__form = """
        <h1>Family Water Consumption</h1>
        <div>
            <form method="GET" >
                <a href="/?fm=1" name="member" id="Jason">Jason</a>
                <a href="/?fm=2" name="member" id="Katie">Katie</a>
                <a href="/?fm=3" name="member" id="Isaac">Isaac</a>
                <a href="/?fm=4" name="member" id="Ella">Ella</a>
                <a href="/?fm=5" name="member" id="Chewie">Chewie</a>
                <a href="/?fm=6" name="member" id="Otis">Otis</a>
            </form>
        </div>
"""
        self.__footer = """
    </body>
</html>"""

    def header(self):
        return self.__header

    def form(self):
        return self.__form

    def footer(self):
        return self.__footer
