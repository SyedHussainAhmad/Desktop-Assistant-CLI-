'''Import Modules:'''
from datetime import datetime # --> For date & time.
import webbrowser # --> To search across web.
import wikipedia # --> To interact with your wIkipedia
from AppOpener import run, give_appnames # --> To run the app.
import speech_recognition as sr # --> For speech recognition
import pyttsx3 # --> Text to speech.


# Voice Initialization:
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

# voice[0].id --> Male Voice.
# voice[1].id --> Feale Voice.

# Functions:

def speak(audio):
    '''This Function speaks the input value.'''
    engine.say(audio)
    engine.runAndWait()

def greeting():
    '''This Function greets the user.'''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Hussain")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Hussain")

    else:
        speak("Good Evening Hussain")

    speak("I am Jarvis Sir. How may I help you")

def listen():
    ''' It takes microphone input from the user and returns string output'''
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing your command...")
        voice_command = recognizer.recognize_google(audio)
        print(f"You said: {voice_command}\n")

    except LookupError:
        print("Please say again...")
        return "None"

    return voice_command

def search(input_query):
    '''This function search user commands on internet.'''
    speak('Searching')
    input_query = input_query.replace('search', '')
    webbrowser.open(input_query)

def website(input_query):
    '''This function opens the apps user wants.'''
    speak('Openning')
    input_query = input_query.replace('open', '')
    run(input_query)

def wiki(input_query):
    '''This function fetch the information from wikipedia.'''
    speak('Searching Wikipedia...')
    print('Searching Wikipedia...')
    input_query = input_query.replace('wikipedia', '')
    results = wikipedia.summary(input_query, sentences = 3)
    speak('According to wikipedia..')
    print(results)
    speak(results)

def date():
    '''This function tells today's date.'''
    today_date = datetime.now().strftime("%B %d, %Y")
    print(f"today's date is {today_date}")
    speak(f"today's date is {today_date}")

def time():
    '''This function tells current time.'''
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Sir, the time is {current_time}")
    speak(f"Sir, the time is {current_time}")

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

        # Current Time:
        elif 'time' in query:
            time()

        # Todays's Date:
        elif 'date' in query:
            date()

        elif 'exit' or 'quit' in query:
            speak("Exiting... Thankyou for using my services.")
            print("Exiting... Thankyou for using my services.")
            exit()
