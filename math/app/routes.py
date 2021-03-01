from pandas.io.json import json_normalize

from app import app
from flask import render_template, request
import pandas, json


@app.route('/math/average', methods=['GET'])
def average():
    data_block = request.get_json()

    data_frame = pandas.DataFrame.from_dict(data_block, orient='columns')

    data_frame['MA-5'] = data_frame.rolling(window=5)['Close'].mean()

    math_block = data_frame['MA-5'].to_json(orient='columns')
    math_block = json.loads(math_block)
    math_block = json.dumps({'MA-5': math_block})

    return math_block




