import requests
from utils import *
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/transcribe')
def transcribe():
    text = get_text()
    return text

@app.route('/immerse_token')
def immerse_token():
    response = get_immersive_reader_token()
    return response

if __name__ == "__main__":
    app.run(debug = True)














