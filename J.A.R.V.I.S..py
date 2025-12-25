import webbrowser
import os
import random
import platform
import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import sys
import time
import subprocess  # Import subprocess

# Predefined lists for various interactions
daddy_words = [
    "dad", "daddy", "papa", "pops", "father", "daddy", "da", "dada", "pop", "pa", "baba"
]

mom_words = [
    "mom", "mommy", "mama", "mum", "mummy", "ma", "mother", "momma", "mam", "mamma", "mammy", "mumsy",
]

boss_addresses = [
    "sarbish Chaudhary", "mr. Chaudhary", "sarbish Sir", "boss Chaudhary", "sir Chaudhary"
]

ai_addresses = [
    "boss", "sir", "master", "owner", "create", "mantor", "creator"
]

greeting_variations = [
    "Hello boss, how can I help you?", "Hi boss, what can I do for you?", "Greetings boss, how may I assist you?",
    "Hello sir, how can I assist you today?", "Hey boss, what do you need?", "Welcome back boss, how may I help?",
    "Hello sir, what can I do for you today?", "Hi boss, I’m ready. How can I assist?", "Good day boss, how may I serve you?",
    "Boss, I’m here. How can I help?"
]

stop_words = [
    "exit", "quit", "stop", "end", "terminate", "halt", "close", "shut up",
    "pause", "abort", "cease", "cancel", "desist", "hold", "quiet", "shutdown",
    "finish", "break", "leave", "retreat", "freeze", "peace", "cutoff"
]

song_actions = [
    "play", "start", "listen", "turn on", "begin", "press play", "launch",
    "activate", "trigger", "stream", "put on", "hit play", "cue", "fire up",
    "play music", "start music", "unleash", "spin the track", "drop the beat"
]

farewell_messages = [
    "Goodbye, sir! Always happy to help!", "Take care, sir! At your service anytime!",
    "Farewell, sir! I’m always here if you need me!", "Bye, sir! Ready to assist whenever you need!",
    "See you, sir! Happy to be of service anytime!", "Catch you later, sir! Here whenever you need me!",
    "Goodbye, sir! Have a great day ahead!", "Take care, sir! I’ll be waiting for your next command!",
    "Goodbye, sir! It’s a pleasure serving you!", "Farewell, sir! Until we meet again!"
]

names_variations = [
    "name", "Full name", "First name", "Last name", "Surname", "Nickname", "Alias", "Username", "Handle", "Title", "you"
]

voice_assistant_variations = [
    "I’m Jarvis, your voice assistant, sir!", "Jarvis at your service, your voice assistant, sir!",
    "Hello, I’m Jarvis, here to assist you, sir!", "I’m Jarvis, your personal voice assistant, sir!",
    "Jarvis, your assistant, ready to help, sir!", "I’m Jarvis, here to assist with your voice commands, sir!",
    "Your voice assistant, Jarvis, at your service, sir!", "I’m Jarvis, your AI-powered assistant, sir!",
    "Call me Jarvis, your helpful assistant, sir!", "Jarvis, your voice assistant, is here, sir!"
]

# Initialize pyttsx3 engine
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        listener.pause_threshold = 1
        audio = listener.listen(source)
    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print(f"🗣️ You said: {command}")
    except sr.UnknownValueError:
        print("❌ Sorry, I didn't understand that. Please try again.")
        return take_command()
    except sr.RequestError:
        print("❌ Could not request results, check your internet connection.")
        return ""
    return command

def tell_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    talk(f"The time is {current_time}")
    print(f"🕒 {current_time}")

def tell_date():
    current_date = datetime.datetime.now().strftime('%Y-%B-%d')
    talk(f"Today is {current_date}")
    print(f"📅 {current_date}")

def tell_day():
    current_day = datetime.datetime.now().strftime('%A')
    talk(f"Today is {current_day}")
    print(f"☾𖤓 {current_day}")

def open_chrome():
    talk("Opening the chrome, sir!")
    if platform.system() == "Windows":
        os.system("start chrome")
    elif platform.system() == "Linux":
        os.system("google-chrome &")
    else:
        talk("Sorry sir, I cannot open Chrome on this OS.")

def open_firefox():
    talk("Opening the firefox, sir!")
    if platform.system() == "Windows":
        os.system("start firefox")
    elif platform.system() == "Linux":
        os.system("firefox &")
    else:
        talk("Sorry sir, I cannot open Firefox on this OS.")

def open_facebook():
    talk("Opening Facebook, sir!")
    if platform.system() == "Linux":
        webbrowser.get("google-chrome").open("https://www.facebook.com")
    elif platform.system() == "Windows":
        webbrowser.get("windows-default").open("https://www.facebook.com")

def open_youtube():
    talk("Opening YouTube, sir!")
    if platform.system() == "Linux":
        webbrowser.get("google-chrome").open("https://www.youtube.com")
    elif platform.system() == "Windows":
        webbrowser.get("windows-default").open("https://www.youtube.com")

# Corrected open_user_folder function with lowercase input handling
def open_user_folder(folder):
    folder = folder.lower()  # Convert folder input to lowercase
    
    home_dir = os.path.expanduser("~")
    folder_path = os.path.join(home_dir, folder)

    if os.path.isdir(folder_path):  # Check if it's a valid directory
        if platform.system() == "Windows":
            subprocess.run(["explorer", folder_path])  # Open folder on Windows
        elif platform.system() == "Linux":
            subprocess.run(["xdg-open", folder_path])  # Open folder on Linux
        else:
            talk("Sorry, I cannot open this folder on your OS.")
            print("Sorry, I cannot open this folder on your OS.")
    else:
        talk("Folder not found.")
        print("Folder not found.")

def play_song(command):
    for action in song_actions:
        if action in command:
            song = command.replace(action, "").strip()
            if song:
                talk(f"Playing {song}")
                pywhatkit.playonyt(song)
            else:
                talk("Sorry sir, I couldn't catch the song name.")
            return True
    return False

def run_assistant():
    try:
        command = take_command()
        if not command:
            return

        if play_song(command):
            return

        elif "time" in command:
            tell_time()

        elif "date" in command:
            tell_date()

        elif "day" in command:
            tell_day()
        
        elif "chrome" in command:
            open_chrome()

        elif "firefox" in command:
            open_firefox()

        elif "facebook" in command:
            open_facebook()

        elif "youtube" in command:
            open_youtube()

        elif "open folder" in command or "folder" in command:
            talk("Which folder do you want to open, sir?")
            folder = take_command()  # Take folder name input
            if folder:
                open_user_folder(folder)  # Open the folder in lowercase
            else:
                talk("Sorry, I couldn't hear the folder name.")

        elif any(word in command for word in stop_words):
            talk(random.choice(farewell_messages))
            print(random.choice(farewell_messages))
            sys.exit()

        else:
            talk("Sorry, I didn't understand that.")

    except Exception as e:
        talk("Sorry, something went wrong!")
        print(e)

def change_voice():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

def restart_assistant():
    talk("Restarting the assistant...")
    time.sleep(2)
    main()

def main():
    global engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)

    change_voice()

    talk(random.choice(greeting_variations))  # Ensure greeting_variations is properly defined
    while True:
        run_assistant()

if __name__ == "__main__":
    main()
