from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
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

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    posts=db.relationship('Post',backref='author',lazy=True)#'Post but not post because we are referencing the Class here which is Post and not the table post'


    def __repr__(self):
        return f"User({self.username},'{self.email}','{self.image_file}')"

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)#'user.id and not User.id because we are referencing the table name here witch by default will be lowercase of User class -> user'


    def __repr__(self):
        return f"Post({self.title},'{self.date_posted}')"










all_posts=[
    {
        'author':'Samesh',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'01/01/2019'
    },
    {
        'author':'IDK',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'02/01/2019'

    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=all_posts,title='Home')


@app.route("/about")
def about():
    return render_template('about.html',title='About Us')


@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
         flash(f'Account created for {form.username.data}!','success')
         return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)


@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful!','danger')
    return render_template('login.html',title='Login',form=form)













if __name__=='__main__':
    app.run(debug=True)
