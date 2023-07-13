from flask import Blueprint
import controllers.EventController as EventController

EventBlueprint = Blueprint('EventBlueprint', __name__)
EventBlueprint.route('/', methods=['GET'])(EventController.gets)
EventBlueprint.route('/<id>', methods=['GET'])(EventController.get)
EventBlueprint.route('/', methods=['POST'])(EventController.post)
