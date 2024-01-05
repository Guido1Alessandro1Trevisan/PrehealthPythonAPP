from flask import Flask

app = Flask(__name__)

from flask import jsonify, request

from time import sleep
import random

import speechSentimentalAnalysis
import questions
from question_evaluator import generate_feedback
import json
import os


@app.route("/")
@app.route("/getQuestion", methods=["GET"])
def getquestions():
    question = questions.get_question()
    return jsonify(question)
#Typed - Response
@app.route("/typedEvaluation", methods=["POST"])
def typedEvaluation():
    try: 
        data = request.json
        questionInput = data['questionInput']
        output = data['answerInput']
        emotion_scores = speechSentimentalAnalysis.query(output)
        top5emotions = speechSentimentalAnalysis.retrieve_top_scores(emotion_scores)
        feedback = generate_feedback(questionInput, output)
        return jsonify({"transcription": output, "feedback": feedback, "top5emotions": top5emotions})
    except Exception as e:
        print(str(e))
        return jsonify(str(e))     
#Audio - Response
@app.route("/speechAnalysis", methods=["POST"])
def speechAnalysis(): 
    output = speechSentimentalAnalysis.transcribe_audio(request)
    feedback = generate_feedback("what is the worst thing you did", output)
    emotion_scores = speechSentimentalAnalysis.query(output)
    top5emotions = speechSentimentalAnalysis.retrieve_top_scores(emotion_scores)
    return jsonify({"transcription": output, "feedback": feedback, "top5emotions": top5emotions})

if __name__ == "__main__": 
    app.run(host = "0.0.0.0", port=5000)