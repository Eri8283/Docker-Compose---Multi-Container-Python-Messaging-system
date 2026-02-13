from flask import Flask
app = Flask(__name__)

@app.route("/")
def quote():
    return "Nobody expects the Spanish Inquisition!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
