import pyttsx3
import datetime
import webbrowser
import os
import random
import wikipedia
import speech_recognition as sr
import smtplib


engine = pyttsx3.init()


recognizer = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_input():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio).lower()
            print("You said:", query)
            return query
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you please repeat?")
            return get_input()
        except sr.RequestError:
            speak("Sorry, I'm unable to access the Google API. Please check your internet connection.")
            return ""


def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your desktop assistant. How can I help you?")


def execute_command(query):
    if 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'date' in query:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")
    elif 'open google' in query:
        webbrowser.open("https://www.google.com")
    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")
    elif 'open notepad' in query:
        os.system('notepad')
    elif 'send email' in query:
        speak("Who is the recipient?")
        recipient = get_input()
        speak("What should I say?")
        content = get_input()
        send_email(recipient, content)
    elif 'search' in query:
        query = query.replace('search', '')
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif 'wikipedia' in query:
        query = query.replace('wikipedia', '')
        try:
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            speak(result)
        except wikipedia.exceptions.DisambiguationError:
            speak("There are multiple options. Can you please be more specific?")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find any relevant information.")
    elif 'exit' in query or 'quit' in query:
        speak("Goodbye! Have a nice day")
        exit()
    else:
        speak("I'm sorry, I didn't understand that.")


def send_email(recipient, content):
    try:
       
        sender_email = "vyavaharepushkraj@gmail.com"
        sender_password = "thebigdog14"
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, content)
        server.close()
        speak("Email sent successfully!")
    except Exception as e:
        speak("Sorry, I couldn't send the email.")


if __name__ == "__main__":
    wish_me()
    while True:
        query = get_input()
        if query:
            execute_command(query)
