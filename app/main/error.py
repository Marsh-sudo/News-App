from flask import render_template

import app
from . import main
# from app import app


@app.errorhandler(404)
def four_Ow_four(error):
    '''
    function that renders the 404 page
    '''
    return render_template('fourOwfour.html'),404