from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    # Loads index.html from the templates folder
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    text_to_analyze = request.form["text"]
    response = emotion_detector(text_to_analyze)

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    result = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return result

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
