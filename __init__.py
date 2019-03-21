from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app=Flask(__name__)
'''
Generate hidden secert key with the help of pythons inbuilt secrets module.
We are generating a random 16 bits key.

import secerts
secrets.token_hex(16)
'''
app.config['SECRET_KEY']='be2c117bdf7dfe089101bb27f4b99825'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)


from flaskblog import routes
