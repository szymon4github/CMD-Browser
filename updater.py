import os
import requests

# Lista plików do aktualizacji (ścieżki w repo i lokalnie)
FILES = [
    "CMD-Browser.py",
    "img.py",
    "logo.png",
    "test.py",
    "photo.png",
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
        print(f"{file_name} zaktualizowany!")
    else:
        print(f"Błąd pobierania {file_name}: {r.status_code}")

def update_app():
    for file_name in FILES:
        update_file(file_name)
    print("Aktualizacja zakończona! Uruchom ponownie aplikację.")

if __name__ == "__main__":
    current = get_current_version()
    latest = get_latest_version()
    print(f"Twoja wersja: {current}, najnowsza: {latest}")
    if latest != current:
        update_app()
    else:
        print("Masz najnowszą wersję!")
