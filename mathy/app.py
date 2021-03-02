from flask import Flask
from flask import request
import pandas, json


app = Flask(__name__)


@app.route('/math/average', methods=['GET'])
def average():
    data_block = request.get_json()
    print(data_block)

    data_frame = pandas.DataFrame.from_dict(data_block, orient='columns')

    data_frame['MA-5'] = data_frame.rolling(window=10)['Close'].mean()

    math_block = data_frame['MA-5'].to_json(orient='columns')
    math_block = json.loads(math_block)
    math_block = json.dumps({'MA-5': math_block})

    print(math_block)
    return math_block


if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')