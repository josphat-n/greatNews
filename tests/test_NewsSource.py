import unittest
from models import NewsSource
Source = NewsSource.Source

class NewsTest(unittest.TestCase):
    """
    Test the behaviour of News class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_source = Source("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com", "general","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_souce,Source))


if __name__ == '__main__':
    unittest.main()