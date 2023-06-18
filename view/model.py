import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()
class Users(db.Model):
    __tablename__ = 'users'
    userkey = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    userid = db.Column(db.String)
    userpwd = db.Column(db.String)