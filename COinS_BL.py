#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Programm, das Metadaten via COinS aus dem KOBV Portal liest und die bibliographischen Angaben ausgibt.
...
authors: Beata Lakenberg, Sebastian Scherübl, Claus Werner
license: MIT License
version: 1.0
date: 2026-07-06
"""




import requests
import sys
from sys import argv
from bs4 import BeautifulSoup
from urllib.parse import parse_qs

DEBUG=True


# Liest COinS-Metadaten von einer KOBV-Titelseite aus. Der Link zur Titelseite wird von nutzer angegeben
def kobv_abfrage (kataloglink):

#Prüfen, ob die Verbindung funktioniert:
    try:
        response = requests.get(url=kataloglink)
    except Exception as e:
         print(f"\nFehler in der Verbindung:\n{e}")
         sys.exit(1)
    #Wenn die Fehlermeldung kommt, kann es an folgenden liegen: Server ist nicht erreichbar; kein Internet;URL ist falsch geschrieben

    # Statuscode prüfen, wenn Fehlermeldung kommt, kann es an folgenden liegen: Seite nicht gefunden (404); Zugriff verweigert (403); Serverfehler (500)
    if response.status_code != 200:
        print("Fehler! Statuscode:", response.status_code)
        sys.exit(1)

    if DEBUG:
        print("URL:", response.url)
        print("Statuscode:", response.status_code)

    # Sicherstellen, dass die Antwort als UTF-8 dekodiert wird
    response.encoding = response.apparent_encoding

def parse_results (html_inhalt):
    #liest COinS-Metadaten aus der HTML aus.
    soup = BeautifulSoup(html_inhalt, "html.parser") #BeautifulSoup macht HTML durchsuchbar
    print(html_inhalt[:2000])  #Prüft ob KOBV überhaupt sinnvolle HTML-Daten zurückschickt. Nur zum Testen

    alle_coins = soup.find_all("span", class_="Z3988") #Findet alle Elemente, die Name "span" und Klasse "Z3988" haben
    print(len(alle_coins)) #Gibt alle gefundene COinS aus

    #for coins in alle_coins:

    """print("Autor:     ", autor.text if autor is not None else "-")
    print("Titel:     ", titel.text if titel is not None else "nicht vorhanden")
    print("ISSN:      ", isbn.text if isbn is not None else "nicht vorhanden")
    print("Seiten:", herausgeber.text if herausgeber is not None else "-") """


# Menü
if __name__ == "__main__":
    kataloglink = input("Bitte geben Sie ein Link zum Exemplar an: ")
    kobv_abfrage(kataloglink)


