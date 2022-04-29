from unittest import result
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods = ['POST'])
def add():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    result = x + y
    
    return jsonify({"Total": result}) 

if __name__ == '__main__':
    app.run(debug=True)