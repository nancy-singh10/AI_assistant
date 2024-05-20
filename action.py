import text_speech
import speech_to_text
import datetime
import webbrowser
import weather
import openai
import cookie

def Action(data):
    user_data = str(data).lower()
    print(user_data)

    if user_data == 'hye':
        text_speech.text_to_speech("Hey there!")
        return "Hey there!"
    
    if "what is your name" in user_data:
        response = "My name is Nano, your personal assistant owned by Nancy Singh"
        text_speech.text_to_speech(response)
        return response
    
    elif any(greeting in user_data for greeting in ["open web automation", "open","web","automation"]):
        ans = cookie.cookie()
        text_speech.text_to_speech("Opening Web Automation project")
        return "Opening Web Automation project"

    elif any(keyword in user_data for keyword in ["what you can do", "what you do", "what can you do", "how can you help me"]):
        response = ("At present, I'm equipped to perform specific tasks like displaying the current time, "
                    "directing you to websites like Google, YouTube, and music streaming platforms, and providing "
                    "updates on the current weather conditions in Delhi.")
        text_speech.text_to_speech(response)
        return response
    
    elif any(greeting in user_data for greeting in ["hello", "hye","hi"]):
        response = "Hey, Ma'am! How can I help you?"
        text_speech.text_to_speech(response)
        return response
    
    elif "good morning" in user_data:
        response = "Good morning, Ma'am!"
        text_speech.text_to_speech(response)
        return response
    
    elif "time" in user_data:
        current_time = datetime.datetime.now()
        Time = f"The current time is {current_time.hour} Hour and {current_time.minute} Minute"
        text_speech.text_to_speech(Time)
        return Time
    
    elif "shutdown" in user_data:
        response = "Ok, Ma'am"
        text_speech.text_to_speech(response)
        return response
    
    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        response = "gaana.com is now ready for you"
        text_speech.text_to_speech(response)
        return response
    
    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        response = "youtube.com is now ready for you"
        text_speech.text_to_speech(response)
        return response
    
    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        response = "google.com is now ready for you"
        text_speech.text_to_speech(response)
        return response
    
    elif "weather" in user_data:
        ans = weather.weather()
        text_speech.text_to_speech(ans)
        return ans
    
    elif "how are you" in user_data:
        response = "I am good, Ma'am. What about you?"
        text_speech.text_to_speech(response)
        return response
    
    else:
        response = "Sorry, I'm not able to understand"
        text_speech.text_to_speech(response)
        return response
