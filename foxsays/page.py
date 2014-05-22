class Page():
    def __init__(self):
        self.__header = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Wisconsin Zoological Society</title>
        <link rel="stylesheet" href="css/style.css">
        <link href='http://fonts.googleapis.com/css?family=Griffy' rel='stylesheet' type='text/css'>
    </head>
    <header>
        <h1>Wisconsin Zoological Society</h1>
        <h1 id='h1bg'>Wisconsin Zoological Society</h1>
        <div>
            <input placeholder="Search for an Animal"></input
        </div>
    </header>
    <body>'''

        self.__form = '''
        <div>
            <p class='cta'>Search for an animal to find out more about it&excl;</p>
            <p class='cta'>Here's some info to help get you started&excl;</p>
        </div>
        <form method="GET" action="" name="animals">
            <a href="/?animal=1">Dog</a>
            <a href="/?animal=2">Horse</a>
            <a href="/?animal=3">Raccoon</a>
        </form>'''