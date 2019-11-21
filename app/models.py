class Source:
   """
   The blueprint for News-source objects.
   """      
   source_results = [] #An empty array of news sources
   
   def __init__(self, id, name, description, url, category, country):
      self.id = id
      self.name = name
      self.description = description
      self.url = url
      self.category = category
      self.country = country
      
   def save_source(self):
      Source.source_results.append(self)
      

class Article:
   """
   The blueprint for article objects.
   """
   article_results = [] #An array of all articles
   
   def __init__(self,source, title, description, content, url, urlToImage,publishedAt):
      self.source = source
      self.title = title
      self.description = description
      self.content = content
      self.url = url
      self.urlToImage = urlToImage
      self.publishedAt = publishedAt
      
   def save_article(self):
      Article.article_results.append(self)   