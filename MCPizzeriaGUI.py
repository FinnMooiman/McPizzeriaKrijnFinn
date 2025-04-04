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
#haal de ingevoerde_klantnaam op uit het invoerveld
# en gebruik dit om met SQL de klant in database te vinden
    gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
    print(gevonden_klanten) # om te testen

    invoerveldKlantnaam.delete(0, END) #invoerveld voor naam leeg maken
    invoerveldKlantNr.delete(0, END) #invoerveld voor klantNr leeg maken
    for rij in gevonden_klanten: #voor elke rij dat de query oplevert
        #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld
        invoerveldKlantNr.insert(END, rij[0])
        #toon klantAchternaam, de tweede kolom uit het resultaat in de invoerveld
        invoerveldKlantnaam.insert(END, rij[1])

### functie voor het selecteren van een rij uit de listbox en deze in een andere veld te plaatsen
def haalGeselecteerdeRijOp(event):
    geselecteerdeRegelInLijst = listboxMenu.curselection()[0]
    geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst)
    invoerveldGeselecteerdePizza.delete(0, END)
    invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst)

def toonMenuInListbox():
    listboxMenu.delete(0, END)  #maak de listbox leeg
    listboxMenu.insert(0, "ID \t Gerecht \t \t Prijs")
    pizza_tabel = MCPizzeriaSQL.vraagOpGegevensPizzaTabel()
    for regel in pizza_tabel:
        listboxMenu.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu

def voegToeAanWinkelWagen():
    klantNr = invoerveldKlantNr.get()
    gerechtID = geselecteerdePizza.get()
    aantal = aantalGeslecteerdePizza.get()
    MCPizzeriaSQL.voegToeAanWinkelWagen(klantNr, gerechtID, aantal )
    winkelwagen_tabel = MCPizzeriaSQL.vraagOpGegevensWinkelWagenTabel()
    listboxWinkelwagen.delete(0, END) #listbox eerst even leeg maken
    for regel in winkelwagen_tabel:
        listboxWinkelwagen.insert(END, regel)

### --------- Hoofdprogramma  ---------------

venster = Tk()
# venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
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

labelKlantnr = Label(venster, text="Klantnummer")
labelKlantnr.grid(row=2, column=0, sticky="W")

invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

KnopZoekOpKlantnaam = Button(venster, text="Zoek Klant", width=12, command=zoekKlant)
KnopZoekOpKlantnaam.grid (row=1, column=4)

knopToonPizzas = Button(venster, text="Toon alle pizza's", width=12, command=toonMenuInListbox)
knopToonPizzas.grid(row=3, column=4)

listboxMenu = Listbox(venster, height=6, width=50)
listboxMenu.grid (row=2, column=1, rowspan=6, columnspan=2, sticky="W")

scrollbarListboxMenu = Scrollbar (0, END)
scrollbarListboxMenu.grid (row=2, column=1, rowspan=6, sticky="E")
ListboxMenu.config(yscrollcommand=scrollbarListboxMenu.set)
scrollbarListboxMenu.config(command=ListboxMenu.yview) 



venster.mainloop()