from email.mime import audio
from logging.config import listen
from tkinter import CENTER, LEFT
import speech_recognition as sr
import turtle
import time
import requests

from config import API_KEY

api_key = API_KEY  # Enter the API key you got from the OpenWeatherMap website
base_url = "http://api.openweathermap.org/data/2.5/weather?"


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
    if "what is the weather" in querry:
        city_name = input("Enter city name : ")
        # This is to complete the base_url, you can also do this manually to checkout other weather data available
        complete_url = base_url + "appid=" + \
            'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]

            current_temperature = y["temp"]
            z = x["weather"]

            weather_description = z[0]["description"]

            print(" Temperature = " +
                  str(current_temperature) +
                  "\n description = " +
                  str(weather_description))

        else:
            print(" City Not Found ")

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
