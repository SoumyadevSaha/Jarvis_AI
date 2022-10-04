import requests
import json
def read_news(str) :
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice") #Creates a Dispatch based COM object.
    speak.Voice = speak.GetVoices().Item(1) # Item(1) is for female voice, default and Item(0) is for male voice.
    print("FRIDAY : " + str + "\n")
    speak.Speak(str)
    
def main() :
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=221a4d722ef1468aa94e9ac9157c4f85"
    news = requests.get(url).text
    news_obj = json.loads(news) # Creating a object news; converts news text to a dictionary,
    art = news_obj ["articles"]
    read_news("Listing relevant headlines for today : ")
    k = 0
    for item in art :
        read_news(item["source"]["name"] + " says : ")
        read_news(item["title"])
        read_news("Moving on to the next news headline : ")
        k += 1
        if k == 5 :
            break

    read_news("That's it for today.")
    read_news("Thank you for your time. Have a great Day !")

if __name__ == "__main__" :
    main()