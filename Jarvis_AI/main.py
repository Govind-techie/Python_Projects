# Jarvis AI:


import speech_recognition as sr # Here, we mentioned that the speech_recognition (Short Form : sr).
import webbrowser # Its a built in module.
import pyttsx3
import musicplaylist
import requests

if __name__ == "__main__":
    pass

recognizer = sr.Recognizer() # Captures and processes user input via voice. # It intialize the speech_recognition and creates a recognizer class.
engine = pyttsx3.init() # Responds back to the user using synthesized speech.
news_api = "826c2e2635f14442918d2c4da9fca1ae"
google_search_api = "AIzaSyAHGnwxJngFnhTbWbTYyKMyGL8_6W_2Y4g"
def speak(text): # Here, is a function speak that takes a text parameter.
    engine.say(text) # Here, we use the engine.say function which say the text in form of an audio.
    engine.runAndWait() # Here, we it runs the engine and it wait.  

def ProcessCommand(c):
    print(f"Processing command: {c}")  # Debug print
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open chat gpt" in c.lower():
        webbrowser.open("https://chat.openai.com")
    elif "today's news headlines" in c.lower():
        try:
            get_request = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}")
            data = get_request.json()
            if "articles" in data:
                headlines = data["articles"]
                for article in headlines:
                    speak(article["title"])
            else:
                speak("No articles found")
        except Exception as e:
            speak("Sorry, I couldn't fetch the news")
            print(f"News error: {str(e)}")
    elif "search" in c.lower():
        try:
            words = c.lower().split()
            search_query = " ".join(words[1:])
            cx = "92d6665d5823c4522"
            base_url = f"https://www.googleapis.com/customsearch/v1?q={search_query}&key={google_search_api}&cx={cx}"
            
            response = requests.get(base_url)
            response.raise_for_status()
            results = response.json().get('items', [])
            
            if results:
                title = results[0]['title']
                link = results[0]['link']
                speak(f"Here is what I found: {title}")
                speak(f"Click here to read the full article: {link}")
                print(f"Full Article: {link}")
            else:
                speak("No results found.")
        except Exception as e:
            speak("Sorry, I couldn't perform the search")
            print(f"Search error: {str(e)}")
    
    elif c.lower().startswith("play"):
        songs = " ".join(c.lower().split(" ")[1:])
        link = musicplaylist.music.get(songs)
        if link:
            webbrowser.open(link)
        else:
            speak("Song is not in the musicplaylist")

speak("Initializing Jarvis....")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            print("Processing...")
        
        word = recognizer.recognize_google(audio)
        print(f"Heard: {word}")  # Debug print
        
        if word.lower() == "jarvis":
            speak("Hello sir, how can I assist you")
            with sr.Microphone() as source:
                print("Listening for command...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                ProcessCommand(command)
                
    except sr.WaitTimeoutError:
        continue
    except sr.UnknownValueError:
        print("Could not understand audio")
        continue
    except sr.RequestError as e:
        print(f"Could not request results: {str(e)}")
        continue
    except Exception as e:
        print(f"Error: {str(e)}")
        continue

    