from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import threading
import action
import text_speech

root = Tk()
# Change the title of the page
root.title("AI Assistant")
# Change to fixed size box
root.geometry("600x755")
# Fix the resize window
root.resizable(False, False)
# Background color
root.config(bg="#000000")

cnt = 0
#no
# Function to log messages to both terminal and Text widget
def log_message(message):
    print(message)  # Print to terminal
    output_text.insert(END, message + '\n')  # Insert into Text widget
    output_text.see(END)  # Auto-scroll to the end

def speech_to_text():
    recognizer = sr.Recognizer()
    log_message("startig speak task speak after RECORDING ")
    
    try:
        with sr.Microphone() as source:
            log_message("Adjusting for ambient noise, please wait...")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            
            log_message("Recording for 5 seconds...")
            audio_data = recognizer.record(source, duration=5)
            
            log_message("Recognizing your text.............")
            recognized_text = recognizer.recognize_google(audio_data)
            log_message("You said: " + recognized_text)
            process_user_input(recognized_text)
        
    except sr.UnknownValueError:
        log_message("Google Speech Recognition could not understand your audio")
        process_user_input("error")

    except sr.RequestError as e:
        log_message(f"Could not request results from Google Speech Recognition service; {e}")
        process_user_input("error")

def ask():
    threading.Thread(target=speech_to_text).start()

def process_user_input(user_val):
    global cnt
    if user_val == 'error' and cnt <= 2:
        cnt += 1
        text_speech.text_to_speech("I can't understand, try again")
    else:
        bot_val = action.Action(user_val)
        log_message('User ---> ' + user_val)
        if bot_val is not None:
            log_message("BOT <--- " + str(bot_val))
        if bot_val == "OK Ma'am":
            root.destroy()

def send():
    send_text = entry.get()
    log_message('User ---> ' + send_text)
    bot = action.Action(send_text)
    if bot is not None:
        log_message("BOT <--- " + str(bot))
    if bot == "OK Ma'am":
        root.destroy()

def delete():
    output_text.delete('1.0', "end")

# Frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#000000")
frame.grid(row=0, column=1, padx=95, pady=10)

# Text label
text_label = Label(frame, text="AI Assistant", font=("Comic Sans MS", 14, "bold"), bg="#605E65")
text_label.grid(row=0, column=0, padx=10, pady=10)

# Load and resize the image
image = Image.open("images/assistant3.png")
# Set the desired width and height for the image
desired_width = 250
desired_height = 350
image = image.resize((desired_width, desired_height), Image.LANCZOS)
image = ImageTk.PhotoImage(image)

# Image label
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

# Adding some text to root
output_text=Text(root,font=("courier 10 bold"),bg="#605E65")
output_text.grid(row=2,column=0)
output_text.place(x=110,y=505,width=400,height=70)

# Entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=110, y=590, width=400, height=30)

# Buttons
Button1 = Button(root, text="ASK", bg="#605E65", pady=16, padx=40, borderwidth=0, relief=SOLID, command=ask)
Button1.place(x=70, y=650)

Button2 = Button(root, text="SEND", bg="#605E65", pady=16, padx=40, borderwidth=0, relief=SOLID, command=send)
Button2.place(x=250, y=650)

Button3 = Button(root, text="DELETE", bg="#605E65", pady=16, padx=40, borderwidth=0, relief=SOLID, command=delete)
Button3.place(x=430, y=650)

root.mainloop()
