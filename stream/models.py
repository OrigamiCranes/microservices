from stream.app import db


class EURUSD(db.Model):
    __tablename__ = 'EURUSD'
    id = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date, nullable=False)
    Time = db.Column(db.Time, nullable=False)
    Open = db.Column(db.Numeric(precision=7, scale=5), nullable=False)
    High = db.Column(db.Numeric(precision=7, scale=5), nullable=False)
    Low = db.Column(db.Numeric(precision=7, scale=5 ), nullable=False)
    Close = db.Column(db.Numeric(precision=7, scale=5), nullable=False)
    Volume = db.Column(db.Integer, nullable=False)