import random
import platform
import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import sys
import time

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
    "Goodbye, sir! Always happy to help!",
    "Take care, sir! At your service anytime!",
    "Farewell, sir! I’m always here if you need me!",
    "Bye, sir! Ready to assist whenever you need!",
    "See you, sir! Happy to be of service anytime!",
    "Catch you later, sir! Here whenever you need me!",
    "Goodbye, sir! Have a great day ahead!",
    "Take care, sir! I’ll be waiting for your next command!",
    "Goodbye, sir! It’s a pleasure serving you!",
    "Farewell, sir! Until we meet again!"
]


names_variations = [
    "name",
    "Full name",
    "First name",
    "Last name",
    "Surname",
    "Nickname",
    "Alias",
    "Username",
    "Handle",
    "Title"
]
voice_assistant_variations = [
    "I’m Jarvis, your voice assistant, sir!",
    "Jarvis at your service, your voice assistant, sir!",
    "Hello, I’m Jarvis, here to assist you, sir!",
    "I’m Jarvis, your personal voice assistant, sir!",
    "Jarvis, your assistant, ready to help, sir!",
    "I’m Jarvis, here to assist with your voice commands, sir!",
    "Your voice assistant, Jarvis, at your service, sir!",
    "I’m Jarvis, your AI-powered assistant, sir!",
    "Call me Jarvis, your helpful assistant, sir!",
    "Jarvis, your voice assistant, is here, sir!"
]



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
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk(f"The time is {time}")
    print(f"🕒 {time}")

def tell_date():
    date = datetime.datetime.now().strftime('%Y-%B-%d')
    talk(f"Today is {date}")
    print(f"📅 {date}")

def tell_day():
    day = datetime.datetime.now().strftime('%A')
    talk(f"Today is {day}")
    print(f"☾𖤓 {day}")

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
        elif any(word in command for word in names_variations):
            talk(random.choice(voice_assistant_variations))
        elif any(word in command for word in stop_words):
            talk(random.choice(farewell_messages))
            print(random.choice(farewell_messages))
            sys.exit()
        else:
            talk("Sorry sir, I didn't understand that. Want me to add it?")
    except Exception as e:
        talk("Sorry sir, something went wrong over here!")
        print(e)

def change_voice():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    #talk("Switching to a female voice")

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

    talk("Hello boss, How can I help you?")
    while True:
        run_assistant()

if __name__ == "__main__":
    main()
