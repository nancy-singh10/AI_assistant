import speech_recognition as sr
from tkinter import *

def speech_to_text(root):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    text.insert("Let's speak!!")
    
    try:
        # Use the microphone as source for input
        with sr.Microphone() as source:
            print("Adjusting for ambient noise, please wait...")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            
            print("Recording for 5 seconds...")
            audio_data = recognizer.record(source, duration=5)
            
            print("Recognizing your text.............")
            text = recognizer.recognize_google(audio_data)
            print("You said: " + text)
            return text
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand your audio")
        return "error"

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "error"


