from main import app
import urllib.request,json

#Get the api key
api_key = app.config['News_API_KEY']

#Get the News base Url
base_url = app.config["News_API_BASE_URL"]