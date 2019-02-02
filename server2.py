from flask import Flask
from flask import request
import json


app = Flask(__name__)

@app.route("/anton", methods=["GET"])
def anton_oni():
    anton = {
        "name": "Anton",
        "l_name": "Oni",
        "age": 26,
        "sex": "Male"
    }
    return json.dumps(anton)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)