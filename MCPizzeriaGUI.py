# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
#s
#
# Vul hier jullie namen in:
# Krijn Meulenkamp, Finn Mooiman
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL


### ---------  Functie definities  -----------------

def zoekKlant():
    gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
    
    print(gevonden_klanten) 

### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")

Knopsluit = Button(venster, text="Sluiten", width = 12, command = venster.destroy)
Knopsluit.grid (row=17, column=4)

labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky="W")

labelKlantnaam = Label(venster, text="Klantnaam:")
labelKlantnaam.grid(row=1, column=0, sticky="W")

ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")

invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

KnopZoekOpKlantnaam = Button(venster, text="Zoek Klant", width=12, command=zoekKlant)
KnopZoekOpKlantnaam.grid (row=1, column=4)

venster.mainloop()