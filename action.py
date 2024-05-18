import text_speech
import speech_to_text
import datetime
import webbrowser
import weather
import openai


def Action(data):
    user_data=data.lower()
    if "what is your name" in user_data:
        text_speech.text_to_speech("My name is Nano your personnel assistant owned by Nancy Singh")
        return "My name is Nano your virtual assistant"
    elif "what you can do" or "what you do" or "what can you do" or "how can you help me" in user_data:
        text_speech.text_to_speech("At present, I'm equipped to perform specific tasks like displaying the current time, directing you to websites like Google, YouTube, and music streaming platforms, and providing updates on the current weather conditions in Delhi.")
        return "At present, I'm equipped to perform specific tasks like displaying the current time, directing you to websites like Google, YouTube, and music streaming platforms, and providing updates on the current weather conditions in Delhi."
    elif "hello" in user_data or "hye" in user_data:
        text_speech.text_to_speech("hey, Maam How i can help you")
        return "hey, Maam How i can help you"
    elif "good morning" in user_data:
        text_speech.text_to_speech("good morning Maam")
        return "good morning Maam"
    elif "time" in user_data:
        current_time=datetime.datetime.now()
        Time=(str)(current_time)+"Hour: ",str(current_time.minute)+"Minute"
        text_speech.text_to_speech(Time)
        return Time
    elif "shutdown" in user_data:
        text_speech.text_to_speech("Ok Maam")
        return "OK Maam"
    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_speech.text_to_speech("gaaana.com is now ready for you")
        return "gaaana.com is now ready for you"
    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com.com/")
        text_speech.text_to_speech("youtube.com is now ready for you")
        return  "youtube.com is now ready for you"
    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_speech.text_to_speech("googleaaana.com is now ready for you")
        return "googleaaana.com is now ready for you"
    elif "weather" in user_data:
        ans=weather.weather()
        text_speech.text_to_speech(ans)
        return ans


    else:
        text_speech.text_to_speech("Sorry ,I'm not able to understand") 
        return "Sorry,I'm not able to understand"