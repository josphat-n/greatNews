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
      