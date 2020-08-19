from flask import redirect, url_for, Response, request
from application import app
import requests
import random

@app.route('/')
@app.route('/animal' methods=['GET','POST'])
def animal():
    animal_list=["dog","goat","pig","cat","cow"]
    the_data = random.choice(animal_list)
    return Response("Animal: " + the_data, mimetype='text/plain')

@app.route('/noise' methods=['GET','POST'])
def noise():
    response=requests.get('https://35.246.20.139:5000/animal')
    if response.text == "dog":
        return "bark"
    elif response.text == "goat":
        return "bleat"
    elif response.text == "pig":
        return "oink"
    elif response.text == "cat":
        return "meow"
    elif response.text == "cow":
        return "moo"