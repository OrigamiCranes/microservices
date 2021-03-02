from flask import Flask
import json
import requests
import pandas

app = Flask(__name__)

block_size = 200


@app.route('/api', methods=['GET'])
def basic():

    settings = {'block_size': block_size}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    settings = json.dumps(settings)

    data_block = requests.get("http://stream:5000/stream/EURUSD", json=settings, headers=headers)
    math_block = requests.get("http://mathy:5001/math/average", json=data_block.json())

    jsonMerged = {**data_block.json(), **math_block.json()}
    merged_block = json.dumps(jsonMerged)

    return merged_block


if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')