import unittest
# from models import NewsArticle
from models import Article
# Article = NewsArticle.Article

class ArticleTest(unittest.TestCase):
   """
   Test the behaviour of News class
   """

   def setUp(self):
      """
      Set up method that will run before every Test
      """
      self.new_article = Article("abc-news","ABC_News","Your trusted source for breaking news", "Your trusted source for breaking news","https://abcnews.go.com", "general","us")

   def test_instance(self):
      self.assertTrue(isinstance(self.new_article,Article))
        
   def test_save_source(self):
      self.new_article.save_source()  # saving the new source
      self.assertEqual(len(Article.source_results),1)  
