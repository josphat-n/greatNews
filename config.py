import os


class Config:
    # This is the url for all named sources available in the News API website
    SOURCE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey={}'
    # URL for fetching the news articles.
    ARTICLES_URL = 'https://newsapi.org/v2/everything?sources={}&apikey={}'

    from secret_configs import NEWS_API_KEY


class ProdConfig(Config):
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    # pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
