from flask import Flask
import json

app = Flask(__name__)

def read_json_file(filename):
    with open(filename) as file:
        data = json.load(file)
    return data

my_dict = read_json_file("CSE312_23sp_lecture.json")

@app.route('/')
def info():
    message=f"""
       Hello, I am your CSE312 resource guide.
    """ 
    return message 

@app.route('/CSE312/23sp/')
def get_cse312_resource(content):
    for i in my_dict:
       if i['lecture description']==content:
          return i['links'] 
    return 'none'