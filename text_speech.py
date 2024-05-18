import pyttsx3

def text_to_speech(text):
    
    engine= pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)    # Set the voice to the second voice (index 1)
    engine.setProperty('rate',120)
    engine.say(text)
    engine.runAndWait()


text_to_speech("Hey there! I'm your personal assistant Nano. How can I assist you today?")