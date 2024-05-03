from flask import Flask, jsonify
import make_requests as mr

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)

