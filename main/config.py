class Config:
   
   #This is the url for all named sources available in the News API website
   SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
   
   #URL for fetching the news articles.
   ARTICLES_URL='https://newsapi.org/v2/everything?sources={}&apikey={}'
   
   
class ProdConfig(Config):
   pass

class DevConfig(Config):
   DEBUG = True