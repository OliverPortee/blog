
from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('home.html', title="Home", active="home")
 
@app.route('/blog')
def blog():
    return render_template('blog-post.html', title="hi", active="blog", text="<b>text</b>text")

@app.route('/contact')
def contact():
    return render_template('about.html', title="Contact", active="contact")

