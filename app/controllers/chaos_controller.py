from flask import Blueprint, jsonify
from services.chaos_service import ChaosService

chaos_bp = Blueprint("chaos", __name__)


@chaos_bp.route("/success", methods=["GET"])
def success():

    response, status_code = ChaosService.get_success_response()

    return jsonify(response), status_code


@chaos_bp.route("/toggle-error", methods=["POST"])
def toggle_error():

    response = ChaosService.toggle_error_mode()

    return jsonify(response), 200