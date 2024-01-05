from flask import Flask, request, jsonify
import whisper
from pydub import AudioSegment
import os


model = whisper.load_model("base")  # You can choose different model sizes


def transcribe_audio(audio_file_request):

    audio_file = audio_file_request.files["file"]
    temp_path = 'temp_file'
    audio_file.save(temp_path)

    # Convert to WAV if necessary
    audio = AudioSegment.from_file(temp_path)
    wav_path = 'output.wav'

    audio = AudioSegment.from_file(temp_path)
    audio.export(wav_path, format='wav')
    result = model.transcribe(wav_path)
    transcription = result['text']
    return (transcription)



import requests
import json

API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    try:
        global API_URL
        global headers
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    except(KeyError):
        return "Short Content"


def retrieve_top_scores(scores):
    if scores == "Short Content":
        return  jsonify("Content is too short for analysis")
    else:
        scores = scores[0]
        top_five = []
        for i in range (5):
            temp = []
            temp.append(scores[i].get("label").capitalize())
            temp.append(round(scores[i].get("score")*100,0))
            top_five.append(temp)
        return top_five


