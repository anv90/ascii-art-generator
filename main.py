"""
app.post (because we want to have a longer message)
    body:
        message - str
        sprite - bool
    if sprite
        method that gets the sprite and the message -> cowsay
        return json
    else 
        method that turns the text into ascii ->text2art
        return json str

"""
from flask import Flask, request, jsonify
from art import *

app = Flask(__name__)

def sprite_msg(msg) -> str:
    # To do: generate sprite and message
    return "temporary"

def text2art_msg(msg) -> str: 
    return text2art(msg)

@app.post('/ascii')
def ascii_handler(): 
    # Access passed json 
    data = request.get_json()

    # Check for valid json 
    if (data == None): 
        return jsonify({"error": 'Request must be of type JSON with fields "message" (string) and "sprite" (bool)'}), 400
    elif ("message" not in data): 
        return jsonify({"error": '"message" is a required field of type string'}), 400
    elif ("sprite" not in data): 
        return jsonify({"error": '"sprite" is a required field of type bool'}), 400

    # Access message and sprite info 
    message = data["message"]
    sprite = data["sprite"]

    if sprite: 
        return jsonify({"message": sprite_msg(message)}), 200
    else: 
        return jsonify({"message": text2art_msg(message)}), 200


if (__name__ == '__main__'):
    # Temporarily set to port 8000. Can be changed if needed
    app.run(port = 8000)