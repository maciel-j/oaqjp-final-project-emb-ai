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

    return response.text