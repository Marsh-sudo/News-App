
from flask import render_template
from app import app

#views
app.route('/')
def index():
    '''
    view root page that returns index page
    '''
    title = 'Home - Welcome to The best Online News Website'
    return render_template('index.html', title = title)

app.route('/Articles/<int:news_id>')
def sourceArticle(id):
    '''
    view news page function that returns the news details page and its data
    '''
    return render_template('sources.html')