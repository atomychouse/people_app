from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)


app.config['SECRET_KEY'] = '0c483b7de838a087dac0263a96dc3b7b'
'''
Configuring database access and permissions
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/alberto.rios/globant-mossions/flask-projects/cora-app/api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


'''
Structutre data to store a list of Contacts 
-------Attributes------------------
- id is a autoincrement primary key
- name : String with 250 length
- last_name : String with 255 length
- email_account : String with 255 length, *** we need this field unique
### collation=NOCASE its to define a none sensitive cases to avoid duplicatns

'''
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250, collation='NOCASE'))
    last_name = db.Column(db.String(200, collation='NOCASE'))
    email_account = db.Column(db.String(255, collation='NOCASE'), unique=True)

"""
Interface to interact with Model People
----------------------------------------
"""
class PeopleInterface:
    """Constructor with the asignation all atributes of the Objects People"""
    def __init__(self, **kwargs):
        pass
    """Validating i the email accunt has the right structure"""
    def is_email(self, email_account):
        pass
    """Verifing that email account exists"""
    def email_exists(self, email_account):
        pass
    """Perform a insertion in the database"""
    def add_people(self):
        pass
    """Remove a specifict People item idetified by ID"""
    def rm_people(self, id=None):
        pass
    def update_people(self):
        pass

"""Inplementation of the People Interface """
class PeopleInteract(People, PeopleInterface):
    """Construct people params with all atributes """
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.last_name = kwargs.get('last_name')
        self.email_account = kwargs.get('email_account')
    """Implementation of the email verification to ensure that the email corresponds only one people item """
    def email_exists(self):
        existe = self.query.filter_by(email_account=self.email_account).scalar()
        return existe
    """ Implementation of the insertion of the people item"""
    def add_people(self):
        db.session.add(self)
        #asign attributes of the class to the model
        db.session.commit()
        #Commit changes
        return True

db.create_all()