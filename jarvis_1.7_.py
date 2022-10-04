# Teaching Jarvis (and Friday) to speak news, and crack jokes, and predict weather.

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from PyDictionary import PyDictionary
import my_news
import jokes
import send_mail

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
print(voice)

engine.setProperty('voice', voice[0].id)
# This sets the pace at which the AI speaks. initially, it is 200.
engine.setProperty('rate', 150)

###### JARVIS SPECIFIC FUNCTIONS (start) ######

def speak(audio):
    print("JARVIS :", audio)
    print()
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning.")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon.")

    else:
        speak("Good evening.")

    speak("How may I be of service to you ?")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"USER : {query}\n")

    except Exception as e:
        print(e)
        speak("Could you kindly say that again please ?")
        return "None"

    return query

###### JARVIS SPECIFIC FUNCTIONS (end) ######

###### MULTIPLE TASKS THAT JARVIS CAN PERFORM (start) ######

# NOTES
def take_notes() :
    speak("Start saying what you want to write.")
    txt = takeCommand()
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y --- %H:%M:%S")
    txt = dt_string + "\n" + "-----------------------\n" + txt + \
        "\n-----------------------\n-----------------------\n"
    with open("notes_by_jarvis.txt", "a") as fp:
        fp.write(str(txt))
    speak("Successfully noted.")

# EMAIL
def mail_someone():
    speak("Who do you want to mail ?")
    receiver_email = input("Enter the email of recipient :")
    speak("What do you want to say ?")
    message = takeCommand()
    send_mail.send_email(receiver_email, message)
    speak("Mail sent.")

# NEWS
def tell_news():
    speak("Alright...")
    my_news.read_news(
        "My name is Friday and I will be reading out today's news, in Jarvis's place.")
    my_news.main()
    speak("Thankyou Friday !")
    speak("Awaiting your next command")

# GOOGLE SEARCH
def google_search():
    speak("Kindly Repeat your search query again ?")
    query = takeCommand()
    speak("Alright.. This may take some time.")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# WEATHER
def get_weather():
    speak("What is the name of the city or place ?")
    city = takeCommand()
    speak("Alright.. This may take some time.")
    webbrowser.open(f"https://www.google.com/search?q=weather+in+{city}")

# JOKE
def tell_joke():
    speak("Friday usually cracks better jokes than me.")
    jokes.read_joke(
        "Alright jarvis, let me entertain the user in your place.")
    while (True):
        jokes.read_joke("Here you go ->")
        jokes.main()
        jokes.read_joke("Do you want to hear one more ?")
        response = takeCommand()
        if ("yes" in response or "of course" in response or "sure" in response or "yeah" in response or "okay" in response or "one more" in response):
            pass
        else:
            jokes.read_joke(
                "Thank you for your time, hope you enjoyed my jokes.")
            break

# WIKI SEARCH
def wiki_search():
    speak("Searching Wikipedia...")
    user_command = user_command.replace("wikipedia", "")
    search_wiki = user_command.replace("search", "")
    results = wikipedia.summary(search_wiki, sentences=2)
    speak("According to Wikipedia : ")
    speak(results)

# YOUTUBE SEARCH
def youtube_search():
    speak("Please repeat your query again.")
    song_name = takeCommand().lower()
    speak("Searching...")
    url = "https://www.youtube.com/results?search_query="
    lst = song_name.split()
    for q in lst:
        url = url + q + "+"
    webbrowser.get('chrome').open(url)  # Opening via chrome.
    speak("Here you go...")

# PLAY GAME
def play_game():
    path = "retro_pong.py"
    os.startfile(path)

###### MULTIPLE TASKS THAT JARVIS CAN PERFORM (end) ######

webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe")) # Use your own file path here.

if __name__ == "__main__":

    WishMe()
    user_command = ""
    while ("quit" or "stop" or "terminate" not in user_command):

        user_command = takeCommand().lower()

        if('what is' in user_command or 'what' in user_command):
            if('date' in user_command or 'time' in user_command):
                time = datetime.datetime.now().strftime("%H:%M:%S")
                date = datetime.date.today()
                x = datetime.datetime(date.year, date.month, date.day)
                month = x.strftime("%B")
                day = int(x.strftime("%d"))
                year = x.strftime("%Y")
                speak(f"Today is {month} - {day}, {year}")
                speak(f"And, the present time is {time}")

            elif ('meaning' in user_command or 'definition' in user_command or 'meant by' in user_command):
                speak("Kindly repeat the word of which you want to know the meaning of.")
                word = takeCommand().lower()
                dict = PyDictionary()
                meaning = dict.meaning(word)
                res = not bool(meaning)
                if res == False:
                    for key in meaning:
                        speak(
                            f"If {word} is used as a {key}, then, it could mean ....")
                        for item in meaning[key]:
                            speak(item)
                else:
                    speak("Sorry, I don't know the meaning of that word.")

            elif ('weather' in user_command or 'climate' in user_command or 'forecast' in user_command):
                get_weather()

            elif ('news' in user_command or 'headline' in user_command or 'headlines' in user_command):
                tell_news()

            else :
                wiki_search()
        
        elif('open' in user_command or 'launch' in user_command):
            if('code' in user_command):
                path = "C:\\Users\\Soumyadev\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # Enter your own file path here.
                os.startfile(path)

            elif('chrome' in user_command):
                speak("Executing.. This might take a few seconds.")
                webbrowser.get('chrome').open("")  # Opening via chrome.

            elif('youtube' in user_command):
                webbrowser.get('chrome').open(
                        "https://www.youtube.com/") # Opening via chrome.

            elif('whatsapp' in user_command):
                speak("Executing.. This might take a few seconds.")
                # Opening via chrome.
                webbrowser.get('chrome').open("web.whatsapp.com")

            else :
                speak("Sorry, I am unable to open that.")
        
        elif('who are you' in user_command or 'what are you' in user_command or 'identify yourself' in user_command or 'your name' in user_command or 'idertify' in user_command):
            speak("My name is JARVIS, I was created using python, by Soumyadev Saha.")

        elif ('who is' in user_command):
            wiki_search()

        elif ('search' in user_command):
            if ('wiki' in user_command or 'wikipedia' in user_command):
                wiki_search()

            else:
                google_search()
        
        elif ('watch' in user_command or 'see' in user_command or 'view' in user_command):
            if ('picture' in user_command or 'image' in user_command or 'photo' in user_command or 'view' in user_command):
                google_search()
            else:
                youtube_search()

        elif ('play' in user_command or 'listen' in user_command or 'hear' in user_command):
            if('joke' in user_command or 'funny' in user_command):
                tell_joke()

            elif('game' in user_command):
                play_game()

            else :
                youtube_search()

        elif ('tell' in user_command or 'say' in user_command or 'read' in user_command):
            if('joke' in user_command or 'funny' in user_command):
                tell_joke()

            elif('weather' in user_command or 'climate' in user_command or 'forecast' in user_command):
                get_weather()

            elif('news' in user_command or 'headline' in user_command):
                tell_news()
                
            else :
                google_search()
        
        elif ('send' in user_command):
            if('mail' in user_command or 'email' in user_command):
                mail_someone()

            else :
                speak("Sorry, I am unable to send that.")
        
        elif ('note' in user_command or 'write' in user_command or 'remember' in user_command):
            take_notes()

        elif ('terminate' in user_command or 'stop' in user_command or 'quit' in user_command or 'exit' in user_command or 'bye' in user_command or 'shutdown' in user_command):
            break

        elif(user_command) :
            speak("Sorry, I am missing that command from my database. Please try again.")

    speak("Alright... Thanks for conversing with me !")
    speak("Don't just have a good day. Have a great day !")
