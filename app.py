from flask import render_template, Flask, request, redirect, url_for
import json

app = Flask(__name__)


def load_posts():
    """Loads all blog posts from the JSON file and returns them as a list."""
    try:
        with open('blog_posts.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_posts(posts):
    """Saves the given list of blog posts to the JSON file."""
    with open('blog_posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)


@app.route('/')
def index():
    """Displays the main page with all blog posts."""
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Handles the creation of new blog posts via a form (GET shows form, POST saves post)."""
    if request.method == 'POST':
        # Daten aus dem Formular holen
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')

        # Alle Posts laden
        blog_posts = load_posts()

        # Neue ID generieren (höchste ID + 1)
        new_id = max([post['id'] for post in blog_posts], default=0) + 1

        # Neuen Post erstellen
        new_post = {
            'id': new_id,
            'title': title,
            'content': content,
            'author': author,
            'date': '2024-01-15'
        }

        # Post zur Liste hinzufügen
        blog_posts.append(new_post)

        # Speichern
        save_posts(blog_posts)

        # Zurück zur Hauptseite
        return redirect(url_for('index'))

    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)