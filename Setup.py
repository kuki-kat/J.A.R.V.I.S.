import subprocess
import platform

if platform.system() == "Linux":
    subprocess.run(["sudo", "apt", "install", "-y", "portaudio19-dev"])
    print("portaudio19-dev installed successfully")
    subprocess.run(["sudo", "apt", "install", "-y", "python3-tk"])
    print("python3-tk installed successfully")
    subprocess.run(["sudo", "apt", "install", "-y", "python3-dev"])
    print("python3-dev installed successfully")
else:
    print("This script is for Linux only")
