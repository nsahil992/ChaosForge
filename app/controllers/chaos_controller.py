from flask import Blueprint, jsonify, Response
from prometheus_client import generate_latest
from services.chaos_service import ChaosService
from utils.metrics import registry

import time

from utils.metrics import (
    REQUEST_COUNT,
    REQUEST_LATENCY,
    ERROR_COUNT,
    CPU_BURN_COUNT,
    MEMORY_LEAK_COUNT
)

chaos_bp = Blueprint("chaos", __name__)


# Healthy endpoint
@chaos_bp.route("/success", methods=["GET"])
def success():

    start_time = time.time()

    REQUEST_COUNT.labels(
        method="GET",
        endpoint="/success"
    ).inc()

    response = ChaosService.get_success_response()

    REQUEST_LATENCY.observe(
        time.time() - start_time
    )

    if response[1] == 500:
        ERROR_COUNT.inc()

    return response


# Failure toggle endpoint
@chaos_bp.route("/toggle-error", methods=["POST"])
def toggle_error():

    REQUEST_COUNT.labels(
        method="POST",
        endpoint="/toggle-error"
    ).inc()

    response = ChaosService.toggle_error_mode()

    return jsonify(response), 200


# Slow response simulation endpoint
@chaos_bp.route("/slow-down", methods=["GET"])
def slow_down():

    start_time = time.time()

    REQUEST_COUNT.labels(
        method="GET",
        endpoint="/slow-down"
    ).inc()

    response, status_code = ChaosService.simulate_slow_response()

    REQUEST_LATENCY.observe(
        time.time() - start_time
    )

    return jsonify(response), status_code


# Health check endpoint
@chaos_bp.route("/health", methods=["GET"])
def health():

    REQUEST_COUNT.labels(
        method="GET",
        endpoint="/health"
    ).inc()

    response, status_code = ChaosService.get_health_status()

    return jsonify(response), status_code


# Prometheus metrics endpoint
@chaos_bp.route("/metrics", methods=["GET"])
@chaos_bp.route("/metrics", methods=["GET"])
def metrics():
    return Response(
        generate_latest(registry),
        mimetype="text/plain"
    )


# CPU stress simulation endpoint
@chaos_bp.route("/cpu-burn", methods=["POST"])
def cpu_burn():

    REQUEST_COUNT.labels(
        method="POST",
        endpoint="/cpu-burn"
    ).inc()

    CPU_BURN_COUNT.inc()

    response = ChaosService.cpu_burn()

    return jsonify(response), 200


# Memory leak simulation endpoint
@chaos_bp.route("/memory-leak", methods=["POST"])
def memory_leak():

    REQUEST_COUNT.labels(
        method="POST",
        endpoint="/memory-leak"
    ).inc()

    MEMORY_LEAK_COUNT.inc()

    response = ChaosService.memory_leak()

    return jsonify(response), 200