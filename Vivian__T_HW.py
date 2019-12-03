#import flask, urllib.request, json, andssl
#import if needed
#Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy
from flask import Flask, render_template
import urllib.request
#JSON (JavaScript Object Notation)
#you need to import JSON
import json

#Make sure to import ssl
#Transport Layer Security
import ssl


#ssl
this_context = ssl.SSLContext()

#expose url with demo key by request and open with context and equal to some object
#call service
the_link_info = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY', context=this_context)

#have the object read and stored into the string
reader = the_link_info.read()

#have the string setup and decode json into python data structure
finished = json.loads(reader.decode('utf-8'))

#Flask object, helps determine the root path
app = Flask(__name__)

#creating a reference for the image
image = finished['hdurl']

#@app- directory route
# Route - mapping (connecting) a URL to Python function
@app.route("/")
def index():
    return render_template('main_page.html', picture=image)+ finished['date']

# Runs app only when we run this script directly, not if we import this somewhere else
if __name__ == '__main__':
    app.run(debug=True)
