from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "world"

@app.route('/pod')
def get_pod_name():
    return os.environ['POD']

if __name__ == "__main__":
    app.run(port=5000, debug=True)
