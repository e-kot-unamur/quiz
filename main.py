from flask import Flask, send_from_directory
import random

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
@app.route("/about")
@app.route("/IST-MST/help")
@app.route("/IST-MST")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

if __name__ == "__main__":
    app.run(debug=True)