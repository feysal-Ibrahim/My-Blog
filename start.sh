#!/usr/bin/env bash

export SECRET_KEY='123'


export MAIL_USERNAME='addictivefazman@gmail.com'
export MAIL_PASSWORD='fazmandinho1'


 heroku run python3.6 manage.py db upgrade