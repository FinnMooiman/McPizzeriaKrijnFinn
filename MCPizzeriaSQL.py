# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in: Krijn Meulenkamp, Finn Mooiman
#
#
#


### --------- Bibliotheken en globale variabelen -----------------

import sqlite3
with sqlite3.connect("MCPizzeria.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen


### ---------  Functie definities  -----------------

def maakTabellenAan():
     # Maak een nieuwe tabel met 3 kolommen: id, naam, prijs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_pizzas(
            gerechtID INTEGER PRIMARY KEY AUTOINCREMENT
            gerechtNaam TEXT NOT NULL
            gerechtPrijs REAL NOT NULL);""")
    print("Tabel 'tbl_pizzas' aangemaakt.")

def printTabel (tabel_naam):
    cursor.execute("SELECT * FROM " + tabel_naam) #SQL om ALLE gegevens te halen
    opgehaalde_gegevens = cursor.fetchall() #sla gegevens op in een variabele
    print("Tabel " + tabel_naam + ":", opgehaalde_gegevens) #druk gegevens af

def verwijderPizza(gerechtNaam):
    cursor.execute("DELETE FROM tbl_pizzas WHERE gerechtNaam = ?", (gerechtNaam,))
    print("Gerecht verwijderd uit 'tbl_pizzas':",gerechtNaam )
    db.commit() #gegevens naar de database wegschrijven
    PrintTabel("tbl_pizzas")


### --------- Hoofdprogramma  ---------------

maakTabellenAan()

printTabel("tbl_pizzas")

print("HALLO")