import time
import os
try:
    import img
except:
    time.sleep(5)
    print("Brak wymaganych plików lub biblioteki colorama. Instalowanie bibliotek...")
    os.system("pip install colorama")
    
try:
        import pyfiglet
        from termcolor import colored
        
except:
    print("Brak wymaganych bibliotek. Instalowanie bibliotek...")
    os.system("pip install pyfiglet")
    os.system("pip install termcolor")
    time.sleep(5)
    exit()
os.system('cls' if os.name == 'nt' else 'clear')
tab = os.get_terminal_size()
enters = tab.lines
tab = tab.columns
max_page = enters - 4
ascii_banner = pyfiglet.figlet_format("CMD-Browser")
img.main("logo.png", 45)
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
print(colored(ascii_banner, "green"))
print(colored("Importowanie bibliotek:", "yellow"))
try:
    import timeit
except:
    print(colored("\t-timeit - instalowanie biblioteki", "red"))
    os.system("pip install timeit")
finally:
    print(colored("\t-timeit", "green"))
time.sleep(0.5)
try:
    from urllib.parse import urljoin
except:
    print(colored("\t-urllib - instalowanie biblioteki", "red"))
    os.system("pip install urllib")
finally:
    print(colored("\t-urllib", "green"))
time.sleep(0.5)
try:
    from PIL import Image
except:
    print(colored("\t-pillow - instalowanie biblioteki", "red"))
    os.system("pip install pillow")
print(colored("\t-pillow", "green"))
time.sleep(0.5)
try:
    import tempfile
except:
    print(colored("\t-tempfile - instalowanie biblioteki", "red"))
    os.system("pip install tempfile")
finally:
    print(colored("\t-tempfile", "green"))
time.sleep(0.5)
try:
    import bs4
except:
    print(colored("\t-bs4 - instalowanie biblioteki", "red"))
    os.system("pip install bs4")
finally:
    print(colored("\t-bs4", "green"))
time.sleep(0.5)
try:
    import requests
except:
    print(colored("\t-requests - instalowanie biblioteki", "red"))
    os.system("pip install requests")
finally:
    print(colored("\t-requests", "green"))
time.sleep(0.5)
try:
    import re
except:
    print(colored("\t-re - instalowanie biblioteki", "red"))
    os.system("pip install re")
finally:
    print(colored("\t-re", "green"))
time.sleep(0.5)

os.system('cls' if os.name == 'nt' else 'clear')
print(colored(ascii_banner, "green"))
print(colored("Definiowanie zmiennych", "yellow"))
print("\n")
print(pyfiglet.figlet_format("."), end="")
time.sleep(0.5)

headers = {
    'User-Agent': 'CMD-Browser/1.0',
    'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
}

os.system('cls' if os.name == 'nt' else 'clear')
print(colored(ascii_banner, "green"))
print(colored("Definiowanie zmiennych", "yellow"))
print("\n")
print(pyfiglet.figlet_format(". ."), end="")
time.sleep(0.5)

argv = False
os.system('cls' if os.name == 'nt' else 'clear')
print(colored(ascii_banner, "green"))
print(colored("Definiowanie zmiennych", "yellow"))
print("\n")
print(pyfiglet.figlet_format(". . ."), end="")
time.sleep(0.5)
pargv = None
time.sleep(0.5)

GITHUB_RAW_BASE = "https://raw.githubusercontent.com/szymon4github/CMD-Browser/main/"

APP_FOLDER = os.path.dirname(os.path.abspath(__file__))

def get_latest_version():
    r = requests.get(GITHUB_RAW_BASE + "version.txt")
    return r.text.strip()

def get_current_version():
    with open(os.path.join(APP_FOLDER, "version.txt"), "r") as f:
        return f.read().strip()

os.system('cls' if os.name == 'nt' else 'clear')

print("\n")
current = get_current_version()
latest = get_latest_version()
print(colored(f"Twoja wersja: {current}, najnowsza: {latest}", "yellow"))
if latest != current:
    print(colored("Dostępna aktualizacja. Uruchom updater.py, aby zaktualizować!", "yellow"))
else:
    print(colored("Masz najnowszą wersję!", "green"))

print(5*"\n")
print(colored(pyfiglet.figlet_format("Gotowe!"), "green"))
time.sleep(3)

os.system('cls' if os.name == 'nt' else 'clear')
try:
    while True:
        
        if argv == True:
            strona = str(pargv)
        else:
            ascii_banner = pyfiglet.figlet_format("CMD-Browser")
            img.main("logo.png", 30)
            print(colored(ascii_banner, 'green'))
            input()
            print(colored("Przeglądarka tekstowa w terminalu".center(tab), 'cyan'))
            print("\n")

            strona = input("Podaj adres strony: http://")

            if strona == "":
                google = input("Wyszukaj w wyszukiwarce: ")
                strona = f"http://bing.com/search?q={google}&ia=web"
            else:
                strona = f"http://{strona}"
        os.system('cls' if os.name == 'nt' else 'clear')
        ntab = int(tab / 3)
        print(colored(strona.center(tab), 'cyan'))
        print(colored("WCZYTYWANIE STRONY...".center(tab), 'yellow'))
        print(colored("━", "green") * ntab, 2*ntab*colored("━", "white"))
        time.sleep(1)
        try:
            page = requests.get(f"{strona}") #allow_redirects=False)
            
        except:
            print(colored("[BŁĄD] Nie udało się połączyć ze stroną.".center(tab), 'red'))
            
            page = requests.get(f"http://bing.com/search?q={strona}&ia=web")
            strona = f"http://bing.com/search?q={strona}&ia=web"
            time.sleep(2)
        ust = "import bs4,requests"
        timepage = timeit.timeit(stmt = f"requests.get('{strona}')", number=1, setup = ust)
        page.encoding = "utf-8"
        dane = bs4.BeautifulSoup(page.text, features="html.parser")
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(strona.center(tab), 'cyan'))
        print(colored("WYODRĘBNIANIE TEKSTU...".center(tab), 'yellow'))
        print(2*ntab*colored("━", "green"), ntab*colored("━", "white"))
        time.sleep(1)
        try:
            naglowek = dane.find("title")
            naglowek = naglowek.get_text()
        except:
            naglowek = strona
            print(colored("[BŁĄD] Nie udało się wyodrębnić tytułu strony.".center(tab), 'red'))
            time.sleep(2)
        try:
            linki = dane.find_all("a")
        except:
            linki = []
            print(colored("[BŁĄD] Nie udało się wyodrębnić linków ze strony.".center(tab), 'red'))
            time.sleep(2)
        try:
            imgs = dane.find_all('img')
        except:
            print(colored("[BŁĄD] Nie udało się wyodrębnić obrazów ze strony.".center(tab), 'red'))
            time.sleep(2)
        try:
            dane = dane.get_text()
            dane = str(dane)
            lines = dane.splitlines()
            LINK_REGEX = re.compile(r'href="(.+?)"')
        except:
            lines = []
            print(colored("[BŁĄD] Nie udało się wyodrębnić tekstu ze strony.".center(tab), 'red'))
            time.sleep(2)
        ascii_banner = pyfiglet.figlet_format(naglowek)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(strona.center(tab), 'cyan'))
        print(colored("GOTOWE...".center(tab), 'yellow'))
        print(colored("━"* tab, "green"))
        time.sleep(1)
        print(colored(ascii_banner.center(tab), 'cyan'))

        
        pages = 0
        for line in lines:
            time.sleep(0.01)
            stripped_line = line.strip()
            print(colored(stripped_line, "yellow").center(tab))
            pages = pages + 1
            if pages == max_page:
                input()
                pages = 0
        
        pages = 0
        for link in linki:
            time.sleep(0.01)
            print(colored(link.get_text(), "yellow"),end="".center(tab))
            znalezione_linki = LINK_REGEX.findall(str(link))
            print("-", colored(f"{znalezione_linki}\n\n","blue").center(tab))
            pages = pages + 3
            if pages == max_page:
                input()
                pages = 0

        lista_url = []
    
    # Znajdź wszystkie tagi <img>
        for img_tag in imgs:
            src = img_tag.get('src')
            
            if src:
                pelny_url = urljoin(strona, src)
                lista_url.append(pelny_url)
            
        for url in lista_url:
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            temp_filepath = temp_file.name
            temp_file.close()

            
            try:
                # 2. Pobieranie obrazu
                response = requests.get(url, stream=True)
                response.raise_for_status()
                with open(temp_filepath, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                

                imgs = Image.open(temp_filepath).convert('RGB')
                

                img.main(temp_filepath, tab)

                input()
                
            except requests.exceptions.RequestException as e:
                print(f"Błąd pobierania obrazu: {e}")
                
            except Exception as e:
                print(f"Wystąpił błąd podczas przetwarzania obrazu: {e}")
                
            finally:
                # 5. Usuwanie pliku tymczasowego (najważniejszy krok)
                if os.path.exists(temp_filepath):
                    os.remove(temp_filepath)

                        
                # Usuń duplikaty za pomocą zbioru (set), a potem przekształć z powrotem na listę


        print(colored(f"\n[CZAS ŁADOWANIA STRONY: {timepage} sekundy]".center(tab), 'green'))

        
        

        print("\n"*enters)

            



except requests.exceptions.ConnectionError as e:
    print("\n[BŁĄD POŁĄCZENIA]")
    print(f"Wystąpił problem z połączeniem lub rozpoznaniem nazwy hosta: {e}")
    print("Sprawdź poprawność adresu lub swoje połączenie internetowe.")
    time.sleep(5)
except KeyboardInterrupt:
    print("\n[WYJŚCIE] Przeglądarka została zamknięta przez użytkownika.")
    time.sleep(2)
except Exception as e:
    print(f"\n[INNY BŁĄD] Wystąpił nieoczekiwany błąd: {e}")
    time.sleep(5)

