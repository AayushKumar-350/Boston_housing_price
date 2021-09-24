import pyttsx3                                                                               # Used to Recognise the voice
import datetime
import speech_recognition as sp
import wikipedia
import webbrowser
import os
import numpy as np                                                                               # importing to play music randomly

engine = pyttsx3.init("sapi5")                                                               # (about it in Documents)
voice = engine.getProperty("voices")                                                         # provides two types of avalible voice in API (Male and Female)
#print(voice[0].id)
engine.setProperty("voices",voice[0].id)

def speak(audio):                                                                           #For speaking the provided audio
    engine.say(audio)
    engine.runAndWait()

def Wish():                                                                                  #For greeting
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak("HEY GOOD MORNING")
    elif (hour>=12 and hour<18):
        speak("HEy GOOD AFTER NOON")
    else:
        speak("HEY GOOD EVENING")
    speak("So How may I help you my lord")

def Commands():                                                                     # "speechRecognition" takes input from the microphone and gives a string Output
    r =sp.Recognizer()                                                              # we also  install PyAudio Library
    with sp.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 2
        audio=r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio,language="en-in")
        print("User Said: ",query)
    except Exception as e:
        print("Please say it again")
        return "NONE"
    return query


if __name__ == "__main__":
    Wish()
    exit_condition=False
    while not exit_condition:
        query=Commands().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia", "")
            result = wikipedia.summary(query,sentences=1)
            speak("According to the wikipedia")
            print("According to the wikipedia:\n ",result)
            speak(result)

        elif "open youtube" in query:
            speak("Opening Youtube..")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Opening GOOGLE..")
            webbrowser.open("google.com")

        elif "music" in query:
            speak("Playing Song for you..")
            music_dir = "F:\\Music"
            song = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,song[np.random.randint(len(song))]))            #used numpy module to import random song

        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("It's ",time)

        elif "exit" in query:
            exit_condition = True
