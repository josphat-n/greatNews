from flask import render_template
from . import main
from ..request import get_articles, get_sources


@main.route('/')
def index():
    """
   function to return the index page and its resources
   """
    # Displaying the news Sources
    display_sources = get_sources()

    return render_template('index.html', sourcess=display_sources)


@main.route('/articles/<id>')
def source(id):
    display_articles = get_articles(id)
    print(display_articles)

    return render_template('articles.html', id=id, articles=display_articles)
