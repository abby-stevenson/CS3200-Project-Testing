from flask import Blueprint, request, jsonify, make_response, current_app, redirect, url_for
import json
from backend.db_connection import db #Some sample code 
from backend.simple.playlist import sample_playlist_data #Some sample data

# This blueprint handles some basic routes that you can use for testing
simple_routes = Blueprint('simple_routes', __name__)
#Flask blueprint object and we are storing it under simple_routes 


# ------------------------------------------------------------
# / is the most basic route
# Once the api container is started, in a browser, go to 
# localhost:4000/playlist
@simple_routes.route('/')
#Define the python function that represents the functionality that you want your API to have 
#This is set up to return HTML but in your project the API should only serve up data 
def welcome():
    current_app.logger.info('GET / handler')
    welcome_message = '<h1>Welcome to the CS 3200 Project Template REST API</h1>'
    response = make_response(welcome_message) #This is the response of the request response cycle
    #The above line is packaging up the welcome message and sending it back
    response.status_code = 200 #Represents everything is good on the server side
    return response

# ------------------------------------------------------------
# /playlist returns the sample playlist data contained in playlist.py
# (imported above)
@simple_routes.route('/playlist')
def get_playlist_data():
    current_app.logger.info('GET /playlist handler')
    response = make_response(jsonify(sample_playlist_data))
    response.status_code = 200
    return response

# ------------------------------------------------------------
#The default verb is always get so here you dont need the phrase after the last comma
#You would type localhost:4001/niceMessage
@simple_routes.route('/niceMesage', methods = ['GET'])
def affirmation():
    message = '''
    <H1>Think about it...</H1>
    <br />
    You only need to be 1% better today than you were yesterday!
    '''
    response = make_response(message)
    response.status_code = 200
    return response

#This is a get method as that is the default
@simple_routes.route("/hello")
def hello():
    message = "<H1>Hello CS3200</H1>"
    response = make_response(message)
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Demonstrates how to redirect from one route to another. 
@simple_routes.route('/message')
def mesage():
    return redirect(url_for(affirmation))

#The flask application knows about simple routes (knows that these routes are here and to process them)
#Inside the rest_entry file this file is imported and then it registers the simple routes object with the 
#flask application object 
#The flask app is running in a little simple web server