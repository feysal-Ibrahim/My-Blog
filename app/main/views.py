from flask import render_template, url_for, flash, redirect, request, abort
from . import main
from flask_login import login_required, current_user
from .. import db



@main.route('/')
def index():
    '''
   view function that defines the routes decorater for the index
    '''



    title = 'Home - Welcome to The best Movie Review Website Online'

    return render_template ( 'index.html' , title=title)