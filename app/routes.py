from app import app #imports app variable from init.py to activate flask

from flask import render_template,url_for,redirect #functions in flask we have access to

@app.route("/")
def hello():
    name = 'Jon Snow'

    characters = {
        "females":['Arya','Daenarys'],
        "males":['Jamie','Jon','Ned','Tyrion']
    }
    return render_template("index.html", name = name, characters = characters)

@app.route('/profile/<gender>/<name>',methods = ['GET'])
def profile(name, gender):
    info = {}

    if gender == 'males':
        gender = 'Male'

    else:
        gender = 'Female'

    if name == 'Arya':
        info = {
            "profile_pic": 'http://placehold.it/250x250',
            "house": 'Stark',
            "home": "Winterfell",
            "weapon": "Needle",
        }
    elif name == 'Jamie':
        info = {
            "profile_pic": 'http://placehold.it/250x250',
            "house": "Lannister",
            "home": "Casterly Rock",
            "weapon": "Oathkeeper"
        }
    return render_template("profile.html", name = name, info = info, gender = gender)