import azure.cognitiveservices.speech as speechsdk
import keys
import requests
import json

def get_text():
    """
    This method will open the mic and conduct live speech to
    text transcription
    """
    region = "eastus"
    speech_key = keys.keys['speech_key']
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=region)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    result = speech_recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        output = result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        output = "No speech could be recognized"
    else:
        output = "Cancelled"
    return output

def get_immersive_reader_token():
    payload = {'Ocp-Apim-Subscription-Key': keys.keys['IR_key'],'content-type': 'application/x-www-form-urlencoded'}
    resp = requests.post(keys.keys['IR_ENDPOINT'], headers=payload)
    return resp.text

def get_key_words():
    """
    Grab the key words from the text.txt file
    """
    ob = open("text.txt", "r")
    text = ob.read()
    ob.close()
    documents = { "documents": [
            { "id": "1", "text": text}

        ] }

    region = "eastus"
    keyword_key = keys.keys['keyword_key']
    headers   = {"Ocp-Apim-Subscription-Key": keyword_key}
    response  = requests.post(keys.keys['keyword_url'], headers=headers, json=documents)
    keywords = response.json()
    return json.dumps(keywords['documents'][0]['keyPhrases'])

