from flask import render_template
from main import app

#This defines the various views in our app
@app.route('/')
def index():
   """
   function to return the index page and its resources
   """
   
   return render_template('index.html')