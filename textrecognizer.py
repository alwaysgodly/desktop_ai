import pyttsx3
import datetime
import webbrowser
import os
import random
import wikipedia

# Initialize text to speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# Function to get user input
def get_input():
    return input("How can I assist you? ").lower()

# Function to wish the user according to time
def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your desktop assistant. How can I help you?")

# Function to execute commands
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
    elif 'play music' in query:
        music_dir = 'C:\\Users\\Public\\Music'  # Change this directory to your music directory
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        else:
            speak("Sorry, no music files found.")
    elif 'search' in query:
        query = query.replace('search', '')
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif 'wikipedia' in query:
        query = query.replace('wikipedia', '')
        try:
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple options. Can you please be more specific?")
        except wikipedia.exceptions.PageError as e:
            speak("Sorry, I couldn't find any relevant information.")
    elif 'exit' in query or 'quit' in query:
        speak("Goodbye! Have a nice day.")
        exit()
    else:
        speak("I'm sorry, I didn't understand that.")

# Main function
if __name__ == "__main__":
    wish_me()
    while True:
        query = get_input()
        execute_command(query)







