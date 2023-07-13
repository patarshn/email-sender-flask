from flask import Blueprint
import controllers.EmailSchedulerController as EmailSchedulerController

RouteBlueprint = Blueprint('RouteBlueprint', __name__)
RouteBlueprint.route('/save_emails', methods=['POST'])(EmailSchedulerController.post)
