from multiprocessing.connection import Listener
from setuptools import Command
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

Listener= sr.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#engine.say("Hi I am your Alexaaa");
#engine.say("What can I do for you?")

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listning')
            voice=Listener.listen(source)
            command=Listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song= command.replace('play ' ,' ')
        talk('playing '+ song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        talk('Current time is '+time)
    
    elif 'tell me about ' in command:
        query= command.replace('tell me about ','')
        result=wikipedia.summary(query,sentences=2)
        print(result)
        talk(result)
    elif 'go for a date' in command:
        talk("Sorry I have headache")
    elif 'are you single' in command:
        talk("I am in relationship with wifi")
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
    else:
        talk("Sorry i couldn't understand")
        
while True:        
    run_alexa()