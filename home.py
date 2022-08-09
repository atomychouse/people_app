from crypt import methods
from flask import (Flask, request)
import config
import settings
import json
from flask_cors import CORS, cross_origin
from models import PeopleInteract, People
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import smtplib


app = Flask(__name__)
app.config['SECRET_KEY'] = '0c483b7de838a087dac0263a96dc3b7b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/alberto.rios/globant-mossions/flask-projects/cora-app/api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)


@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    if request.method == 'POST':
        username = settings.users.get(request.form['username'] ,None)
        if not username:
            return {'login':'user no valid'}
        if username.Password == request.form['password']:
            return {'login':True}
        
        return {'login':'password invalid'}


@app.route('/addpeople', methods=['PUT'])
@cross_origin()
def addpeople()->dict:
    if request.method == 'PUT':
        kwargs = {
            'name':request.form['name'],
            'last_name':request.form['last_name'],
            'email_account':request.form['email']
        }
        new_people = PeopleInteract(**kwargs)
        x = new_people.email_exists()
        if x:
            print('ya existe')
            return {'error':'Email account exists please try with other'}
        print(new_people.add_people(),'plex')
        return {'saved':True}




@app.route('/people', methods=['GET'])
@cross_origin()
def people() -> dict:
    filtro = {}
    args = request.args
    attribute = args.get('filter_attr', None)
    columns = ['name','last_name','email_account']
    if attribute and attribute in columns:
        filtro[attribute] = args.get('filter_val',None)
    else:
        return {'err':'filter attributes are not valid'}
    people = People.query.filter_by(**filtro)
    peoples = [
        {
            'id':p.id,
            'name':p.name,
            'last_name':p.last_name,
            'email_account':p.email_account
        }
         for p in people]
    return {'people':peoples}

@app.route('/send_email', methods=['POST'])
@cross_origin()
def send_email() -> dict:
    accounts = request.form.getlist('accounts')
    if len(accounts)>0:
        messenger = smtplib.SMTP('localhost')
        messenger.sendmail('cruzarios@gmail.com',accounts, ' Hello guys, this is a friendly message')
        return {'sent':True}
    else:
        return {'sent':False}
