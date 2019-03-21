from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

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
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login' #function name of route to be taken
login_manager.login_message_category='info'



from flaskblog import routes
