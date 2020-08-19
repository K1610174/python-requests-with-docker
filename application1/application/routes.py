from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/')

@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/generate', methods=['GET','POST'])
def generate():
    #response = requests.get("http://application2:5000/animal")
    response1=requests.get('https://35.246.20.139:5001/animal')
    response2=requests.get('https://35.246.20.139:5001/noise')
    return (response1.text , response2.text)


