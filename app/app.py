#!/usr/bin/env python

from flask import Flask, request
from pushbullet import PushBullet
app = Flask(__name__)

pb = PushBullet(YOUR_TOKEN)
device = pb.devices[1]

@app.route('/button', methods=["POST", "GET"])
def button_pressed():
    print("request : {}".format(request.data)) # for debug purpose...

    message = ""
    title = "Sensit button pressed"
    pb.push_note(title, message, device=device)
    return message


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=31415)
