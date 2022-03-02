from ensurepip import bootstrap

from flask import Flask
from config import config_options 
# from config import DevConfig
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    #initializing bootstrap
    bootstrap.init_app(app)

    #registering a blueprint
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #setting config
    from .request import configure_request
    configure_request(app)
    # will add the routes

    return app


