from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Hello, Flask API!"})


@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")
    return jsonify({"message": f"Hello, {name}!"})


@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({"received": data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
