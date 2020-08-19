from flask import redirect, url_for, Response, request
from application import app
import requests
import random

@app.route('/')
@app.route('/animal/name' methods=['GET','POST'])
def animal_name():
    animal_list=["dog","goat","pig","cat","cow"]
    the_data = random.choice(animal_list)
    return Response("Animal: " + the_data, mimetype='text/plain')

@app.route('/animal/noise' methods=['GET','POST'])
def animal_noise():
    response=request.data.decode('utf-8')
    if response == "dog":
        noise = "bark"
    elif response == "goat":
        noise = "bleat"
    elif response == "pig":
        noise = "oink"
    elif response == "cat":
        noise = "meow"
    elif response == "cow":
        noise = "moo"
    else:
        noise = "Hmmm???"
    return Response(noise, mimetype='text/plain')
