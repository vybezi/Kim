import os
import re
import sys
import subprocess
from gtts import gTTS
from time import ctime
from datetime import datetime
import time
from playsound import playsound 
import pyaudio
import webbrowser
import random
from PyDictionary import PyDictionary 


CHROME = os.path.join('C:\\', 'Program Files (x86)', 'Google', 'Chrome', 'Application', 'chrome.exe')

i = 1
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en-uk')
    global i
    response = str("resources/kim/audio"+str(i)+".mp3")
    tts.save(response)
    playsound(response)
    i=i+1

def define(word):
    dictionary = PyDictionary()
    meaning = dictionary.meaning(word)
    if(meaning is None):
        return "I don't have that word, I'm sorry"
    else:
        definition = str(meaning)
        definition =definition.replace("[","")
        definition = definition.replace("]","")
        definition =definition.replace("'","")
        head, sep, tail = definition.partition(',')
        return(head)

#print(define("awesome"))



def listenFor(data):
    """Defining the functions to be carried out by personal assistant"""
    if re.search(r'\b(deactivate|quit)\b', data, re.I):
                print('Exiting..')
                speak("Ok hun, I'll talk to you later")
                sys.exit(0)
    
    if re.search(r'\b(what time is it)\b', data, re.I):
                t = time.ctime()
                f = datetime.strptime(t, '%a %b %d %H:%M:%S %Y')
                speak("The time is "+f.strftime('%H:%M'))

    if re.search(r'\b(how are you)\b', data, re.I):
                speak(f.strftime("I don't know, I have no feelings nor emotions"))
    
    if re.search(r'\b(what is your name|who are you)\b', data, re.I):
                speak("I'm Kim, your personal assistant")

    if re.search(r'\b(thanks|thank you)\b', data, re.I):
                speak("I'm just doing my job")
    
    if re.search(r'\b(launch lms)\b', data, re.I):
                psxmlgen = subprocess.Popen([r'C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe','-ExecutionPolicy','Unrestricted','./nculogin.ps1'], cwd=os.getcwd())
                result = psxmlgen.wait()
    

    if "Define" or "define" in data:
        data = data.split(" ")
        word = word = data[1]
        
        if(word=="Define" or word=="define"):
            word = data[2]

        print("Word is:" + word)
        speak(define(word))
        #definition = define(str(word))
        #speak("The definition for " + word + " is " + definition)

    
    if "where is" in data:
        data = data.split(" ")
        location = ""

        
        for x in range(2,len(data)):
            location += data[x]
            location +=" "
            
        
        speak("Hold on John, I will show you where " + location + " is.")
        url = "https://www.google.nl/maps/place/" + location + "/&amp;"
        webbrowser.open_new_tab(url)


intros= random.choice(("Good Day Sir, How may I help?","Nice to have you back sir, how may I help"))          
speak(intros)
