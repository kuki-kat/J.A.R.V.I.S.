import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

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

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)

    elif "your name" in command:
        talk("I am your voice assistant, Jarvis!")

    elif "stop" in command or "bye" in command:
        talk("Goodbye! Have a great day!")
        exit()

    else:
        talk("I didn't quite get that. Could you repeat?")

talk("Hello boss, I am your voice assistent. How can I help you boss ?")
while True:
    run_assistant()
