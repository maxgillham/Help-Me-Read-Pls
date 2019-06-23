import requests
from utils import *
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('Record') == 'Record':
            text = get_text()
            print(text)
            return render_template('index.html', text=text)
        else:
            return render_template('index.html', text='none')
    else:
        return render_template('index.html', text='none')

def transcribe():
    text = get_text()
    return render_template('index.html', text=text)

@app.route('/immerse_token', methods=['POST'])
def immerse_token():
    response = get_immersive_reader_token()
    return response

if __name__ == "__main__":
    app.run(debug = True)
