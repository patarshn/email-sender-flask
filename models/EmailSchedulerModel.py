from app import db

class EmailScheduler(db.Model):
    __tablename__ = 'email_schedulers'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer,db.ForeignKey('events.id'),nullable=False)
    email_subject = db.Column(db.String(255))
    email_content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime,nullable=False)
    is_sending = db.Column(db.Boolean,default=0)

    def __init__(self, event_id, email_subject, email_content, timestamp, is_sending):
        self.event_id = event_id
        self.email_subject = email_subject
        self.email_content = email_content
        self.timestamp = timestamp
        self.is_sending = is_sending