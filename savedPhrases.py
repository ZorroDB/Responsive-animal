from ast import keyword
from distutils.log import error
import string
import speech_recognition as sr


def main():
    r = sr.Recognizer()
    keyword = 'yo'

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something.. \n")

        audio = r.listen(source)

        try:
            if r.recognize_google(audio) == keyword:
                print("Hello!")

            elif r.recognize_google(audio) is not keyword:
                print("Didn't recognize a word... :(")

            print("--------- \n")

            print("You have said \n" +
                  r.recognize_google(audio, language="en-us"))

        except Exception as e:
            print("Error : " + str(e))

        with open("recordedaudio.wav", "wb") as f:
            f.write(audio.get_wav_data())


if __name__ == "__main__":
    main()
