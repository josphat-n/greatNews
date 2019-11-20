from main import app
import urllib.request,json
from .models import NewsArticle, NewsSource

Article = NewsArticle.Article
Source = NewsSource.Source

#Get the api key
api_key=app.config['NEWS_API_KEY']

#Get the News base Url
base_url = app.config["NEWS_API_BASE_URL"]

def get_articles():
   """
   get sources using the json response
   """
   get_article_url = base_url.format(api_key)
   
   with urllib.request.urlopen(get_article_url) as url:
      get_articles_data = url.read()
      get_articles_resp = json.loads(get_articles_data)
      
      article_results = None  
      
      if get_articles_resp['sources']:
        article_results_list = get_articles_resp['sources']
        article_results= process_articles(article_results_list)
        
   return article_results

def process_articles(article_list):
   """
   Transform the article results into a list of objects.
   """
   article_results = []
   for article_item in article_list:
      # source = article_item.get('source')
      # title =  article_item.get('title')
      # description =  article_item.get('description')
      # url =  article_item.get('url') 
      # urlToImage =  article_item.get('urlToImage') 
      # publishedAt =  article_item.get('publishedAt')
      
      # article_object = Article(source,title,description,url,urlToImage,publishedAt)
      
      id = article_item.get('id')
      name = article_item.get('name')
      description = article_item.get('description')
      url = article_item.get('url')
      category = article_item.get('category')
      country = article_item.get('country')
      
      article_object = Source(id,name, description,url,category,country)
      article_results.append(article_object)     
   
   return article_results     