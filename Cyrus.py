from asyncore import ExitNow
from calendar import month
from cgitb import text
from distutils import command
from distutils.log import info
from imghdr import what
from importlib.resources import path
from logging.config import listen
from operator import truediv
import re
import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr #pi
import pywhatkit 
import wikipedia
import pyjokes
import webbrowser
import os
 
 
 
engine = pyttsx3.init()
 
 
 
def speak (audio):
    engine.say(audio)
    engine.runAndWait()
 
 
 
 
def time():
    time = datetime.datetime.now().strftime("%I %M:%p")
    speak(time)
 
 
def date ():
    year= int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date= int(datetime.datetime.now().day)
 
    speak(date)
    speak(month)
    speak(year)
 
def hour ():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <12 :
        speak("good morning sir")
    elif hour >=12 and hour <16:
        speak("good afternoon sir")
    elif hour >=16 and hour <19:
        speak("good evening sir")
    else:
        speak ("Good nit sir")
 
 
def whishme():
    hour()
    speak("the current time is")
    time ()
    speak("the current month")
    date()
    speak("jarvis at your service, how can i help you")
 
 
 
speak(" hi . this is cyrus")
speak("Initializing cyrus")
speak("Starting all systems applications")
speak("Installing and checking all drivers")
speak("Caliberating and examining all the core processors")
speak("Checking the internet connection")
speak("Wait a moment sir")
speak("All drivers are up and running")
speak("All systems have been activated")
speak("Now I am online")
hour()
speak("cyrus at your service,how could i help you sir")
 
 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("listenting......")
        r.pause_threshold = 1
        audio = r.listen(source)
 
    try:
        print ("Recognizing.......")
        command = r.recognize_google(audio,language  ='en-in')
        if "cyrus" in command:
            command = command.replace("cyrus","")
            print(command)
 
 
    except Exception as e:
        print(e)
       
 
        return "None"
    return command
 
 
def work():
    command = takecommand()
    if "play" in command:
        song = command.replace("play","")
        speak("playing" +song)
        pywhatkit.playonyt(song)
        print(command)
    elif "who is" in command:
        person = command.replace("who is","")
        info = wikipedia.summary(person,2)
        print(info)
        speak(info)
       
    elif "time " in command:
         print(command)
         time ()

    elif "hi" in command:
        speak("Hi  this is cyrus ,you look soo pretty, how can i help you" )
        print(speak)
 
    elif" date" in command:
         print(command)
         date()
 
    elif "about yourself" in command:
        print(command)
        speak("Hi iam cyrus, my boss mister Pradeep kumar , i am his voice assistant, i love to help him")
        print(speak)
 
    elif "joke" in command:
        print(command)
        speak(pyjokes.get_joke())
        print(speak)
 
    elif "about me" in command:
        print(command)
        speak(" you are good person, you nice to me, you will reach your goals high,")
 
    elif "love" in command:
        print(command)
        speak("To breed a healthy relationship with your wife or girlfriend, you must feed the love and affection between you and your lover")
        speak("One of the simplest yet most efficient ways of doing this is through sweet words of affirmation")
        speak("It’s amazing how a quick text or a well-crafted message can have so much impact on someone")
        speak("By sending romantic messages, you not only keep your relationship vibrant but also reassure your partner of your never-ending love")
       
   
 
    elif "moment" in command:
        print (command)
        whishme()
 
    elif "search " in command:
        command = command.replace("search","")
        text= "https://www.google.co.in/search?q="
        search_command = text + command
        webbrowser.open(search_command)
        speak("searching" + command)
 
    elif "note" in command:
        print(command)
        os.system("notepad")
 
    elif "music" in command:
        print(command)
        os.system("spotify")
 
    elif "file" in command:
        print(command)
        os.system("explorer.exe")
 
    elif "thank you" in command:
        print("Thank you")
        speak("its my pleasure to work for you boss")
        exit()
 
   
    else:
        speak("say that again please")
       
while True:
    work()
 

