from flask import Flask
from flask import jsonify
from bs4 import BeautifulSoup
from urllib.request import urlopen


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! I am Xinya from IMT542'

@app.route('/cse312/24sp')
def cse312in24sp():
    # Example URL of UW CS course website
    url = "https://courses.cs.washington.edu/courses/cse312/24sp/"

    # Send a GET request to the URL
    page = urlopen(url)
    html = page.read().decode("utf-8")

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup.get_text(html, "html.parser")

    # Extract relevant information from the webpage
    # Example: get all links from the webpage
    links = [link['href'] for link in soup.find_all('a')]

    return jsonify({'links': links}) 