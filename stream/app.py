from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask import render_template, request
import random, json, pandas
from sqlalchemy import and_, func

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'example-key'

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://jack:notguest@35.211.129.255:3306/epics"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_TIME_LIMIT = 86400

    TESTING = False
    LOGIN_DISABLED = False
    WTF_CSRF_ENABLED = True


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)
db = SQLAlchemy(app)


class EURUSD(db.Model):
    __tablename__ = 'EURUSD'
    id = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date, nullable=False)
    Time = db.Column(db.Time, nullable=False)
    Open = db.Column(db.Numeric(precision=7, scale=5), nullable=False)
    High = db.Column(db.Numeric(precision=7, scale=5), nullable=False)
    Low = db.Column(db.Numeric(precision=7, scale=5), nullable=False)
    Close = db.Column(db.Numeric(precision=7, scale=5), nullable=False)
    Volume = db.Column(db.Integer, nullable=False)


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
    data_frame.loc[:, 'Date'] = pandas.to_datetime(
        data_frame.Date.astype(str) + ' ' + data_frame.Time.astype(str)).dt.tz_convert(None)
    data_frame.drop('Time', axis=1, inplace=True)
    data_frame.drop('id', axis=1, inplace=True)

    print(data_frame.dtypes)

    # export json
    data_block = data_frame.to_json(orient='columns')
    return data_block


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
