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

CSE417_24wi = read_json_file("CSE417_24wi_lecture.json")

CSE312_24sp = read_json_file("CSE312_24sp_lecture.json")
CSE332_24sp = read_json_file("CSE332_24sp_lecture.json")
CSE333_24sp = read_json_file("CSE333_24sp_lecture.json")
CSE401_24sp = read_json_file("CSE401_24sp_lecture.json")
CSE414_24sp = read_json_file("CSE414_24sp_lecture.json")

@app.route('/')
def info():
    message=f"""
       Hello, I am your UW CSE resource guide. <br>
       <br> Please input your interested course (for example, <em> /cse414/ </em>) to get the course introduction.<br>
       <br> Please input your interested course + course quarter (for example, <em> /cse414/24sp/ </em>) to get the course lecture materials of the whole quarter.<br>
       <br> You can even search for the materials related to a certain lecture topic! Just input interested course + course quarter + topic keyword (for example, <em> /CSE414/24sp/SQL </em>) to get the targeted materials.<br>
       <br> The supported courses and quarters include:<br>
       <br> CSE312 23sp 24sp<br>
       <br> CSE332 23sp 24sp<br>
       <br> CSE333 24sp<br>
       <br> CSE401 24sp<br>
       <br> CSE414 24sp<br>
       <br> CSE417 24wi<br>
       <br> <em> Continuing... </em>
       
    """ 
    return message 


@app.route('/cse312/')
def info_cse312():
    message=f"""
       CSE 312 Foundations of Computing II<br> 
       <br> Examines fundamentals of enumeration and discrete probability; applications of randomness to computing; polynomial-time versus NP; and NP-completeness. 
    """ 
    return message 

@app.route('/cse332/')
def info_cse332():
    message=f"""
       CSE 332 Data Structures And ParallelismII<br> 
       <br> Covers abstract data types and structures including dictionaries, balanced trees, hash tables, priority queues, and graphs; sorting; asymptotic analysis; fundamental graph algorithms including graph search, shortest path, and minimum spanning trees; multithreading and parallel algorithms; P and NP complexity classes.  
    """ 
    return message 

@app.route('/cse333/')
def info_cse333():
    message=f"""
       CSE 333 Systems Programming<br> 
       <br> Includes substantial programming experience in languages that expose machine characteristics and low-level data representation (e.g., C and C++); explicit memory management; modern libraries and language features; interacting with operating-system services; introduction to concurrent programming.   
    """ 
    return message 

@app.route('/cse401/')
def info_cse401():
    message=f"""
       CSE 401 Introduction To Compiler Construction<br> 
       <br> Fundamentals of compilers and interpreters; symbol tables; lexical analysis, syntax analysis, semantic analysis, code generation, and optimizations for general purpose programming languages.  
    """ 
    return message 

@app.route('/cse414/')
def info_cse414():
    message=f"""
       CSE 414 Introduction To Database Systems<br> 
       <br> Introduces database management systems and writing applications that use such systems; data models, query languages, transactions, database tuning, data warehousing, and parallelism. Intended for non-majors.  
    """ 
    return message 

@app.route('/cse417/')
def info_cse417():
    message=f"""
       CSE 417 Algorithms And Computational Complexity<br> 
       <br> Design and analysis of algorithms and data structures. Efficient algorithms for manipulating graphs and strings. Fast Fourier Transform. Models of computation, including Turing machines. Time and space complexity. NP-complete problems and undecidable problems.   
    """ 
    return message 



@app.route('/cse312/23sp/')
def get_cse312_23sp_all_resource():
    return jsonify(CSE312_23sp)

@app.route('/cse312/23sp/<keyword>')
def get_cse312_23sp_resource(keyword):
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


@app.route('/cse312/24sp/')
def get_cse312_24sp_all_resource():
    return jsonify(CSE312_24sp)

@app.route('/cse312/24sp/<keyword>')
def get_cse312_24sp_resource(keyword):
    matching_data = []
    for lecture in CSE312_24sp:
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



@app.route('/cse332/23sp/')
def get_cse332_23sp_all_resource():
    return jsonify(CSE332_23sp)

@app.route('/cse332/23sp/<keyword>')
def get_cse332_23sp_resource(keyword):
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


@app.route('/cse332/24sp/')
def get_cse332_24sp_all_resource():
    return jsonify(CSE332_24sp)

@app.route('/cse332/24sp/<keyword>')
def get_cse332_24sp_resource(keyword):
    matching_data = []
    for lecture in CSE332_24sp:
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


@app.route('/cse333/24sp/')
def get_cse333_24sp_all_resource():
    return jsonify(CSE333_24sp)

@app.route('/cse333/24sp/<keyword>')
def get_cse333_24sp_resource(keyword):
    matching_data = []
    for lecture in CSE333_24sp:
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


@app.route('/cse401/24sp/')
def get_cse401_24sp_all_resource():
    return jsonify(CSE401_24sp)

@app.route('/cse401/24sp/<keyword>')
def get_cse401_24sp_resource(keyword):
    matching_data = []
    for lecture in CSE401_24sp:
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



@app.route('/cse414/24sp/')
def get_cse414_24sp_all_resource():
    return jsonify(CSE414_24sp)

@app.route('/cse414/24sp/<keyword>')
def get_cse414_24sp_resource(keyword):
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



@app.route('/cse417/24wi/')
def get_cse417_24wi_all_resource():
    return jsonify(CSE417_24wi)

@app.route('/cse417/24wi/<keyword>')
def get_cse417_24wi_resource(keyword):
    matching_data = []
    for lecture in CSE417_24wi:
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



