from flask import Blueprint
import controllers.EmailSchedulerController as EmailSchedulerController

EmailSchedulerBlueprint = Blueprint('EmailSchedulerBlueprint', __name__)
EmailSchedulerBlueprint.route('/', methods=['GET'])(EmailSchedulerController.gets)
EmailSchedulerBlueprint.route('/<id>', methods=['GET'])(EmailSchedulerController.get)
EmailSchedulerBlueprint.route('/', methods=['POST'])(EmailSchedulerController.post)
