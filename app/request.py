import json
from unicodedata import name

import urllib3
from app import app
from urllib.request import json
from .models import news

#getting api key
api_key = app.config['NEWS_API_KEY']

#getting the base url
base_url = app.config['SOURCE_API_BASE_URL']

def get_sources(category):
    '''
    function that gets json response to our url requests
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib3.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    '''
    function that processes the sources result and transform them to a list of objects

    Args:
       sources_list:A list of dictionaries that contain sources list

       Returns:
          sources_results:A list of sources objects
    '''

    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        language = source_item.get('language')
        country = source_item.get('country')

        if 