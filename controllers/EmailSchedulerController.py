from flask import Flask, Response, request
import json
from models.EmailSchedulerModel import EmailScheduler
from app import db
from flask import jsonify
from helpers.base_response import *
from helpers.base_request import *

def get(id):
    emailScheduler = EmailScheduler.query.filter_by(id=id).first()
    if not emailScheduler:
        return baseResponseErrorNotFound()
    data = {
        "id" : emailScheduler.id,
        "event_id" : emailScheduler.event_id,
        "email_subject" : emailScheduler.email_subject,
        "email_content" : emailScheduler.email_content,
        "timestamp" : emailScheduler.timestamp,
        "is_sending" : emailScheduler.is_sending
    }
    return baseResponseSuccess(data)

def gets():
    emailSchedulers = EmailScheduler.query.all()
    data = []
    for emailScheduler in emailSchedulers:
        data.append({
            "id" : emailScheduler.id,
            "event_id" : emailScheduler.event_id,
            "email_subject" : emailScheduler.email_subject,
            "email_content" : emailScheduler.email_content,
            "timestamp" : emailScheduler.timestamp,
            "is_sending" : emailScheduler.is_sending
        })
    return baseResponseSuccess(data)

def post():
    reqData = baseRequestData(request)
    event_id = reqData.get('event_id')
    email_subject = reqData.get('email_subject')
    email_content = reqData.get('email_content')
    timestamp = reqData.get('timestamp')
    is_sending = False

    emailScheduler = EmailScheduler(event_id, email_subject, email_content, timestamp, is_sending)
    db.session.add(emailScheduler)
    db.session.commit()
    data = {
        "id" : emailScheduler.id,
        "event_id" : emailScheduler.event_id,
        "email_subject" : emailScheduler.email_subject,
        "email_content" : emailScheduler.email_content,
        "timestamp" : emailScheduler.timestamp
    }
    return baseResponseSuccessCreated(data)


