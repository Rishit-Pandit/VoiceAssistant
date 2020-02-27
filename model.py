import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# initialising the responding voice
engine = pyttsx3.init()
activated = False


def speech(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speech("Good morning!")
    elif hour >= 12 and hour < 18:
        speech("Good afternoon!")
    else:
        speech("Good evening!")


def activation():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        activate = r.recognize_google(audio, language="en-in").lower()
        if "hey david" in activate:
            activated = True
        elif "hello david" in activate:
            activated = True
        elif "ok david" in activate:
            activated = True
        elif "hi david" in activate:
            activated = True
        elif "listen david" in activate:
            activated = True

    except Exception as e:
        print(e)
        return "None"
        reactivation()

    return activated


def reactivation():
    activation()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Please say that again...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('rishit.pandit2@gmail.com', '123@Scientist')
    server.sendmail('rishit.pandit2@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wish()
    speech("My name is David! How can I help you?")
    print("Welcome! My name is David, how can I help you?")
    activated = activation()
    while activated:
        query = takeCommand().lower()

        if query == "exit":
            print("Shutting down...")
            speech("Shutting down! Thanks for using me!")
            break

        elif "wikipedia" in query:
            speech("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speech("According to wikipedia")
            print(results)
            speech(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open search engine" in query:
            webbrowser.open("duckduckgo.com")

        elif "open gmail" in query:
            webbrowser.open("mail.google.com")

        elif "play music" in query:
            musicDir = "C:\\Users\\rishit\\Music"
            songs = os.listdir(musicDir)
            print(songs)
            os.startfile(os.path.join(musicDir, songs[0]))

        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speech(f"The time is {strTime}")

        elif "open code" in query:
            codePath = "C:\\Users\\rishit\\Downloads\\VS Code\\code.exe"
            os.startfile(codePath)

        elif "open pycharm" in query:
            pycharmPath = "C:\\Users\\rishit\\Downloads\\PyCharm 2019.3.1\\PyCharm Community Edition 2019.3.1\\bin\\pycharm64.exe"
            os.startfile(pycharmPath)

        elif "open sublime text" in query:
            sublimePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(sublimePath)

        elif "what is my age" in query:
            speech("please type in your Date of Birth!")
            print("please type in your Date of Birth!")
            dob = input("Date of Birth in DD:MM:YYYY format")
            dob = dob.strip(":")
            birthYear = dob[4:8]
            birthMonth = dob[2:4]
            birthDay = dob[0:2]
            today = datetime.date.today()
            thisYear = today.isoformat().strip("-")[0:4]
            age = int(thisYear) - int(birthYear)
            print("Your age is ", age)
            speech(f"your age is {age}")

        elif "thanks" in query:
            speech("Your most welcome!")

        elif "thank you" in query:
            speech("You most welcome!")

        elif "hello david" in query:
            speech("Yes sir, what should I do?")

        elif "send an email" in query:
            try:
                speech("What should I say?")
                content = takeCommand()
                speech("OK!")
                to = "darshit.pandit10@gmail.com"
                sendEmail(to, content)
                speech("Email has been sent!")
            except Exception as e:
                print(e)
                speech("Sorry email can't be sent!")
    while activated != True:
        reactivation()
