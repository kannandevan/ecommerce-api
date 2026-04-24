from routes.auth import auth_bp
from flask import Flask, jsonify

app = Flask(__name__)

app.register_blueprint(auth_bp, url_prefix="/api/auth")

@app.route("/")
def home():
    return jsonify({"message":"Auth API Running"})

if __name__ == "__main__":
    app.run(debug=True)