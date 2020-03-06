from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "casting"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
#   db_test_data()

'''
db_test_data()
    sample data for testing
'''
# def db_test_data():
    
'''
Actor
'''
class Actor(db.Model):  
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    age

    def __init__(self, name, catchphrase=""):
        self.name = name
        self.catchphrase = catchphrase

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'catchphrase': self.catchphrase}