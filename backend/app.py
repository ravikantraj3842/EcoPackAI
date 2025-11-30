from flask import Flask, request, jsonify
from routes.recommend import get_recommendation

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "EcoPackAI Backend Running"}), 200

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    result = get_recommendation(data)
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)

