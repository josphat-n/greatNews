class Article:
   """
   The blueprint for article objects.
   """
   
   def __init__(self,source, title, description, url, urlToImage,publishedAt):
      self.source = source
      self.title = title
      self.description = description
      self.url = url
      self.urlToImage = urlToImage
      self.publishedAt = publishedAt