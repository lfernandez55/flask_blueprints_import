from flask import Flask, request, render_template, Blueprint

api = Blueprint('api', 'api', url_prefix='/')

@api.route('/')
def home_page():
    return render_template('index.html')
