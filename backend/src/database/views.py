from flask import Blueprint, request
from .models import db, Event


database = Blueprint('database_bp',__name__)

def format_event(event): ##for easy frontend use
    return {
        "description": event.description,
        "id": event.id,
        "created_at": event.created_at
    }

# create event
@database.route('/event', methods=['POST'])
def create_event():
    description = request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    return format_event(event)

# get all events
@database.route('/events', methods = ['GET'])
def get_events():
    events = Event.query.order_by(Event.id.asc()).all() 
    event_list = []
    for event in events:
        event_list.append(format_event(event))
    return {'events': event_list}

@database.route('/events/<id>', methods=['GET'])
def get_event(id):
    event = Event.query.filter_by(id=id).one()    #id should be unique
    formatted_event = format_event(event)

    return {'event': formatted_event}

@database.route('/events/<id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.filter_by(id=id).one()    #id should be unique
    db.session.delete(event)
    db.session.commit()
    return f'Event (id: {id} deleted.)'

@database.route('/events/<id>', methods=['PUT'])
def update_event(id):
    event = Event.query.filter_by(id=id).one()  #id should be unique
    description = request.json['description']
    event.update_description(new_description = description)

    return {'event': format_event(event=event)}