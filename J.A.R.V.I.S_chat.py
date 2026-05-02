import webbrowser
import os
import random
import platform
import datetime
import subprocess
from openai import OpenAI

# ----- AI SETUP (SECURE) -----

client = OpenAI(
    api_key="API",
    base_url="https://api.groq.com/openai/v1"
)

# ----- CONFIG -----

STOP_WORDS = ["exit", "quit", "stop", "end", "terminate", "halt", "close"]
SONG_ACTIONS = ["play", "start", "listen", "turn on", "begin", "stream"]

GREETINGS = [
    "Hello boss, how can I help you?",
    "Hi boss, what can I do for you?",
    "Greetings boss, how may I assist you?"
]

# ----- AI RESPONDER -----

def ask_ai(question):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a smart personal assistant named JARVIS."},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        print("🤖", answer)

    except Exception as e:
        print("⚠️ AI Error:", e)

# ----- TIME / DATE -----

def tell_time():
    print("🕒 The time is", datetime.datetime.now().strftime('%I:%M %p'))

def tell_date():
    print("📅 Today is", datetime.datetime.now().strftime('%Y-%B-%d'))

def tell_day():
    print("📅 Today is", datetime.datetime.now().strftime('%A'))

# ----- BROWSER / APPS -----

def open_website(url, name="Website"):
    print(f"Opening {name}...")
    webbrowser.open(url)

def open_app(app_name):
    print(f"Opening {app_name}...")
    system = platform.system()

    try:
        if system == "Windows":
            os.system(f"start {app_name}")
        elif system == "Linux":
            subprocess.Popen([app_name])
        else:
            print("Unsupported OS")
    except Exception:
        print("⚠️ Could not open app.")

# ----- FILE SYSTEM -----

def open_user_folder(folder):
    home_dir = os.path.expanduser("~")
    folder_path = os.path.join(home_dir, folder.lower())

    if os.path.isdir(folder_path):
        print(f"Opening folder: {folder}")
        if platform.system() == "Windows":
            subprocess.run(["explorer", folder_path])
        elif platform.system() == "Linux":
            subprocess.run(["xdg-open", folder_path])
    else:
        print("⚠️ Folder not found.")

# ----- MUSIC (NO PYWHATKIT) -----

def play_song(command):
    for action in SONG_ACTIONS:
        if command.startswith(action):
            song = command.replace(action, "").strip()
            if song:
                print(f"🎵 Playing {song} on YouTube...")
                query = song.replace(" ", "+")
                url = f"https://www.youtube.com/results?search_query={query}"
                webbrowser.open(url)
            else:
                print("⚠️ Please specify a song name.")
            return True
    return False

# ----- COMMAND HANDLER -----

def handle_command(command):
    command = command.lower().strip()

    if not command:
        return

    # EXIT
    if any(word in command for word in STOP_WORDS):
        print("👋 Goodbye boss!")
        exit()

    # MUSIC
    if play_song(command):
        return

    # TIME / DATE
    if "time" in command:
        tell_time()
    elif "date" in command:
        tell_date()
    elif "day" in command:
        tell_day()

    # WEBSITES
    elif "youtube" in command:
        open_website("https://www.youtube.com", "YouTube")
    elif "facebook" in command:
        open_website("https://www.facebook.com", "Facebook")
    elif "google" in command:
        open_website("https://www.google.com", "Google")

    # APPS
    elif "chrome" in command:
        open_app("google-chrome" if platform.system() == "Linux" else "chrome")
    elif "firefox" in command:
        open_app("firefox")

    # FOLDER
    elif "folder" in command:
        folder = input("📁 Which folder? ")
        open_user_folder(folder)

    # FALLBACK AI
    else:
        ask_ai(command)

# ----- MAIN LOOP -----

def run_chatbot():
    print("🤖", random.choice(GREETINGS))

    while True:
        try:
            command = input("💬 You: ")
            handle_command(command)

        except KeyboardInterrupt:
            print("\n👋 Interrupted. Goodbye!")
            break
        except Exception as e:
            print("⚠️ Error:", e)

# ----- RUN -----

if __name__ == "__main__":
    run_chatbot()
