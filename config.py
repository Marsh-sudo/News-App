# from distutils.command.config import config
import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q=Apple&from=2022-02-26&sortBy=popularity&apiKey=https://newsapi.org/v2/everything?q=apple&from=2022-02-25&to=2022-02-25&sortBy=popularity&apiKey=9762e5f31e314775bd934aa2b1ef72c1'
    SOURCES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey=9762e5f31e314775bd934aa2b1ef72c1'
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey=9762e5f31e314775bd934aa2b1ef72c1'
    


class ProdConfig(Config):
    '''
    production configuration child class.
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config:The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}