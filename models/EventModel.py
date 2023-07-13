from app import db

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    emailshedulers = db.relationship('EmailScheduler', backref='events', lazy=True)
    participants = db.relationship('Participant', backref='events', lazy=True)

    def __init__(self, name):
        self.name = name
