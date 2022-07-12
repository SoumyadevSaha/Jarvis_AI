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

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
print(voice)

engine.setProperty('voice', voice[0].id)
# This sets the pace at which the AI speaks. initially, it is 200.
engine.setProperty('rate', 150)


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


if __name__ == "__main__":

    WishMe()
    user_command = ""
    while ("quit" not in user_command):

        user_command = takeCommand().lower()

        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))

        if ('wikipedia' in user_command):
            speak("Searching Wikipedia...")
            user_command = user_command.replace("wikipedia", "")
            search_wiki = user_command.replace("search", "")
            results = wikipedia.summary(search_wiki, sentences=2)
            speak("According to Wikipedia : ")
            speak(results)
        elif ('weather' in user_command or 'climate' in user_command) :
            path = "D:\\DEVELOPMENT\\My_Projects\\Python_Project\\Weather app\\weather.py"
            os.startfile(path)
            speak("Enter the name of your city in the widget to know current weather.")
        elif ('open' in user_command or 'view' in user_command or 'watch' in user_command or 'see' in user_command or 'show' in user_command):

            if ('youtube' in user_command.lower()):
                speak("Executing.. This might take a few seconds.")
                # Opening via chrome.
                webbrowser.get('chrome').open("youtube.com")

            elif ('anime' in user_command):
                speak("Executing.. This might take a few seconds.")
                if ('schedule' in user_command):
                    webbrowser.get('chrome').open("livechart.me")
                    speak("Here you go...")
                else:
                    webbrowser.get('chrome').open("animixplay.to")
                    speak("Tano-shin-de kuda-sai...")

            elif ('hotstar' in user_command or 'disnep' in user_command or 'movie' in user_command):
                speak("Executing.. This might take a few seconds.")
                # Opening via chrome.
                webbrowser.get('chrome').open("hotstar.com/in/")
                speak(
                    "Search for the movie you want to watch in the top-right search bar.")
                speak("Enjoy !")

            elif ('scenery' in user_command):
                speak("Executing.. This might take a few seconds.")
                # Opening via chrome.
                webbrowser.get('chrome').open(
                    "https://unsplash.com/s/photos/beautiful-scenery")

            elif ('landscape' in user_command):
                speak("Executing.. This might take a few seconds.")
                # Opening via chrome.
                webbrowser.get('chrome').open(
                    "https://www.google.com/search?q=nice+landscapes&rlz=1C1CHBD_enIN954IN954&hl=en&sxsrf=AOaemvKXVdwnjE2hSfQJe-uNgpn1tdwHrw:1632413977588&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj4oIr6v5XzAhVFmuYKHc7ZCPMQ_AUoAXoECAEQAw&biw=1366&bih=625&dpr=1")

            elif ('picture' in user_command or 'image' in user_command):
                pic_dir = "D:\\Pictures"
                pic = os.listdir(pic_dir)
                r = random.randint(0, len(pic)-1)
                os.startfile(os.path.join(pic_dir, pic[r]))

            elif ('whatsapp' in user_command):
                speak("Alright.")
                speak("Executing.. This might take a few seconds.")
                # Opening via chrome.
                webbrowser.get('chrome').open("web.whatsapp.com")

            elif ('google' in user_command or 'tab' in user_command):
                speak("Executing.. This might take a few seconds.")
                webbrowser.get('chrome').open("")  # Opening via chrome.

            elif ('facebook' in user_command):
                speak("Alright.")
                speak("Executing.. This might take a few seconds.")
                # Opening via chrome.
                webbrowser.get('chrome').open("facebook.com")
            elif ("code" in user_command or "visual studio" in user_command or "vs" in user_command):
                path = "C:\\Users\\Soumyadev\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)

            elif ("java" in user_command):
                path = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.2.3\\bin\\idea64.exe"
                os.startfile(path)

            elif ("video" in user_command):
                vid_dir = "D:\Videos"
                videos = os.listdir(vid_dir)
                r = random.randint(0, len(videos)-1)
                os.startfile(os.path.join(vid_dir, videos[r]))
            else:
                speak(
                    "Sorry, unable to execute, that command is missing from my matrix.")

        elif ("listen" in user_command or "hear" in user_command or "play" in user_command):

            if ("song" in user_command):

                if ("english" in user_command):
                    speak("Alright.")
                    speak("Executing.. This might take a few seconds.")
                    # Opening via chrome.
                    webbrowser.get('chrome').open(
                        "https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLhsz9CILh357zA1yMT-K5T9ZTNEU6Fl6n")
                elif ("hindi" in user_command):
                    speak("Alright.")
                    speak("Executing.. This might take a few seconds.")
                    # Opening via chrome.
                    webbrowser.get('chrome').open(
                        "https://www.youtube.com/watch?v=_cPHiwPqbqo&list=PL9bw4S5ePsEF-J_tIORZ6xE_OXkGuKjjY")
                else:
                    speak("Please tell the name of the song you want to hear.")
                    song_name = takeCommand().lower()
                    speak("Searching...")
                    url = "https://www.youtube.com/results?search_query="
                    lst = song_name.split()
                    for q in lst:
                        url = url + q + "+"
                    webbrowser.get('chrome').open(url)  # Opening via chrome.
                    speak("Here you go...")
            # playing music from directory.
            elif ("music" in user_command or "audio" in user_command):
                if ("light" in user_command):
                    music_dir = "D:\\Music\\Soft -jazz from Ambar"
                    songs = os.listdir(music_dir)
                    r = random.randint(0, len(songs)-1)
                    os.startfile(os.path.join(music_dir, songs[r]))
                else:
                    music_dir = "D:\\Music\\Music store downloads\\A Sense of Adventure 25 Fantastic Tracks for Endless Imaginations"
                    songs = os.listdir(music_dir)
                    r = random.randint(0, len(songs)-1)
                    os.startfile(os.path.join(music_dir, songs[r]))
            elif ("video" in user_command):
                vid_dir = "D:\Videos"
                videos = os.listdir(vid_dir)
                r = random.randint(0, len(videos)-1)
                os.startfile(os.path.join(vid_dir, videos[r]))
            else:
                speak(
                    "Sorry, unable to execute, that command is missing from my matrix.")

        # Meaning of a word.
        elif ("meaning of" in user_command or "meant by" in user_command or "mean by" in user_command):
            speak("Kindly repeat the word of which you want to know the meaning of.")
            word = takeCommand().lower()
            dict = PyDictionary()
            # meaning of "python"
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

        elif ("search" in user_command or "what is" in user_command):
            if ("news" in user_command or "headline" in user_command):
                speak("Alright...")
                my_news.read_news(
                    "My name is Friday and I will be reading out today's news, in Jarvis's place.")
                my_news.main()
                speak("Thankyou Friday !")
                speak("Awaiting your next command")
            else:
                speak("Kindly repeat you search query again")
                srch = takeCommand().lower()
                url = "https://www.google.com/search?q="
                lst = srch.split()
                for q in lst:
                    url = url + q + "+"
                webbrowser.get('chrome').open(url)
                speak("Here you go..")
        elif ("stop" in user_command or "shut" in user_command):
            user_command = user_command + " quit"

        elif ("date" in user_command or "time" in user_command):
            time = datetime.datetime.now().strftime("%H:%M:%S")
            date = datetime.date.today()
            x = datetime.datetime(date.year, date.month, date.day)
            month = x.strftime("%B")
            day = int(x.strftime("%d"))
            year = x.strftime("%Y")
            speak(f"Today is {month} - {day}, {year}")
            speak(f"And, the present time is {time}")
        elif ("who are you" in user_command or "your name" in user_command or "who is your" in user_command or "who created you" in user_command or "you identity" in user_command):
            speak("My name is JARVIS, and I was created by Sou-mya-dev Saha.")
        # elif ("what can you do" or "commands" in user_command) :
        #     speak("I can do the following : ")
        #     os.startfile("jarvis_cmd.txt")
        elif ("read" in user_command or "tell" in user_command or "say" in user_command):
            if ("joke" in user_command or "funny" in user_command):
                speak("Alright... ")
                speak("Friday usually cracks better jokes than me.")
                jokes.read_joke(
                    "Alright jarvis, let me entertain the user in your place.")
                while (True):
                    jokes.read_joke("Here you go ->")
                    jokes.main()
                    jokes.read_joke("Do you want to hear one more ?")
                    response = takeCommand()
                    if ("yes" in response or "ofcourse" in response or "sure" in response or "yeah" in response or "okay" in response or "one more" in response):
                        pass
                    else:
                        jokes.read_joke(
                            "Thankyou for your time, hope you enjoyed my jokes.")
                        break
            elif ("news" in user_command or "headline" in user_command):
                speak("Alright...")
                my_news.read_news(
                    "My name is Friday and I will be reading out today's news, in Jarvis's place.")
                my_news.main()
                speak("Thankyou Friday !")
                speak("Awaiting your next command")
            else:
                speak("Sorry, unable to read.")
        elif ('write' in user_command or 'note' in user_command):
            speak("Start saying what you want to write.")
            txt = takeCommand()
            now = datetime.datetime.now()
            dt_string = now.strftime("%d/%m/%Y --- %H:%M:%S")
            txt = dt_string + "\n" + "-----------------------\n" + txt + \
                "\n-----------------------\n-----------------------\n"
            with open("notes_by_jarvis.txt", "a") as fp:
                fp.write(str(txt))
            speak("Successfully noted.")

    speak("Alright... Thanks for conversing with me !")
    speak("Don't just have a good day. Have a great day !")
