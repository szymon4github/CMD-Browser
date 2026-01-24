import os
from PIL import Image
import webcolors
import colorama
from colorama import Fore, Style # Zostawiamy termcolor, ale używamy colorama
colorama.init(autoreset=True)

# Zestaw znaków ASCII (jak poprzednio)
ASCII_CHARS = '@%#*+=━-:. '
CHAR_COUNT = len(ASCII_CHARS)

def rgb_to_256(r, g, b):
    """Konwertuje kolor RGB na najbliższą wartość w palecie 256 kolorów terminala."""
    try:
        # webcolors jest użyteczne do konwersji RGB na nazwę/wartość
        # Używamy prostego wzoru na 256 kolorów:
        return 16 + (r * 5 // 256) * 36 + (g * 5 // 256) * 6 + (b * 5 // 256)
    except Exception:
        # Awaryjnie zwraca kolor biały (kod 15)
        return 15 

def mapuj_jasnosc_na_znak(jasnosc):
    """Mapuje wartość jasności (0-255) na znak ASCII."""
    index = int((jasnosc / 255) * CHAR_COUNT)
    if index >= CHAR_COUNT:
        index = CHAR_COUNT - 1
    # Zwraca odwrócony znak (ciemne piksele to puste znaki)
    return ASCII_CHARS[~index]

def koloruj_znak(znak, color_256_code):
    """Generuje kod ANSI dla koloru 256-bitowego i dodaje znak."""
    # Format ANSI dla koloru foreground (tekstu): \033[38;5;[kod_koloru]m
    return f"\033[38;5;{color_256_code}m{znak}"

def obraz_na_ascii(sciezka_do_obrazu, szerokosc_docelowa):
    # ... (kod otwierania, skalowania i obliczania szerokości pozostaje taki sam)
    # Pamiętaj, aby go skopiować/przenieść z poprzedniej wersji.
    try:
        img = Image.open(sciezka_do_obrazu).convert('RGB')
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku pod ścieżką: {sciezka_do_obrazu}")
        return

    oryginalna_szerokosc, oryginalna_wysokosc = img.size
    ASPECT_RATIO_KOREKTA = 0.5
    nowa_wysokosc = int((oryginalna_wysokosc * szerokosc_docelowa / oryginalna_szerokosc) * ASPECT_RATIO_KOREKTA)
    img = img.resize((szerokosc_docelowa, nowa_wysokosc))
    
    ascii_output = []
    
    # Iteracja po pikselach
    for y in range(nowa_wysokosc):
        linia_ascii = []
        for x in range(szerokosc_docelowa):
            r, g, b = img.getpixel((x, y))
            
            # Obliczanie jasności
            jasnosc = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            
            # Mapowanie na znak
            znak = mapuj_jasnosc_na_znak(jasnosc)
            
            # Mapowanie na kod koloru 256
            kolor_kod = rgb_to_256(r, g, b)
            
            # Dodanie kolorowego znaku (nowa funkcja)
            linia_ascii.append(koloruj_znak(znak, kolor_kod))
            
        ascii_output.append("".join(linia_ascii) + Style.RESET_ALL) # Reset koloru na końcu linii
        
    # Wypisanie wyniku w terminalu
    print("\n" + "\u2550" * szerokosc_docelowa)
    print("\u2550" * szerokosc_docelowa)
    
    print("\n".join(ascii_output))


# --- Użycie ---
def main(sciezka, szerokosc=120):

    try:
        # Używamy stałej szerokości (bezpieczniejsza opcja)
        TERMINAL_WIDTH = szerokosc
    except Exception:
        TERMINAL_WIDTH = 120 

    obraz_na_ascii(sciezka, szerokosc_docelowa=TERMINAL_WIDTH)