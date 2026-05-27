from flask import jsonify
import time
from models.state import ChaosState

from metrics.prometheus_metrics import (
    REQUEST_COUNT,
    ERROR_MODE
)

from utils.cpu_stress import burn_cpu
from utils.memory_stress import leak_memory

class ChaosService:

    # Healthy response service
    @staticmethod
    def get_success_response():

        REQUEST_COUNT.inc()

        if ChaosState.error_mode:

            print("[CRITICAL] Database Connection Timeout!")

            return jsonify({
                "status": "error",
                "message": "Simulated system failure"
            }), 500

        return jsonify({
            "status": "success",
            "message": "ChaosForge healthy"
        }), 200

    # Failure toggle service
    @staticmethod
    def toggle_error_mode():

        ChaosState.error_mode = not ChaosState.error_mode

        ERROR_MODE.set(
            1 if ChaosState.error_mode else 0
        )

        return {
            "status": "success",
            "error_mode": ChaosState.error_mode,
            "message": "Chaos mode toggled"
        }

    # Slow response simulation service
    @staticmethod
    def simulate_slow_response():

        time.sleep(5)

        return {
            "status": "slow",
            "message": "Response delayed intentionally by 5 seconds"
        }, 200

    # Application health service
    @staticmethod
    def get_health_status():

        if ChaosState.error_mode:
            return {
                "status": "DEGRADED",
                "message": "Chaos mode active"
            }, 200

        return {
            "status": "UP",
            "message": "Application healthy"
        }, 200

    # CPU stress simulation service
    @staticmethod
    def cpu_burn():

        burn_cpu()

        return {
            "status": "success",
            "message": "CPU burn simulation completed"
        }

    # Memory leak simulation service
    @staticmethod
    def memory_leak():

        allocations = leak_memory()

        return {
            "status": "warning",
            "message": "Memory leak simulated",
            "allocations": allocations
        }