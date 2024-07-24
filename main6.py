''''''''''''''''''''import pyttsx3
import datetime
import webbrowser
import os
import pyowm
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get user input
def get_input():
    return input("You: ").lower()

# Function to execute commands
def execute_command(query):
    query = query.lower()

    if 'time' in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"The current time is {current_time}")
        speak(f"The current time is {current_time}")

    elif 'search' in query:
        search_query = input("What do you want me to search for? ")
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        print(f"Here are the search results for {search_query}")
        speak(f"Here are the search results for {search_query}")

    elif 'weather' in query:
        city = input("Please tell me the city name: ")
        owm = pyowm.OWM('your-owm-api-key')
        observation = owm.weather_manager().weather_at_place(city)
        w = observation.weather
        temperature = w.temperature('celsius')['temp']
        status = w.status
        print(f"The temperature in {city} is {temperature} degrees Celsius and the weather is {status}")
        speak(f"The temperature in {city} is {temperature} degrees Celsius and the weather is {status}")

    elif 'joke' in query:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised!",
            "What do you call fake spaghetti? An impasta!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Parallel lines have so much in common. It’s a shame they’ll never meet."
        ]
        joke = random.choice(jokes)
        print(joke)
        speak(joke)

    elif 'open' in query:
        if 'notepad' in query:
            os.system('notepad.exe')
        elif 'calculator' in query:
            os.system('calc.exe')
        elif 'browser' in query:
            webbrowser.open('https://www.google.com')
        else:
            print("Sorry, I can't open that application.")
            speak("Sorry, I can't open that application.")

    elif 'exit' in query:
        print("Goodbye!")
        speak("Goodbye!")
        exit()

    else:
        # Use NLTK to process the query
        tokens = word_tokenize(query)
        clean_tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]
        
        # Check for specific keywords or patterns in the input
        if 'who' in clean_tokens or 'what' in clean_tokens:
            print("Sorry, I don't have the answer to that question.")
            speak("Sorry, I don't have the answer to that question.")
        else:
            print("I'm not sure about that. Please repeat or try something else.")
            speak("I'm not sure about that. Please repeat or try something else.")

if __name__ == "__main__":
    speak("Hello! How can I assist you?")
    while True:
        query = get_input()
        if 'assistant' in query or 'hey' in query:
            execute_command(query)

