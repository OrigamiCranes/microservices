import json
import requests
from . import app
import pandas

block_size = 100


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
