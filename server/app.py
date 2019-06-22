import requests
from utils import *
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/index')
"""
This route is to render the homepage
"""
def index():
    return render_template('index.html')


@app.route('/transcribe')
"""
This endpoint will activate the microphone, transcibe what is being said and return the text
"""
def transcribe():
    text = get_text()
    return text

@app.route('/immerse__token')
"""
This will set up the token for the immersive reader veiw
"""
def immerse_token():
    response = get_immersive_reader_token()
    return response















