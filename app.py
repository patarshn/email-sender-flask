from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
scheduler = BackgroundScheduler()
scheduler.start()

# migrations
from models.EventModel import Event
from models.EmailSchedulerModel import EmailScheduler
from models.ParticipantModel import Participant

# routes
from routes.RouteBlueprint import RouteBlueprint
from routes.EventBlueprint import EventBlueprint
from routes.ParticipantBlueprint import ParticipantBlueprint
from routes.EmailSchedulerBlueprint import EmailSchedulerBlueprint

# worker
from worker.email_sender_worker import email_sender_worker
scheduler.add_job(email_sender_worker, 'cron', minute='*')


app.register_blueprint(RouteBlueprint, url_prefix='')
app.register_blueprint(EventBlueprint, url_prefix='/events')
app.register_blueprint(ParticipantBlueprint, url_prefix='/participants')
app.register_blueprint(EmailSchedulerBlueprint, url_prefix='/email_schedulers')


    
if __name__ == '__main__':
    app.debug = True
    app.run()
