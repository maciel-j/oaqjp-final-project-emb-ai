"""Module to text Emotion Detection"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Define a function named emotion_detector that takes a string input (text_to_analyse)
    """
    url = "https://sn-watson-emotion.labs.skills.network" \
    + "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    input_json =  { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_json, headers=headers, timeout=10)

    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        anger_score =  None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

        return     {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }


    anger_score =  formatted_response['emotionPredictions'][0]["emotion"]["anger"]
    disgust_score = formatted_response['emotionPredictions'][0]["emotion"]["disgust"]
    fear_score = formatted_response['emotionPredictions'][0]["emotion"]["fear"]
    joy_score = formatted_response['emotionPredictions'][0]["emotion"]["joy"]
    sadness_score = formatted_response['emotionPredictions'][0]["emotion"]["sadness"]

    dominant_emotion = max(
        formatted_response['emotionPredictions'][0]["emotion"],
        key=formatted_response['emotionPredictions'][0]["emotion"].get
    )

    return     {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }