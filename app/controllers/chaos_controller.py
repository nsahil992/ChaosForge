from flask import Blueprint, jsonify

chaos_bp = Blueprint("chaos", __name__)

@chaos_bp.route("/success", methods=["GET"])
def success():
    return jsonify({
        "status": "success",
        "message": "ChaosForge healthy"
    }), 200