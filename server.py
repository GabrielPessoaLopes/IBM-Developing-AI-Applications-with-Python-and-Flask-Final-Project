"""
server.py

Flask web server for the Emotion Detection application.
Handles user input, calls the emotion detection function, 
and returns formatted results or error messages.
"""

from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the main page of the application.

    Returns:
        str: Rendered index.html template.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    Process submitted text and return detected emotions.
    
    If the text is blank or the API returns invalid results, 
    an error message is returned. Otherwise, returns a formatted 
    string with each emotion score and the dominant emotion.

    Returns:
        str: Formatted response string with emotions or an error message.
    """
    text_to_analyze = request.form.get("text", "").strip()
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response


def main():
    """
    Start the Flask server on host 0.0.0.0 and port 5000.
    """
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
