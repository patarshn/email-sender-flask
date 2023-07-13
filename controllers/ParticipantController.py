from flask import Flask, Response, request
import json
from models.ParticipantModel import Participant
from app import db
from flask import jsonify
from helpers.base_response import *
from helpers.base_request import *

def get(id):
    participant = Participant.query.filter_by(id=id).first()
    if not participant:
        return baseResponseErrorNotFound()
    data = {
        "id" : participant.id,
        "event_id" : participant.event_id,
        "email" : participant.email
    }
    return baseResponseSuccess(data)

def gets():
    participants = Participant.query.all()
    data = []
    for participant in participants:
        data.append({
            "id" : participant.id,
            "event_id" : participant.event_id,
            "email" : participant.email
        })
    return baseResponseSuccess(data)

def post():
    reqData = baseRequestData(request)
    event_id = reqData.get('event_id')
    email = reqData.get('email')

    participant = Participant(event_id, email)
    db.session.add(participant)
    db.session.commit()
    data = {
        "id" : participant.id,
        "event_id" : participant.event_id,
        "email" : participant.email
    }
    return baseResponseSuccessCreated(data)


