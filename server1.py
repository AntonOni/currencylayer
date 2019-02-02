from flask import Flask
from flask import request
from news_checker import NewsChecker
import json





app = Flask("server1")
a = NewsChecker()

@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        news = a.work()
        resp = {"news": news}
        return json.dumps(resp)
    return "Server #1 OFFLINE"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)




