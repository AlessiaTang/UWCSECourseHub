from flask import Flask
from flask import jsonify
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! I am Xinya from IMT542'

@app.route('/cse312/24sp')
def cse312in24sp():
    session = HTMLSession()

    url = 'https://courses.cs.washington.edu/courses/cse312/24sp/'

    response = session.get(url)

    response.html.render()

# Find the navbar element
    navbar = response.html.find('.nav navbar-nav', first=True)

# Extract links from the navbar
    links = navbar.find('a')
    return jsonify({'links': list(links)})



    # Send a GET request to the URL
    #page = urlopen(url)
    #html = page.read().decode("utf-8")

    # Parse the HTML content using BeautifulSoup
    #soup = BeautifulSoup(html, "html.parser")

    # Extract relevant information from the webpage
    # Example: get all links from the webpage
