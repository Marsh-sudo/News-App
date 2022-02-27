
from flask import render_template
from app import app
from .request import get_sources

#views
app.route('/')
def index():
    '''
    view root page that returns index page
    '''
    universal_news = get_sources('universal')
    sport_news = get_sources('sports')
    business_news = get_sources('business')
    title = 'Home - Welcome to The best Online News Website'
    return render_template('index.html', title = title, universal = universal_news,sports = sport_news,business = business_news)

app.route('/Articles/<int:news_id>')
def sourceArticle(id):
    '''
    view news page function that returns the news details page and its data
    '''
    return render_template('sources.html')

