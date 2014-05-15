
class Page():
    def __init__(self):
        self.page_head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Family Water Consumption</title>
        <link href="css/style.css" rel="stylesheet" type"text/css" />
    </head>
    <body>"""
        self.page_body = """
        <h1>Family Water Consumption</h1>
        <div>
            <form method="GET" >
                <a href="/?fm=1" name="family_member" id="Jason">Jason</a>
                <a href="/?fm=2" name="family_member" id="Katie">Katie</a>
                <a href="/?fm=3" name="family_member" id="Isaac">Isaac</a>
                <a href="/?fm=4" name="family_member" id="Ella">Ella</a>
                <a href="/?fm=5" name="family_member" id="Chewie">Chewie</a>
                <a href="/?fm=6" name="family_member" id="Otis">Otis</a>
            </form>
        </div>
"""
        self.page_close = """
    </body>
</html>"""

    def head(self):
        return self.page_head

    def body(self):
        return self.page_body

    def close(self):
        return self.page_close
