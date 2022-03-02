from ensurepip import bootstrap

from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap

bootstrap =Bootstrap()
#initializing application

app = Flask(__name__,instance_relative_config = True) 
from app.main import routes


#setting up configurations
app.config.from_object([DevConfig])
app.config.from_pyfile("config.py")

#initializing flask extension
bootstrap.init_app(app)

from app.main import error

