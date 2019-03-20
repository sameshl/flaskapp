from flask import Flask,render_template,url_for
app=Flask(__name__)


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
def hello():
    return render_template('home.html',posts=all_posts,title='Home')

@app.route("/about")
def about():
    return render_template('about.html',title='About Us')




if __name__=='__main__':
    app.run(debug=True)
