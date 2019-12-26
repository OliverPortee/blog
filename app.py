from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path="/static")


def website(title=None, content=None, active=None):
    return render_template("website_template.html", title=title, content=content, active=active)


@app.route('/')
def home():
    return website(title="Home@lvrsblc", content="<h1>Home</h1>", active="home")

@app.route('/blog')
def blog():
    return website(title="Blog@lvrsblc", content="<h1>Blog</h1>", active="blog")

@app.route('/contact')
def contact():
    return website(title="Contact@lvrsblc", content="<h1>Contact</h1>", active="contact")

if __name__ == '__main__':
    app.debug = True
    app.run()
