from distutils.debug import DEBUG


class Config:
    '''
    General configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    production configuration child class
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config:The parent configuration class with General configuration settings
    '''

    DEBUG = True