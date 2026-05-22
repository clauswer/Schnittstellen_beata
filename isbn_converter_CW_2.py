#! /usr/bin/python3
 
# isbn_converter.py - Programm zum Konvertieren von ISBN-10 zu ISBN-13.
# Übernimmt eine ISBN-10 als Kommandozeilenparameter.
# Version 1.0, Autoren: Beata Lakenberg, Sebastian Scherübl, Claus Werner

import sys

# Fehlermeldungen
FEHLER_KEINE_PARAMETER = "Bitte eine ISBN-10 als Kommandozeilenparameter angeben."
FEHLER_ANZAHL_PARAMETER = "Bitte nur EINE ISBN-10 als Kommandozeilenparameter angeben."
FEHLER_ZEICHENMENGE = "ISBN darf nur Zeichen 0 bis 9, - und X (als letztes Zeichen) enthalten. Gefunden wurden aber auch: "
FEHLER_LAENGE = "ISBN muss 10 Zeichen (ohne '-') enthalten. Länge des übergebenen Wertes ohne '-' ist aber: "
FEHLER_ISBN10_NICHT_VALIDE = "Angegebene ISBN-10 ist nicht valide!"

# Zahl der Kommandozeilenparameter prüfen
if len(sys.argv) != 2:
    if len(sys.argv) > 2:
        print(FEHLER_ANZAHL_PARAMETER, file=sys.stderr)
    else:
        print(FEHLER_KEINE_PARAMETER, file=sys.stderr)
    exit(1)

# Übernahme der ISBN-10 über Kommandozeile
isbn10_input = sys.argv[1]

# Prüfe auf korrekte Zeichenmenge
list_error_char = set()

# Prüfen aller Zeichen außer letztem
for c in isbn10_input[:-1]:
    if c not in "0123456789-":
        list_error_char.add(c)

# Prüfen des letzten Zeichens
if isbn10_input[-1] not in "0123456789Xx":
    list_error_char.add(isbn10_input[-1])

if len(list_error_char) > 0:
    print(FEHLER_ZEICHENMENGE, " ".join(list_error_char), file=sys.stderr)
    exit(1)

# entfernen der Bindestriche
isbn10 = isbn10_input.replace("-", "")

# Prüfe auf korrekte Länge
if len(isbn10) != 10:
    print(FEHLER_LAENGE, len(isbn10), file=sys.stderr)
    exit(1)

# Prüfe auf valide ISBN-10:
# Summe der Produkte der ersten 9 Ziffern mit ihren Stellenindex (beginnend bei 1) bilden

sum_isbn = 0
for i, c in enumerate(isbn10[:-1]):
    sum_isbn += (i + 1) * int(c)

# Abgleich mit Prüfziffer
# vorher x in 10 umwandeln

if isbn10[-1] in "xX":
    prüfziffer = 10
else:
    prüfziffer = int(isbn10[-1])

# Fehlermeldung bei fehlerhafter ISBN
# Mod 11 der Summe muss die 10. Stelle ergeben
if prüfziffer != sum_isbn % 11:
    print(FEHLER_ISBN10_NICHT_VALIDE, file=sys.stderr)
    exit(1)


# Konvertierung
isbn13_ohne_pruefwert = "978" + isbn10[0:9] 

# Prüfwert ermitteln
#  Summe der Ziffern, wobei Ziffern auf geraden Stellen dreifach gewertet werden
sum_isbn13 = 0
for i, c in enumerate(isbn13_ohne_pruefwert):
    if (i+1) % 2 == 0:
        sum_isbn13 += 3 * int(c)
    else:
        sum_isbn13 += int(c)

# Hinweis: Alternative Rechenweise: Summe der ungeraden stellen + 3 * Summe der geraden Stellen

letzte_stelle_isbn13 = ( 10 - ( sum_isbn13 % 10 ) ) % 10 

# Prüfwert konkatenieren
isbn13 = str(isbn13_ohne_pruefwert) + str(letzte_stelle_isbn13)


print(f"Konvertiernug abgeschlossen.\nISBN-10 {isbn10_input} als ISpy isbn_conventer_BL_2.py 3-16-148410-XBN-13 lautet: 978{isbn10[0:-1]}{letzte_stelle_isbn13}")