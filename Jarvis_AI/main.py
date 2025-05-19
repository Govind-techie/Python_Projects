# Import required libraries
import speech_recognition as sr  # For converting speech to text
import webbrowser  # To open URLs in the web browser
import pyttsx3  # For converting text to speech
import requests  # For sending HTTP requests (e.g., to fetch news or search results)
import musicplaylist  # Custom module (assumed) that contains a dictionary or method to get music URLs

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define API keys for news and Google Custom Search
NEWS_API = "826c2e2635f14442918d2c4da9fca1ae"  # NewsAPI key to fetch top headlines
GOOGLE_SEARCH_API = "AIzaSyAHGnwxJngFnhTbWbTYyKMyGL8_6W_2Y4g"  # Google Custom Search API key

# Function to convert text to speech
def speak(text):
    engine.say(text)  # Queue the text to be spoken
    engine.runAndWait()  # Speak the queued text

# Function to process user voice commands
def process_command(command):
    print(f"Processing command: {command}")  # Print the received command for debugging

    # If user says "open google", open the Google website
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    
    # If user says "open youtube", open YouTube
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    
    # If user says "open chat gpt", open ChatGPT website
    elif "open chat gpt" in command.lower():
        webbrowser.open("https://chat.openai.com")
    
    # If user asks for news, call the fetch_news function
    elif "today's news headlines" in command.lower():
        fetch_news()

    # If user says "search something", extract the query and perform a Google search
    elif "search" in command.lower():
        search(query=command)

    # If command starts with "play", assume user is requesting a song and play it
    elif command.lower().startswith("play"):
        play_music(command)

# Function to fetch and read out today's news headlines
def fetch_news():
    try:
        # API call to get top news headlines in India
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API}")
        data = response.json()

        # Check if news articles are found
        if "articles" in data:
            headlines = data["articles"]
            # Read each headline using text-to-speech
            for article in headlines:
                speak(article["title"])
        else:
            speak("No articles found.")
    except Exception as e:
        # If an error occurs, inform the user and print the error for debugging
        speak("Sorry, I couldn't fetch the news.")
        print(f"News error: {str(e)}")

# Function to search a query using Google Custom Search API
def search(query):
    try:
        words = query.lower().split()  # Split the command into words
        search_query = " ".join(words[1:])  # Remove "search" and take the actual query
        cx = "92d6665d5823c4522"  # Your Google Custom Search Engine ID

        # Construct the search URL using the API key, query and search engine ID
        base_url = f"https://www.googleapis.com/customsearch/v1?q={search_query}&key={GOOGLE_SEARCH_API}&cx={cx}"

        # Make the API request
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an error for bad HTTP status
        results = response.json().get('items', [])  # Extract search results

        # If results found, read out and print the top one
        if results:
            title = results[0]['title']
            link = results[0]['link']
            speak(f"Here is what I found: {title}")
            speak(f"Click here to read the full article: {link}")
            print(f"Full Article: {link}")
        else:
            speak("No results found.")
    except Exception as e:
        speak("Sorry, I couldn't perform the search.")
        print(f"Search error: {str(e)}")

# Function to play music based on voice command
def play_music(command):
    # Extract song name from command (e.g., "play Believer" => "believer")
    song_name = " ".join(command.lower().split(" ")[1:])
    link = musicplaylist.music.get(song_name)  # Get the link from musicplaylist module

    # If song found, open the link
    if link:
        webbrowser.open(link)
    else:
        speak("Song is not in the music playlist.")

# Main loop to listen for the keyword "Jarvis" continuously
def listen_for_commands():
    print("Listening for 'Jarvis'...")

    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Reduce background noise
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)  # Listen for 3 seconds
                word = recognizer.recognize_google(audio)  # Convert speech to text
                print(f"Heard: {word}")  # Debugging print

                # If the word "Jarvis" is heard, trigger assistant
                if word.lower() == "jarvis":
                    speak("Hello sir, how can I assist you?")
                    listen_for_command()

        # Handle common errors and keep listening
        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            print("Could not understand audio")
            continue
        except sr.RequestError as e:
            print(f"Could not request results: {str(e)}")
            continue

# Function to listen for an actual command after hearing "Jarvis"
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)  # Listen for full user command

        try:
            command = recognizer.recognize_google(audio)  # Convert speech to text
            print(f"Command received: {command}")  # Debugging print
            process_command(command)  # Process the spoken command
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except Exception as e:
            print(f"Error processing command: {str(e)}")

# Start the program by greeting the user and beginning the command loop
speak("Initializing Jarvis...")                 
listen_for_commands()