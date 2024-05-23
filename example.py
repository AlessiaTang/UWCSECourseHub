from flask import Flask
import json

app = Flask(__name__)

def read_json_file(filename):
    with open(filename) as file:
        data = json.load(file)
    return data

my_dict = read_json_file("sbir-search-results.json")

@app.route('/sbir/state/<state>')
def sbir_state(state):
    for i in my_dict:
       if i['State']==state:
          return i['Award_Title'] 
    return 'none'

@app.route('/sbir/year/<year>')
def sbir_year(year):
    companies_for_year = []
    for i in my_dict:
        if i['Award_Year'] == year:
            companies_for_year.append(i['Company'])
    if companies_for_year:
        return ', '.join(companies_for_year)
    else:
        return 'none'
    


@app.route('/')
def info():
    message=f"""
       Hello, I am your API.
       You can call my functions
       hello or hello(xinya)
    """ 
    return message 

@app.route('/hello/name/<username>')
def hello(username):
    return 'hello %s' % username 

 
