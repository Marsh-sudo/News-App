import json
from app import app
from urllib.request import json
from .models import news

#getting api key
api_key = app.config['NEWS_API_KEY']