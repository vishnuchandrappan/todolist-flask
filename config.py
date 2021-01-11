# config.py
class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments



class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}


'''
TESTING: setting this to True activates the testing mode of Flask extensions. This allows us to use testing properties that could for instance have an increased runtime cost, such as unittest helpers. It should be set to True in the configurations for testing. It defaults to False.
DEBUG: setting this to True activates the debug mode on the app. This allows us to use the Flask debugger in case of an unhandled exception, and also automatically reloads the application when it is updated. It should however always be set to False in production. It defaults to False.
SQLALCHEMY_ECHO: setting this to True helps us with debugging by allowing SQLAlchemy to log errors.
'''