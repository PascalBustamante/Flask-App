from flask import Blueprint, request
from .models import db, Event

database_bp = Blueprint('database_bp',__name__)

def format_event(event): ##for easy frontend use
    return {
        "descrition": event.description,
        "id": event.id,
        "created_at": event.created_at
    }

@database_bp.route('/event', methods=['POST'])
def create_event():
    description = request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    return format_event(event)

    