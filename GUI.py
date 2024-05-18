from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
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


#ask fun
def ask():
    user_val=speech_to_text.speech_to_text()
    bot_val=action.Action(user_val)
    text.insert(END,'User--->'+user_val+'\n')
    if bot_val!=None:
        text.insert(END,"BOT<---"+str(bot_val)+"\n")
    if bot_val=="OK sir":
        root.destroy()
    print('hi')

def send():
   send=entry.get()
   bot=action.Action(send)
   text.insert(END,'User--->'+send+"\n")
   if bot!=None:
      text.insert(END,"BOT<---"+str(bot)+"\n")
   if bot=="OK sir":
        root.destroy()



def delete():
    text.delete('1.0',"end")








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

#adding some text to root

text=Text(root, font=("courier 10 bold"),bg="#605E65")
text.grid(row=2,column=0)
text.place(x=110,y=505,width=400,height=70)


#entry widget
entry=Entry(root,justify=CENTER)
entry.place(x=110 ,y=590,width=400 ,height=30)



#3 button
Button1 =Button(root,text="ASK",bg="#605E65",pady=16,padx=40,borderwidth=0,relief=SOLID,command=ask)
Button1.place(x=70,y=650)


Button2 =Button(root,text="SEND",bg="#605E65",pady=16,padx=40,borderwidth=0,relief=SOLID,command=send)
Button2.place(x=250,y=650)

Button3=Button(root,text="DELETE",bg="#605E65",pady=16,padx=40,borderwidth=0,relief=SOLID,command=delete)
Button3.place(x=430,y=650)

root.mainloop()
