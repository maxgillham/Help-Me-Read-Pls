import azure.cognitiveservices.speech as speechsdk
import keys
import requests

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

if __name__ == "__main__":
    print(get_text())

