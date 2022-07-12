import random


def read_joke(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")  # Creates a Dispatch based COM object.
    # Item(1) is for female voice, default and Item(0) is for male voice.
    speak.Voice = speak.GetVoices().Item(1)
    print("FRIDAY : " + str + "\n")
    speak.Speak(str)


def main():
    lst = []
    with open("joke.txt", "r") as fp:
        lst = fp.readlines()
    r = random.randint(0, len(lst)-1)
    read_joke(lst[r])


if __name__ == "__main__":
    main()
