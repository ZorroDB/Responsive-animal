from ast import keyword
from distutils.log import error
import string
import speech_recognition as sr
import turtle
import time

wn = turtle.Screen()
wn.title("Responsive test")
wn.bgcolor("grey")


def main():
    r = sr.Recognizer()
    keyword = 'hello'

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        turtle.write("I am all ears... \n")

        audio = r.listen(source)

        try:
            if r.recognize_google(audio) == keyword:
                turtle.write("Hello! \n")

            elif r.recognize_google(audio) is not keyword:
                turtle.write("I am sorry, I don't understand.. :(")

            turtle.write("You have said \n" +
                         r.recognize_google(audio, language="en-us"))

        except Exception as e:
            print("Error : " + str(e))

        with open("recordedaudio.wav", "wb") as f:
            f.write(audio.get_wav_data())


if __name__ == "__main__":
    main()
    wn.mainloop()
