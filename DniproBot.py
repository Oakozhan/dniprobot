from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def test():
    return "It works"

@app.route("/hook", methods=["POST"])
def hook():
    chat_id = request.get_json()["message"]["chat"]["id"]
    requests.post("https://api.telegram.org/bot210028783:AAFHZGggLg6ffvbryE9LSrz5IqCfF5YnzOY/sendMessage",
                  {
                      "chat_id": chat_id,
                      "text": "hi!"
                  })
    return "OK"
