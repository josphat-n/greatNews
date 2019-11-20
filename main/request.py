from main import app
import urllib.request,json
from .models import NewsArticle, NewsSource

Article = NewsArticle.Article
Source = NewsSource.Source

#Get the api key
api_key=app.config['NEWS_API_KEY']

#Get the News base Url
source_url = app.config["SOURCE_URL"]
articles_url= app.config['ARTICLES_URL']

def get_sources():
   """
   get sources using the json response
   """
   news_source_url=source_url.format(api_key)

   with urllib.request.urlopen(news_source_url) as url:

      source_data = url.read()
      source_response = json.loads(source_data)
      source_results= None

      if source_response['sources']:
         source_results_list = source_response['sources']
         source_results = process_results(source_results_list)

   return source_results 

def process_results(source_list):
   """
   Transform the article results into a list of objects.
   """
   source_results=[]

   for news_item in source_list:
      id=news_item.get('id')
      name=news_item.get('name')
      description=news_item.get('description')
      url=news_item.get('url')
      category=news_item.get('category')
      country=news_item.get('country')
                  
      source_object = Source(id,name,description,url,category,country)
      source_results.append(source_object)

   return source_results   

def get_articles(id):
   """
   get articles using the json response
   """
   get_article_url = articles_url.format(id,api_key)
   
   with urllib.request.urlopen(get_article_url) as url:
      get_articles_data = url.read()
      get_articles_resp = json.loads(get_articles_data)
      
      article_results = None  
      
      if get_articles_resp['articles']:
        article_results_list = get_articles_resp['articles']
        article_results= process_articles(article_results_list)
        
   return article_results

def process_articles(article_list):
   """
   Transform the article results into a list of objects.
   """
   article_results = []
   for article_item in article_list:
      source = article_item.get('source')
      title =  article_item.get('title')
      description =  article_item.get('description')
      url =  article_item.get('url') 
      urlToImage =  article_item.get('urlToImage') 
      publishedAt =  article_item.get('publishedAt')
      
      new_article = Article(source,title,description,url,urlToImage,publishedAt)
      article_results.append(new_article)
      
   return article_results     