from flask import Flask
from flask import render_template

app = Flask(__name__)

post = [1,1,1]


@app.route('/')
def index():
    return render_template("index.html", num_posts=len(post))

@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template('post_view.html', slug_title=slug)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>")
def post_form(post_id=None):
    return render_template('admin/post_form.html', post_id=post_id)


