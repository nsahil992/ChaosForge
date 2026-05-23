from models.state import ChaosState

class ChaosService:

    @staticmethod
    def get_success_response():

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

        return {
            "error_mode": ChaosState.error_mode
        }