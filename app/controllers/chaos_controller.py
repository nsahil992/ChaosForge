from flask import Blueprint, jsonify
from services.chaos_service import ChaosService
from prometheus_client import generate_latest
from flask import Response
chaos_bp = Blueprint("chaos", __name__)

# Success controller
@chaos_bp.route("/success", methods=["GET"])
def success():

    response, status_code = ChaosService.get_success_response()

    return jsonify(response), status_code

# Toggle error controller
@chaos_bp.route("/toggle-error", methods=["POST"])
def toggle_error():

    response = ChaosService.toggle_error_mode()

    return jsonify(response), 200

# Slow down controller
@chaos_bp.route("/slow-down", methods=["GET"])
def slow_down():

    response, status_code = ChaosService.simulate_slow_response()

    return jsonify(response), status_code

# Health controller
@chaos_bp.route("/health", methods=["GET"])
def health():

    response, status_code = ChaosService.get_health_status()

    return jsonify(response), status_code

# Metrics controller
@chaos_bp.route("/metrics", methods=["GET"])
def metrics():

    return Response(
        generate_latest(),
        mimetype="text/plain"
    )

# CPU high usage controller
@chaos_bp.route("/cpu-burn", methods=["POST"])
def cpu_burn():

    return ChaosService.cpu_burn()

# Memory leak controller
@chaos_bp.route("/memory-leak", methods=["POST"])
def memory_leak():

    return ChaosService.memory_leak()