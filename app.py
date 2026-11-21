
from flask import Flask, render_template, abort

app = Flask(__name__)

posts = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "content": "Python is a simple and powerful programming language. It is used in web development, data science and AI."
    },
    {
        "id": 2,
        "title": "What is Flask?",
        "content": "Flask is a lightweight Python web framework used to create web applications."
    },
    {
        "id": 3,
        "title": "Learning HTML and CSS",
        "content": "HTML creates the structure of a website and CSS makes it beautiful and responsive."
    }
]

@app.route("/")
def home():
    return render_template("posts.html", posts=posts)

@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)

    if post is None:
        abort(404)

    return render_template("post_detail.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
