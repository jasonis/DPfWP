
# Jason Slocum
# 5.9.2014
# DPW
# Simple Form
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" ?>
    </head>
    <body>"""
        page_body = """

        page_close = """

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
