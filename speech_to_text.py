import speech_recognition as sr
import speech_recognition as sr
import pyaudio


def speech_to_text():

    init_rec = sr.Recognizer()
    print("Let's speak!!")
    with sr.Microphone() as source:
        audio_data = init_rec.listen(source)
        print("Recognizing your text.............")
        text = init_rec.recognize_google(audio_data)
        print(text)
        return text
    # except sr.UnknownValueError:
    #     print("Google Speech Recognition could not understand your audio")
    # except sr.RequestError as e:
    #     print("Could not request results from Google Speech Recognition service; {0}".format(e))

speech_to_text()