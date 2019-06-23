import requests
from utils import *
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', kills='none')

@app.route('/test')
def test():
    print('hellloooooo')
    return render_template('index.html', kills='200000000')
@app.route('/transcribe')
def transcribe():
    text = get_text()
    return render_template('index.html', kills=text)

@app.route('/immerse_token', methods=['POST'])
def immerse_token():
    response = get_immersive_reader_token()
    return response

if __name__ == "__main__":
    app.run(debug = True)
