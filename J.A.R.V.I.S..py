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
import subprocess
from openai import OpenAI

# -------------------- API SETUP --------------------

client = OpenAI(
    api_key="API",  # 🔴 PUT YOUR GROQ API KEY HERE
    base_url="https://api.groq.com/openai/v1"
)

# -------------------- DATA --------------------

greeting_variations = [
    "Hello boss, how can I help you?",
    "Hi boss, what can I do for you?",
    "Greetings boss, how may I assist you?",
    "Welcome back boss!"
]

stop_words = [
    "exit", "quit", "stop", "end", "terminate", "halt", "close"
]

song_actions = [
    "play", "start", "listen", "begin", "launch", "stream"
]

farewell_messages = [
    "Goodbye, sir!",
    "Take care, sir!",
    "Shutting down, sir!"
]

# -------------------- SPEAK --------------------

def talk(text):
    engine.say(text)
    engine.runAndWait()

# -------------------- LISTEN --------------------

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        listener.pause_threshold = 1
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("🗣️ You:", command)
        return command

    except sr.UnknownValueError:
        print("❌ Didn't catch that...")
        return ""

    except sr.RequestError:
        print("❌ Internet issue...")
        return ""

# -------------------- AI --------------------

def ask_ai(question):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are Jarvis, a smart voice assistant."},
                {"role": "user", "content": question}
            ]
        )

        answer = response.choices[0].message.content
        print("🤖", answer)
        talk(answer)

    except Exception as e:
        print("AI Error:", e)
        talk("Sorry sir, I cannot connect to AI right now.")

# -------------------- FEATURES --------------------

def tell_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    talk(f"The time is {current_time}")
    print("🕒", current_time)

def tell_date():
    current_date = datetime.datetime.now().strftime('%Y-%B-%d')
    talk(f"Today is {current_date}")
    print("📅", current_date)

def tell_day():
    current_day = datetime.datetime.now().strftime('%A')
    talk(f"Today is {current_day}")
    print("📅", current_day)

def open_chrome():
    talk("Opening Chrome")
    if platform.system() == "Windows":
        os.system("start chrome")
    else:
        webbrowser.open("https://www.google.com")

def open_youtube():
    talk("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def open_facebook():
    talk("Opening Facebook")
    webbrowser.open("https://www.facebook.com")

def open_folder(folder):
    home = os.path.expanduser("~")
    path = os.path.join(home, folder.lower())

    if os.path.isdir(path):
        if platform.system() == "Windows":
            subprocess.run(["explorer", path])
        else:
            subprocess.run(["xdg-open", path])
    else:
        talk("Folder not found")

def play_song(command):
    for action in song_actions:
        if action in command:
            song = command.replace(action, "").replace("song", "").strip()
            if song:
                talk(f"Playing {song}")
                pywhatkit.playonyt(song)
            else:
                talk("Song name missing")
            return True
    return False

# -------------------- MAIN LOGIC --------------------

def run_assistant():
    command = take_command()

    if not command:
        return

    # SONG
    if play_song(command):
        return

    # TIME / DATE
    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "day" in command:
        tell_day()

    # OPEN APPS
    elif "chrome" in command:
        open_chrome()

    elif "youtube" in command:
        open_youtube()

    elif "facebook" in command:
        open_facebook()

    elif "folder" in command:
        talk("Which folder?")
        folder = take_command()
        if folder:
            open_folder(folder)

    # EXIT
    elif any(command.strip() == word for word in stop_words):
        msg = random.choice(farewell_messages)
        talk(msg)
        print(msg)
        sys.exit()

    # AI FALLBACK 🔥
    else:
        ask_ai(command)

# -------------------- SETUP --------------------

def main():
    global engine
    engine = pyttsx3.init()

    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    talk(random.choice(greeting_variations))

    while True:
        try:
            run_assistant()
        except Exception as e:
            print("Error:", e)
            talk("Something went wrong")

# -------------------- RUN --------------------

if __name__ == "__main__":
    main()