
# Online Python - IDE, Editor, Compiler, Interpreter

def isbn13_umrechner(list_isbn10_ohne_pruef):
    #Ergänzung um Präfix
    isbn13_praefix = [9,7,8]
    #Addition Präfix und ISBN-10
    list_isbn13_ohne_pruef = isbn13_praefix + list_isbn10_ohne_pruef
    pruefsumme = 0
    for i, number in enumerate(list_isbn13_ohne_pruef):
       #Integration Formel für ISBN-13
        if i%2 == 0:
            pruefsumme += number*1
        else: 
            pruefsumme += number*3
    modulo = pruefsumme % 10
    pruefziffer = 10 - modulo
    #Sicherung für Prüfziffer X bzw. x
    if pruefziffer == 10:
        pruefziffer = 0
    #ISBN-Ausgabe als String, erst list umwandeln von int-Bestandteilen zu String-Bestandteilen 
    list_isbn13 = list_isbn13_ohne_pruef + [pruefziffer]
    str_list_isbn13 = map(str, list_isbn13)
    #Dann Überführung zu einem String
    #Entscheidung bei der Umsetzung, dass Ausgabe ohne Bindestriche, siehe separator
    separator = ''
    isbn13 = separator.join(str_list_isbn13)
    return isbn13
#Testet hier Länge  
def pruefe_isbn10_laenge(isbn10):
    #Bindestrich entfernen
    isbn10_bereinigt = isbn10.replace("-", "")
    #Länge überprüfen
    if len(isbn10_bereinigt) != 10:
        return False
    else:
        return isbn10_bereinigt
        
def pruefe_isbn10_pruefziffer(list_isbn10_ohne_pruef, pruefziffer):
    pruefsumme = 0
    i = 0
    #Integration der Prüfsummenformel für ISBN-10 via Schleife, die jede Stelle abdeckt
    for i, number in enumerate(list_isbn10_ohne_pruef):
        x = i + 1
        pruefsumme = number*x + pruefsumme
    modulo_check = pruefsumme % 11
    #Kontrolle, ob Prüfziffer nicht X ist
    if modulo_check == 10:
        berechnete_pruefziffer = str("X")
    else: 
        berechnete_pruefziffer = str(modulo_check)
    #Check, ob berechnete Prüfziffer identisch mit Übergebener
    return pruefziffer == berechnete_pruefziffer
#import sys
#isbn10 = '0-306-40615-2'
#isbn10 = '3-499-13599-x'
#Intro für das Programm
print("Hallo beim 'ISBN10->ISBN13'-Konverter")
print("Bitte beachte bei der Eingabe:")
print("keine Trennzeichen oder '-' erlaubt")
print("und gebe nur 10stellige ISBN's ein")
#!!!!!!!!!!!Eingabe hier falsch, realisiert via Editor!!!!!!!!!!!
#isbn10 = sys.argv[1]
isbn10 = input('Gib eine ISBN-10 ein: ')
#Testet hier Länge
test_ergebnis_isbn10 = pruefe_isbn10_laenge(isbn10)
if test_ergebnis_isbn10 is False:
    print("Fehler: Falsche Länge der ISBN, 10stellig erforderlich")
else:
    #print("Bereinigte ISBN-10:", test_ergebnis_isbn10)
    pruefziffer = test_ergebnis_isbn10[-1]
    #Buchstaben groß schreiben, keine Auswirkung auf Zahlen
    pruefziffer = pruefziffer.upper()
    #Check, ob Prüfziffer eine Zahl oder x ist
    if not (pruefziffer.isdigit() or pruefziffer == "X"):
        print("Fehler: Prüfziffer muss 0-9 oder X sein")
    else:
        #Prüfziffer rausnehmen
        isbn10_ohne_pruef = test_ergebnis_isbn10[:-1]
        #Überprüfen, ob in ISBN ohne Prüfziffer nur Ziffern vorliegen
        if not isbn10_ohne_pruef.isdigit():
            print("Fehler: ISBN-10 darf nur Ziffern in den ersten 9 Stellen enthalten")
        else:
            #ISBN als Liste nur mit int's umwandeln, um damit weiter rechnen zu können
            list_isbn10_ohne_pruef = [int(z) for z in isbn10_ohne_pruef]
            #Aufruf Funktion, die Prüfziffer überprüft
            if pruefe_isbn10_pruefziffer(list_isbn10_ohne_pruef,pruefziffer) == True:
                #Wenn true, dann Berechnung ISBN-13
                print("Die umgerechnete ISBN-13 ist: " + isbn13_umrechner(list_isbn10_ohne_pruef))
            else: print("Fehler: Ungültige ISBN")    


