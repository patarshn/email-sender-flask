from flask import Blueprint
import controllers.ParticipantController as ParticipantController

ParticipantBlueprint = Blueprint('ParticipantBlueprint', __name__)
ParticipantBlueprint.route('/', methods=['GET'])(ParticipantController.gets)
ParticipantBlueprint.route('/<id>', methods=['GET'])(ParticipantController.get)
ParticipantBlueprint.route('/', methods=['POST'])(ParticipantController.post)
