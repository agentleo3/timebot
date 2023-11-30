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


def get_time(latitude, longitude):
    url = f'https://timeapi.io/api/Time/current/coordinate?latitude={latitude}&longitude={longitude}'
    response = requests.get(url).json()
    time = response["time"]
    date = response["date"]
    return f"{time}, {date}"


def get_result():
    # извлечение параметра
    req = request.get_json(force=True)
    print(req)
    current_time = get_time(38.9, -77.03)
    print(current_time)
    return {
        "fulfillmentText": current_time
    }



app.run(host='0.0.0.0', port=81)



