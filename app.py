from flask import render_template, Flask
import json

app = Flask(__name__)

def load_posts():
    try:
        with open('blog_posts.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_posts(posts):
    with open('blog_posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)


@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)