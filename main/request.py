from main import app
import urllib.request,json
from .models import Article

Article = NewsArticle.Article

#Get the api key
api_key = app.config['News_API_KEY']

#Get the News base Url
base_url = app.config["News_API_BASE_URL"]

def get_articles:
   """
   get articles using the json response
   """
   get_articles_url = base_url.format(api_key)
   
   with urllib.request.urlopen(get_articles_url) as url:
      get_articles_data = url.read()
      get_articles_resp = json.loads(get_articles_data)
      
      article_results = None  
      
     if get_articles_resp['articles']:
        article_results_list = get_articles_resp['articles']
        article_results= process_articles(article_results_list)
        
   return article_results
        