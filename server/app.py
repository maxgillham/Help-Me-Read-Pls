import requests
from utils import *
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('Record') == 'Record':
            ob = open("text.txt", 'r')
            text = ob.read() + " "
            text += get_text()
            ob.close()
            ob = open("text.txt", 'w')
            ob.write(text)
            ob.close()
            keywords = get_key_words()
            return render_template('index.html', text=text, keywords=keywords)
        else:
            ob = open("text.txt", "w")
            ob.write(" ")
            ob.close()
            return render_template('index.html', text='', keywords='')
    else:
        return render_template('index.html', text='',keywords='')

def transcribe():
    text = get_text()
    return render_template('index.html', text=text)

@app.route('/immerse_token', methods=['POST'])
def immerse_token():
    response = get_immersive_reader_token()
    return response

if __name__ == "__main__":
    app.run(debug = True)
