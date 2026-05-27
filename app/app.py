from flask import Flask
from controllers.chaos_controller import chaos_bp

app = Flask(__name__)

app.register_blueprint(chaos_bp)

@app.route("/")
def home():
    return {
        "project": "ChaosForge",
        "status": "running"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=False, use_reloader=False)