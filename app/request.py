from email.mime import base
import json
from turtle import title
from unicodedata import name

import urllib3

from app import app
from urllib3.request import json
from .models import news,articles

#getting api key
api_key = app.config['NEWS_API_KEY']

#getting the base url
base_url = app.config['SOURCE_API_BASE_URL']
base_url = app.config['ARTICLES_API_BASE_URL']

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

        sources_object = news.Sources(id,name,description,url,language,country)
        sources_results.append(sources_object)


    return sources_results


def get_articles(category):
    '''
    function that gets the json response to our Url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib3.request.urlopen(get_articles_url)as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['results']:
            articles_results_list = get_articles_response['results']
            articles_results = process_results(articles_results_list)

            return articles_results



def process_results(articles_list):
    '''
    function that process the articles results and transform them to a list of objects 
    '''

    articles_results = []
    for article_item in articles_list:
        id = article_item('id')
        title = article_item('title')
        author = article_item('author')
        description = article_item('description')
        url = article_item('url')

