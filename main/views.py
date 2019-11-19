from flask import render_template
from main import app

#This defines the various views in our app
@app.route('/')
def index():
   """
   function to return the index page and its resources
   """
    
   # Displaying the news Articles
   dispArticle = get_articles()
   print(dispArticle)
   
   return render_template('index.html', articles = dispArticle)