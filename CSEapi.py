from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

def read_json_file(filename):
    with open(filename) as file:
        data = json.load(file)
    return data

CSE312_23sp = read_json_file("CSE312_23sp_lecture.json")
CSE332_23sp = read_json_file("CSE332_23sp_lecture.json")
CSE414_24sp = read_json_file("CSE414_24sp_lecture.json")

@app.route('/')
def info():
    message=f"""
       Hello, I am your UW CSE resource guide.
    """ 
    return message 

@app.route('/CSE312/23sp/')
def get_cse312_all_resource():
    return jsonify(CSE312_23sp)

@app.route('/CSE312/23sp/<keyword>')
def get_cse312_resource(keyword):
    matching_data = []
    for lecture in CSE312_23sp:
        description = lecture.get('lecture description')  # Get the value associated with 'lecture description' key
        if description and keyword.lower() in description.lower():
            matching_data.append({
                'lecture description': description,
                'links': lecture['links']
            })

    if matching_data:
        return json.dumps(matching_data)
    else:
        return 'No matching lecture descriptions found for the keyword: {}'.format(keyword)


@app.route('/CSE332/23sp/')
def get_cse332_all_resource():
    return jsonify(CSE332_23sp)

@app.route('/CSE332/23sp/<keyword>')
def get_cse332_resource(keyword):
    matching_data = []
    for lecture in CSE332_23sp:
        description = lecture.get('lecture description')  # Get the value associated with 'lecture description' key
        if description and keyword.lower() in description.lower():
            matching_data.append({
                'lecture description': description,
                'links': lecture['links']
            })

    if matching_data:
        return json.dumps(matching_data)
    else:
        return 'No matching lecture descriptions found for the keyword: {}'.format(keyword)



@app.route('/CSE414/24sp/')
def get_cse414_all_resource():
    return jsonify(CSE414_24sp)

@app.route('/CSE414/24sp/<keyword>')
def get_cse414_resource(keyword):
    matching_data = []
    for lecture in CSE414_24sp:
        description = lecture.get('lecture description')  # Get the value associated with 'lecture description' key
        if description and keyword.lower() in description.lower():
            matching_data.append({
                'lecture description': description,
                'links': lecture['links']
            })

    if matching_data:
        return json.dumps(matching_data)
    else:
        return 'No matching lecture descriptions found for the keyword: {}'.format(keyword)



