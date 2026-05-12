import os
import requests
import time
from termcolor import colored
import subprocess
import sys
os.system('cls' if os.name == 'nt' else 'clear')
print(colored("Czekanie na zamknięcie głównego programu", "yellow"))
time.sleep(3)
print(colored("Program zamknięty, uruchamianie aktualizacji", "green"))

# Lista plików do aktualizacji (ścieżki w repo i lokalnie)
FILES = [
    "CMD-Browser.py",
    "updater.py",
    "img.py",
    "logo.png",
    "test.py",
    "version.txt"
]

GITHUB_RAW_BASE = "https://raw.githubusercontent.com/szymon4github/CMD-Browser/main/"

APP_FOLDER = os.path.dirname(os.path.abspath(__file__))

def get_latest_version():
    r = requests.get(GITHUB_RAW_BASE + "version.txt")
    return r.text.strip()

def get_current_version():
    with open(os.path.join(APP_FOLDER, "version.txt"), "r") as f:
        return f.read().strip()

def update_file(file_name):
    url = GITHUB_RAW_BASE + file_name
    r = requests.get(url)
    if r.status_code == 200:
        with open(os.path.join(APP_FOLDER, file_name), "wb") as f:
            f.write(r.content)
    else:
        print(f"Błąd pobierania {file_name}: {r.status_code}")

def update_app():
    for file_name in FILES:
        update_file(file_name)
    print(colored("Aktualizacja zakończona sukcesem!", "green"))

if __name__ == "__main__":
    current = get_current_version()
    latest = get_latest_version()
    print(f"Twoja wersja: {current}, najnowsza: {latest}")
    if latest != current:
        update_app()
        print(colored("Uruchamienie z powrotem głównego programu!", "green"))
        time.sleep(3)
        subprocess.Popen(["python", "CMD-Browser.py"])
        sys.exit()
    else:
        print("Masz najnowszą wersję!")
