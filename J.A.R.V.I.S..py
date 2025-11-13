import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

stop_words = [
    "exit", "quit", "stop", "end", "terminate", "halt", "close", "shutup",
    "silence", "pause", "break", "abort", "cease", "discontinue", "retire",
    "kickoff", "shutdown", "giveup", "resign", "pullout", "freeze", "halted",
    "nope", "enough", "drop", "backoff", "cancel", "desist", "hold", "quiet",
    "standby", "disconnect", "logoff", "suspend", "finish", "wrapup", "stopit",
    "holdon", "cutit", "kill", "endit", "leave", "retreat", "bowout", "disband",
    "ceasefire", "breakoff", "stopnow", "haltplease", "pauseit", "shush",
    "hush", "bequiet", "zipit", "coolit", "knockitoff", "slowdown", "stepback",
    "dropit", "freezeup", "timeout", "endgame", "backout", "quitit", "peace",
    "calmdown", "letgo", "holdup", "noshouting", "stopthat", "desistplease",
    "finishup", "wrapthis", "closeup", "endthis", "haltoperation", "stopaction",
    "cutoff", "stall", "breaktime", "pausegame", "shutdownsystem", "killprocess",
    "endprocess", "haltprogram", "quitprogram", "stopsignal", "ceaseactivity",
    "terminateprocess", "stopmotion", "stopactivity", "breakactivity", "standdown",
    "poweroff", "stopsequence", "endsequence", "breaksequence", "haltsequence",
    "stopcommand", "terminatecommand", "quitcommand", "abortmission"
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
        print("❌ Sorry, I didn't understand that.")
        return ""
    return command

def run_assistant():
    command = take_command()
    if not command:
        return

    if "play" in command:
        song = command.replace("play", "")
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {time}")
        print(f"🕒 {time}")

    elif "date" in command:
        date = datetime.datetime.now().strftime('%Y-%B-%d')
        talk(f"Today is {date}")
        print(f"📅 {date}")

    elif "day" in command:
        day = datetime.datetime.now().strftime('%A')
        talk(f"Today is {day}")
        print(f"☾𖤓 {day}")

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)

    elif "your name" in command:
        talk("I am your voice assistant, Jarvis!")

    elif any(word in command for word in stop_words):
        talk("Bye sir! Any time at your service!")
        exit()

    else:
        talk("I am unable sir. Want me to add that?")

def main():
    global engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)

    talk("Hello boss, How can I help you?")
    while True:
        run_assistant()

if __name__ == "__main__":
    main()
