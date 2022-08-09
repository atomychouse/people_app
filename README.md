This Flask application contatins the basic contact management functionality
to add and filter items.

Instalation instructions
**************************************

1 git clone 
#Clone the repository
2 pip install -r requirements.txt
#install all requirements
3 sqlite3 api.db
3.1  .databases
#create database with sqlitecommands
4 python models.py
#Create database tables
5 flask run --host=0.0.0.0


For run tests
1 cd app_project
#project created in clone (step 1) of instalation
2 python -m pytest
#run python test command
