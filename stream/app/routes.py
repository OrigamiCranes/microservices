from app import app, db
from .models import EURUSD
from flask import render_template, request
import random, json, pandas
from sqlalchemy import and_, func


@app.route('/stream/<epic>', methods=['GET'])
def stream(epic):
    settings = request.get_json()
    settings = json.loads(settings)

    # get db_table size to assure no out of range values
    # generate rng value of datasteam
    size = db.session.query(eval(epic)).count()
    stream_start = random.randrange(1, size - int(settings['block_size']))

    # get data_block between two values
    db_query = db.session.query(eval(epic)).filter(and_(EURUSD.id >= stream_start), (
                EURUSD.id <= (stream_start + int(settings['block_size']) - 1))).statement

    # convert date+time columns to DATETIME column
    data_frame = pandas.read_sql_query(db_query, db.session.bind, parse_dates={'Date': '%Y-%m-%d', 'Time': '%H:%M:%S'})
    data_frame.loc[:, 'Date'] = pandas.to_datetime(data_frame.Date.astype(str) + ' ' + data_frame.Time.astype(str)).dt.tz_convert(None)
    data_frame.drop('Time', axis=1, inplace=True)
    data_frame.drop('id', axis=1, inplace=True)

    print(data_frame.dtypes)

    # export json
    data_block = data_frame.to_json(orient='columns')
    return data_block
