from flask import Flask, jsonify, send_file
import os

base_folder = "numbers"
list_numbers = []
for l in os.listdir(base_folder):
    list_numbers.append(f"{base_folder}/{l}")

app = Flask(__name__)

application = app

@app.route("/<int:videoID>")
def videoID(videoID):

    print(videoID)

    return send_file(f"{list_numbers[videoID]}", mimetype='video/mp4')




@app.route("/videos")
def video_list():
    return jsonify({
        "length": len(list_numbers),
        "urls": list_numbers
    })


if __name__ == '__main__':
    app.run()