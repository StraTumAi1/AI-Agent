from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/call-event", methods=["POST"])
def handle_call():
    data = request.json
    caller_name = data.get("name")
    device = data.get("device")
    issue = data.get("issue")
    response_text = f"Thanks {caller_name}, your {device} will be ready soon!"
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run()
