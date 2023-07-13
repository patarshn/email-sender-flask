from flask import Flask, Response, request
import json
from models.EventModel import Event
from app import db
from flask import jsonify
from helpers.base_response import *
from helpers.base_request import *

def get(id):
    event = Event.query.filter_by(id=id).first()
    if not event:
        return baseResponseErrorNotFound()
    data = {
        "id" : event.id,
        "name" : event.name
    }
    return baseResponseSuccess(data)

def gets():
    events = Event.query.all()
    data = []
    for event in events:
        data.append({
            "id" : event.id,
            "name" : event.name
        })
    return baseResponseSuccess(data)

def post():
    reqData = baseRequestData(request)
    name = reqData.get('name')
    event = Event(name)
    db.session.add(event)
    db.session.commit()
    data = {
        "id" : event.id,
        "name" : event.name
    }
    return baseResponseSuccessCreated(data)


