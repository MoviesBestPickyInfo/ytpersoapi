from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/transcript")
def transcript():
    video_id = request.args.get("id")
    try:
        data = YouTubeTranscriptApi().fetch(video_id)
        text = " ".join([x.text for x in data])
        return jsonify({"text": text})
    except:
        return jsonify({"text": ""})

app.run(host="0.0.0.0", port=10000)
