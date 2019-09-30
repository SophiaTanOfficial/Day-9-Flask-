import os
from app import app
from flask import render_template, request, redirect

events = [ #List of dictionaries/objects/documents
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"},
        {"event":"Fintech Graduation", "date":"2019-08-02"},
        {"event":"Leaving for College", "date": "2019-08-23"},
        {"event":"Liberty Science Center Field Trip", "date": "2019-07-25"}
    ] #Events passed in our index route
#A static list

myPassword = "HZL9r0wMsEHyce4Q"


#This line let's us use flask_pymongo to get to PyMongo (Which is a class)
from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'test' 

# URI of database
#Gotta remember to fill in our password where it says <password>. Get rid of the <> too
app.config['MONGO_URI'] = 'mongodb+srv://admin:HZL9r0wMsEHyce4Q@cluster0-u5agh.mongodb.net/test?retryWrites=true&w=majority' 

#This creates an object from the class with the argument 'app'
#We have configured app before creating this so it has our information in this object
mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    #Open up index.html, pass events data with it! (Events is a dictionary up top)
    #first, connect to database. eventsDB is the ENTIRE collection
    eventsDB = mongo.db.events
    
    #making a query == asking DB for information 
    #events here is what we get back from Mongo
    #.find - what do we want from database? Sending an empty dictionary ({}) gets us everything back
    events = eventsDB.find()
    return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA

@app.route('/add')
def add():
    # connect to the database
    #Creates a variable called users that is equal to our mongo object, the database part, the useres part
    #mongo is smart enough to make new collections if they don't exist yet
    #this is our tunnel from python -> tthe users collection in mongo
    users = mongo.db.users #Go to that collection in that database
    # insert new data
    #Use our new variable and a mongo specific method called insert
    #this takes an argument of what we will send ot mongo in the form of a dictionary, which mongo will call'documents.' It can have any number of keys and values
    users.insert({"name": "Sophia"})
    users.insert({"name": "User"})
    print("User created.")
    # return a message to the user
    return render_template("index.html", events=events)
    
@app.route("/addEvent")
def addEvent():
    events = mongo.db.events
    #Add an event
    events.insert({"event" :"College", "date":"2019-08-23"})
    
    #return a thing! Maybe a template! let's redirect!
    return redirect("/")
