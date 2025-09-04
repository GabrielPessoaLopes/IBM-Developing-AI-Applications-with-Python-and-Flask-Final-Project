import requests
import json

def emotion_detector(text_to_analyze):
    # Watson NLP API endpoint
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    # Required headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON with the text
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Send POST request
    response = requests.post(url, headers=headers, json=input_json)
    
    # Convert response text into a Python dictionary
    response_dict = json.loads(response.text)
    
    # Extract emotions and their scores
    emotions = response_dict["emotionPredictions"][0]["emotion"]
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]
    
    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the formatted dictionary
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
