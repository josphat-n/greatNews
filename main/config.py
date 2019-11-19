class Config:
   pass
   News_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&from=2019-10-19&sortBy=publishedAt&apiKey={}'

class ProdConfig(Config)
   pass

class DevConfig(Config)
   DEBUG = True