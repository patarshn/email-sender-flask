from app import db

class Participant(db.Model):
    __tablename__ = 'participants'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer,db.ForeignKey('events.id'),nullable=False)
    email = db.Column(db.String(128),nullable=False)

    def __init__(self, event_id, email):
        self.event_id = event_id
        self.email = email