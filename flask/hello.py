from flask import Flask

from flask import render_template

app = Flask(__name__)

@app.route("/user/<username>")
def show_user_profile(username):
    return "User %s" % username

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "post %d" % post_id

@app.route("/projects/")
def projects():
    return "The project page"

@app.route("/about")
def about():
    return "The about page"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html",name=name)

if __name__ == "__main__":
    app.run()
