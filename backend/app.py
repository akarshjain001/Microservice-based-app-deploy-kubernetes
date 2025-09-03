from flask import Flask, render_template, jsonify
import os
from connection import collection


app = Flask(__name__)

PORT=os.environ.get('PORT', 8000)

@app.route('/')
def index():
    return jsonify({  'message': 'Backend is running!'})

@app.route('/api/get')
def api():
    names = collection.find()   
    result = []
    for name in names:
        result.append(name['value'])
    
    result = {
        'data': result
    }
    return jsonify(result)


@app.route('/api/add/<name>')
def add(name):
    collection.insert_one({'value': name})
    return jsonify({'message': f'{name} added to the database!'})


if __name__ == '__main__':
    app.run(debug=True, port=PORT, host='0.0.0.0')

