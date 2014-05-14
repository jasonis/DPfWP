
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
            <ul>
                <li><button>Jason</button></li>
                <li><button>Katie</button></li>
                <li><button>Isaac</button></li>
                <li><button>Ella</button></li>
                <li><button>Chewie</button></li>
                <li><button>Otis</button></li>
            </ul>
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
