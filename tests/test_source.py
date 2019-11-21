import unittest
# from .models import NewsSource
from models import Source
# Source = NewsSource.Source

class NewsTest(unittest.TestCase):
    """
    Test the behaviour of News class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_source = Source("abc-news","ABC_News","Your trusted source for breaking news","https://abcnews.go.com", "general","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
        
    def test_save_source(self):
        self.new_source.save_source()  # saving the new source
        self.assertEqual(len(Source.source_results),1)  