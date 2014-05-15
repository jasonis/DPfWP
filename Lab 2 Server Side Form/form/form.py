class Page():
    def __init__(self):
        self.css = "css/style.css"
        self.page_head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
        <link href='http://fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Roboto:400,100' rel='stylesheet' type='text/css'>
    </head>
    <body>"""
        self.page_body = """
        <h1>Want to learn more about us&#63;<h1>
        <p>Sign up today and find out how we help businesses and individuals make their dream websites a reality<p>
        <form method="GET">
            <div>
                <ul>
                    <li>
                        <label>First Name* </label><br>
                        <input type="text" name="firstname" />
                    </li>
                    <li>
                        <label>Last Name* </label><br>
                        <input type="text" name="lastname" />
                    </li>
                    <li>
                        <label>Email* </label><br>
                        <input type="text" name="email" />
                    </li>
                    <li>
                        <label>Website URL </label><br>
                        <input type="text" name="weburl" />
                    </li>
                    <li>
                        <label>How Can We Help&#63;</label><br>
                        <textarea rows="15" cols="65" name="message" ></textarea>
                    </li>
                    <li id="checkbox">
                        <input type="checkbox" name="alertsbox" value="albox"><label>Sign me up for email alerts</label>
                    </li>
                    <li>
                        <input id="send" type="submit" value="Send" />
                    </li>
                </ul>
            </div>"""
        self.page_close = """
        </form>
    </body>
    <footer>
        <div>
            <ul>
                <li>
                    <h3>Call Us</h3>
                    <p>1.888.555.5555</p>
                </li>
                <li>
                    <h3>Email Us</h3>
                    <p>mail@website.com</p>
                </li>
            </ul>
        </div>
    </footer>
</html
"""

    def header(self):
        return self.page_head

    def body(self):
        return self.page_body

    def footer(self):
        return self.page_close