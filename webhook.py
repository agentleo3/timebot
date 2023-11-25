from flask import Flask, request, jsonify, make_response
import requests
import random

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(jsonify(get_result()))


def get_result():
    # извлечение параметра
    req = request.get_json(force=True)
    print(req)


app.run(host='0.0.0.0', port=81)


