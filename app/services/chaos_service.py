from models.state import ChaosState
import time
from metrics.prometheus_metrics import REQUEST_COUNT, ERROR_MODE
from utils.cpu_stress import burn_cpu

class ChaosService:

    @staticmethod
    def get_success_response():

        REQUEST_COUNT.inc()

        if ChaosState.error_mode:
            return {
                "status": "error",
                "message": "Simulated system failure"
            }, 500

        return {
            "status": "success",
            "message": "ChaosForge healthy"
        }, 200

    @staticmethod
    def toggle_error_mode():

        ChaosState.error_mode = not ChaosState.error_mode

        ERROR_MODE.set(1 if ChaosState.error_mode else 0)

        return {
            "error_mode": ChaosState.error_mode
        }

    @staticmethod
    def simulate_slow_response():

        time.sleep(5)

        return {
            "status": "slow",
            "message": "Response delayed intentionally by 5 seconds"
        }, 200

    @staticmethod
    def get_health_status():

        if ChaosState.error_mode:
            return {
                "status": "DOWN",
                "message": "Chaos mode active"
            }, 503

        return {
            "status": "UP",
            "message": "Application healthy"
        }, 200

    @staticmethod
    def cpu_burn():

        burn_cpu()

        return {
            "status": "success",
            "message": "CPU burn simulation completed"
        }