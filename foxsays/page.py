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

        self.__template = '''
        <div id="animal_area">
            <h2>{obj.name}</h2>
            <div id="animal_info">
                <h2>Phylum:</h2>
                <p>{obj.phy}</p>
                <h2>Class:</h2>
                <p>{obj._class}</p>
                <h2>Order:</h2>
                <p>{obj.order}</p>
                <h2>Family:</h2>
                <p>{obj._fam}</p>
                <h2>Genus:</h2>
                <p>{obj._gen}</p>
                <h2>Average Lifespan:</h2>
                <p>{obj.avg_life}</p>
                <h2>Habitat:</h2>
                <p>{obj.hab}</p>
                <h2>Geolocation:</h2>
                <p>{obj.geo}</p>
            </div>
            <div id="animal_pic">
                <img src="{obj.url}" width=500 />
            </div>
        </div>'''

        self.__footer = '''
    </body>
</html>'''