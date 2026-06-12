"""
ISBN-10 zu ISBN-13 Konverter
Beata Lakeberg
Version 3 11.03.2026
"""

import sys


def clean_isbn(isbn: str) -> str:
    """Entfernt Bindestriche und Leerzeichen, wandelt in Großbuchstaben um."""
    return isbn.replace("-", "").replace(" ", "").upper()


def validate_isbn10(isbn: str) -> bool:
    """
    Prüft ob eine ISBN-10 gültig ist.
    Summe von (10*d1 + 9*d2 + ... + 1*d10) muss durch 11 teilbar sein.
    Letzte Ziffer darf 'X' sein(= 10).
    """
    if len(isbn) != 10:
        return False

    # Erste 9 Zeichen müssen Ziffern sein
    if not isbn[:9].isdigit():
        return False

    # Letzte Stelle darf Ziffer oder 'X' sein
    if not (isbn[9].isdigit() or isbn[9] == 'X'):
        return False

    # Prüfsumme berechnen
    total = 0
    position = 1

    for idx, i in enumerate(isbn):
        if i == "X":
            if idx == 9:
                digit = 10
            else:
                raise ValueError
        else:
            digit = int(i)
        total += digit * (10 - idx)
    return total % 11 == 0


def isbn10_to_isbn13(isbn10: str) -> str:
    """
    Konvertiert eine gültige ISBN-10 zu ISBN-13.
    Algorithmus:
    1. Entferne die Prüfziffer der ISBN-10
    2. Füge "978" am Anfang hinzu
    3. Berechne neue Prüfziffer
    """
    # Prüfziffer entfernen, "978" voranstellen
    isbn13_without_check = "978" + isbn10[:9]

    # Neue Prüfziffer berechnen
    # Abwechselnd mit 1 und 3 multiplizieren (erste Zahl*1, zweites Zahl+3 usw.)
    total = 0
    for i, digit in enumerate(isbn13_without_check):
        factor = 1 if i % 2 == 0 else 3
        total += factor * int(digit)
    check_digit = (10 - (total % 10)) % 10
    return isbn13_without_check + str(check_digit)


#def format_isbn13(isbn: str) -> str:
    #"""Nice to have: Formatierung ISBN-13 mit Bindestrichen: 978-X-XX-XXXXXX-X"""
    #return f"{isbn[0:3]}{isbn[3]}{isbn[4:6]}{isbn[6:12]}{isbn[12]}"


def main() -> None:
    # Kommandozeilen-Argument
    raw_input = sys.argv[1]
    print(f"Eingabe: {raw_input}")

    # Bereinigen
    isbn = clean_isbn(raw_input)
    print(f"Bereinigt: {isbn}")

    # Validieren
    if not validate_isbn10(isbn):
        print(f"Fehler: '{raw_input}' ist keine gültige ISBN-10!")
        sys.exit(1)

    # Konvertieren
    isbn13 = isbn10_to_isbn13(isbn)
    #isbn13_formatted = format_isbn13(isbn13)

    print(f"ISBN-10: {raw_input}")
    print(f"ISBN-13: {isbn13}")


if __name__ == "__main__":
    main()
