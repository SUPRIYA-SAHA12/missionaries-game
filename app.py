
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validate", methods=["POST"])
def validate():
    data = request.json
    # Extract state info from frontend
    left = data['left']
    right = data['right']
    boat = data['boat']
    
    # Check game logic
    def is_valid(side):
        m, c = side
        return m == 0 or m >= c

    if is_valid(left) and is_valid(right):
        return jsonify({"valid": True})
    else:
        return jsonify({"valid": False, "message": "Cannibals ate missionaries!"})

if __name__ == "__main__":
    app.run(debug=True)