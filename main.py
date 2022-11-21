# Import Modules:
import pyttsx3 
import speech_recognition as sr 
import wikipedia # --> To interact with your wIkipedia
import webbrowser # --> To search across web.
import os # --> To interact with your operating system
import smtplib 
from youtubesearchpython import Search # --> To search something on youtube.
import datetime # --> For date & time.
from AppOpener import run


# Voice Initialization:
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

# voice[0].id --> Male Voice.
# voice[1].id --> Feale Voice.

# Functions:

def speak(audio):
    # This Function speaks the input value.

    engine.say(audio)
    engine.runAndWait()

def greeting():
    # This Function greets the user.

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Hussain")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Hussain")   

    else:
        speak("Good Evening Hussain")

    speak("I am Jarvis Sir. How may I help you")       



def listen():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing your command...")    
        query = r.recognize_google(audio)
        print(f"You said: {query}\n")

    except Exception as e:
        print("Please say again...")  
        return "None"

    return query

def search(query):
    # This function search user commands on internet.
    speak(f'Searching')
    query = query.replace('search', '')
    webbrowser.open(query)

def website(query):
    # This function opens the website user wants.
    speak(f'Openning')
    query = query.replace('open', '')
    query = query.replace(' ', '')
    try:
        run(query)
    except:
        searchItem = f'{query}.com'
        webbrowser.open(searchItem)


def wiki(query):
    # This function fetch the information from wikipedia.
    speak('Searching Wikipedia...')
    print('Searching Wikipedia...')
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences = 3)
    speak('According to wikipedia..')
    print(results)
    speak(results)


def sendMail():
    pass

def dateTime():
    pass

# Main Program
if __name__ == "__main__":

    # greeting()
    while True:

        query = listen().lower() # --> Take command and convert it into lower case string.

        # Logic of performing tasks:

        # Open some website:
        if 'open' in query:
            website(query)

        # Search something on Internet:
        elif 'search' in query:
            search(query)

        # Search something on wikipedia:
        elif 'wikipedia' in query:
            wiki(query)

        elif 'exit' or 'quit' in query:
            speak("Exiting... Thankyou for using my services.")
            print("Exiting... Thankyou for using my services.")
            exit()
        
