from flask import Flask,jsonify

app = Flask(_name_)
@app.route('/Hello', methods = ['GET'])
def welcome():
    return jsonify({'msg': 'Hello World'})
app.run(debug = True)  