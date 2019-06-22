import azure.cognitiveservices.speech as speechsdk
import keys




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


if __name__ == "__main__":

    output = get_text()
    print(output)
