from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import os
import sys
from scrape_mars import scrape

app = Flask(__name__)

#mongo = PyMongo(app, uri="mongodb://localhost:27017/notepad")
mongo = PyMongo(app, uri="mongodb+srv://Scott:nN5GELRQucw.qJb@cluster0.w73ay.mongodb.net/notepad?retryWrites=true&w=majority")

@app.route('/')
def index():
    
    #print(mars['news_title'])
    return render_template('index.html')
    #return render_template('index.html')

@app.route('/api/notes/mongo')
def note_mongo():
    notes = mongo.db.tasks.find()
    data = []

    for note in notes:
        data.append({
            '_id': str(note['_id']),
            'content': note['content']
        })

    return jsonify(data)

if __name__=="__main__":
    app.run(debug=True)