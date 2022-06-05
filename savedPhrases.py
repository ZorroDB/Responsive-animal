from email.mime import audio
from logging.config import listen
from tkinter import CENTER, LEFT
import speech_recognition as sr
import turtle
import time
import requests


# <------ TURTLE STYLING AND SETUP ---->

wn = turtle.Screen()
wn.title("Responsive test")
wn.bgcolor("grey")

# <------- AUDIO RESPONSIVE ------>


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        turtle.write("Waiting for command...", font=("Arial",
                                                     20, "normal"), align=CENTER)

        audio = r.listen(source)
    try:
        turtle.clear()
        turtle.write("Recognizing...", font=(
            "Arial", 20, "normal"), align=CENTER)
        query = r.recognize_google(audio, language='en')
        turtle.clear()
        turtle.write(f"You said: {query}", font=("Arial",
                                                 20, "normal"), align=CENTER)
        with open("recordedaudio.wav", "wb") as f:
            f.write(audio.get_wav_data())
    except Exception as e:
        return "none"
    query = query.lower()
    return query


def main():
    querry = takecommand()

    if "hello" in querry:
        turtle.clear()
        turtle.write("Hello Sir!", font=("Arial",
                                         20, "normal"), align=CENTER)
    else:
        pass
    if "goodbye" in querry:
        turtle.clear()
        turtle.write("Bye have a nice day", font=("Arial",
                                                  20, "normal"), align=CENTER)
    else:
        pass
    if "command list" in querry:
        time.sleep(2)
        turtle.clear()
        turtle.write("1. Hello", font=("Arial",
                                       20, "normal"), align=CENTER)
        time.sleep(3)
        turtle.clear()
        turtle.write("2. Goodbye", font=("Arial",
                                         20, "normal"), align=CENTER)
        time.sleep(3)
        turtle.clear()
        turtle.write("3. What is the weather", font=("Arial",
                                                     20, "normal"), align=CENTER)
        time.sleep(3)
        turtle.clear()
        turtle.write("4. Say 'Again' to repeat the list/ or say stop.", font=("Arial",
                                                                              20, "normal"), align=CENTER)

    if "again" in querry:
        turtle.write("1. Hello", font=("Arial",
                                       20, "normal"), align=CENTER)
        time.sleep(3)
        turtle.clear()
        turtle.write("2. Goodbye", font=("Arial",
                                         20, "normal"), align=CENTER)
        time.sleep(3)
        turtle.clear()
        turtle.write("3. What is the weather", font=("Arial",
                                                     20, "normal"), align=CENTER)
        time.sleep(3)
        turtle.clear()
    else:
        pass
    if "stop" in querry:
        turtle.clear()
        turtle.write("What is your command..")
        time.sleep(2)
        turtle.clear()
        takecommand()


if __name__ == "__main__":
    main()
    wn.mainloop()
