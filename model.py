import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# initialising the responding voice
engine = pyttsx3.init()
activatedvar = False
deactivatedvar = False
on = True

# Data
email_address = ""
password = ""

music_dir = "" # like "C:\\Users\\<user>\\Music'
ide_path = "" # for `open code editor` command


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
    server.login(email_address, password)
    server.sendmail(email_address, to, content)
    server.close()


    while True:
        query = takeCommand().lower()

        wish()
        speech("My name is David! How can I help you?")
        print("Welcome! My name is David, how can I help you?")

        if "exit" in query:
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
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speech(f"The time is {strTime}")

        elif "open code editor" in query:
            os.startfile(ide_path)

        elif "what is my age" in query:
            speech("please type in your Date of Birth!")
            print("please type in your Date of Birth!")
            dob = input("Date of Birth in DDMMYYYY format")
            dob = dob.strip(":")
            birthYear = dob[4:8]
            birthMonth = dob[2:4]
            birthDay = dob[0:2]
            today = datetime.date.today()
            thisYear = today.isoformat().strip("-")[0:4]
            age = int(thisYear) - int(birthYear)
            print("Your age is ", age)
            speech(f"your age is {age}")

        elif "thanks" in query or "thank you" in query:
            speech("Your most welcome!")

        elif "hello david" in query:
            speech("Yes, what should I do?")

        elif "send an email" in query:
            try:
                speech("To whom?")
                to = takeCommand()
                speech("What should I say?")
                content = takeCommand()
                speech("OK!")
                sendEmail(to, content)
                speech("Email has been sent!")
            except Exception as e:
                print(e)
                speech("Sorry the email couldn't be sent!")
