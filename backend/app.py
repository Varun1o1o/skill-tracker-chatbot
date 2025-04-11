
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    if "log" in user_message:
        return jsonify({"reply": "Logged 'Python' skill at beginner level. Nice start!"})

    elif "progress" in user_message:
        return jsonify({"reply": "You're 70% through your Python skill goal. Keep going!"})

    elif "recommend" in user_message or "suggest" in user_message:
        return jsonify({"reply": "Try building a small project using Python and Flask!"})

    elif "goal" in user_message:
        return jsonify({"reply": "Goal set to become proficient in Python within 30 days!"})

    else:
        return jsonify({"reply": "I can help you log skills, track progress, set goals, or recommend steps. Try asking!"})

if __name__ == "__main__":
    app.run(debug=True)
