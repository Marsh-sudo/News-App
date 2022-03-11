from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap




app = Flask(__name__,instance_relative_config=True)

app.config.from_object(DevConfig)

bootstrap = Bootstrap(app)


    # initializing bootstrap
bootstrap.init_app(app)

    # registering a blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
    
    # setting config
from .request import configure_request
configure_request(app)
    # will add the routes
   


