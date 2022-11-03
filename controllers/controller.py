from flask import render_template, request
from app import app
from models.todo_list import events, add_new_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def add_event():
  eventDate = request.form['date']
  eventName = request.form['name']
  eventParticipants = request.form['participants']
  eventLocation = request.form['location']
  eventDesc = request.form['description']
  eventRecurrence = request.form['recurring']
  newEvent = Event(date=eventDate, name_event=eventName, guest_number=eventParticipants, location=eventLocation, description=eventDesc, recurrence=eventRecurrence)
  add_new_event(newEvent)

  return render_template('index.html', title='Home', event=events)
