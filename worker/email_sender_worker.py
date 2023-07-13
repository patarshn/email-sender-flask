from lib.EmailSender import EmailSender
from flask import Flask, request
from models.EmailSchedulerModel import EmailScheduler
from models.ParticipantModel import Participant
from datetime import datetime
from app import app, db
from sqlalchemy import or_, and_

def email_sender_worker():
    with app.app_context():
        current_time = datetime.now()
        current_time_start = current_time.replace(second=0)
        current_time_end = current_time.replace(second=59)
        emails = EmailScheduler.query.filter(
            EmailScheduler.timestamp <= current_time_end,
            EmailScheduler.is_sending.is_not(True)
        ).all()
        print(emails)
        
        email_sender = EmailSender()
        for email in emails:
            email_subject = email.email_subject
            email_message = email.email_content
            event_id = email.event_id
            participants = Participant.query.filter(
                Participant.event_id == event_id
            ).all()

            list_participant = []
            for participant in participants:
                list_participant.append(participant.email)
            recipient_email = ','.join(list_participant)
            print(recipient_email)
            res = email_sender.send_email(recipient_email, email_subject, email_message)
            res=True
            if(res):
                email.is_sending = True
                db.session.commit()

        print("Email sending")


