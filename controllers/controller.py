from flask import render_template, request
from app import app
from models.events_list import events_list, add_new_event
# from models.events import Event

@app.route('/events')
def index():
    return render_template('index.html', title= 'Events', list_of_events=events_list) #list_of_events connects list_of_events in html file in for loop

@app.route('/events', methods=['POSTS'])
def add_new_event():
    event_name = request.form['name']
    event_date = request.form['dates']