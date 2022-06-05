from email.mime import audio
import speech_recognition as sr
import turtle
import time


wn = turtle.Screen()
wn.title("Responsive test")
wn.bgcolor("grey")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        turtle.write("Waiting for command...(Hello)/(GoodBye)")
        audio = r.listen(source)
    try:
        turtle.write("Recognizing...")
        query = r.recognize_google(audio, language='en')
        turtle.write(f"You said: {query}")
        with open("recordedaudio.wav", "wb") as f:
            f.write(audio.get_wav_data())
    except Exception as e:
        return "none"
    query = query.lower()
    return query


def main():
    querry = takecommand()

    if "Hello" in querry:
        turtle.write("Hello Sir!")
    else:
        pass


if __name__ == "__main__":
    main()
    wn.mainloop()
