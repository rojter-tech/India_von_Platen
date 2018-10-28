#India von Platen
#Påbörjades 11/10-2018
#Kurs i programmeringsteknik
#DD100N
#Uppgift 127- Platsbokning på SJ
#Datastrukturer: Filhantering, listor med objekt

import sys, os              


class Biljett:


    def __init__(self, sträcka = "Stockholm - Malmö", avgångstid = "15.00", plats = 0, ägare = "Ingen vald", gång = "Ingen vald" + "\n"):
        """Skriver ut valmenyn.
   Inparameter: self, sträcka, avgångstid, ägare, gång.
   Returnerar: ingenting """
        self.sträcka = sträcka
        self.avgångstid = avgångstid
        self.plats = plats
        self.ägare = ägare
        self.gång = gång
    

    def __repr__(self):
        """Skriver ut valmenyn.
   Inparameter: self
   Returnerar: uppbyggnad för hur utskriften av en biljett ska se ut. """
        delsträng1 = "PLATSBILJETT" + "\n" + str(self.sträcka) + "\n"
        delsträng2 = str(self.avgångstid) + "\n" + "Plats " + str(self.plats) + " \n" 
        delsträng3 = str(self.ägare) + "\n" + str(self.gång) + "\n"
        bijettUtskrift = delsträng1 + delsträng2 + delsträng3
        return bijettUtskrift


def konverteraPlatsLista(platsListaKolumn):
    """Byter plats på rad och kolumn i en lista. 
       Inparameter: platsListaKolumn
        Returnerar: en lista- platsLista"""
    platsLista = []
    platsRad = []
    for i in range(4):
        for j in range(8):
            platsRad.append(platsListaKolumn[j][i])
        platsLista.append(platsRad)
        platsRad = []
    return platsLista


def hämtaPlatsStatus(biljett,biljettNummer):
    if biljett.plats == 0:
        if biljettNummer < 10:
            platsstatus = str(biljettNummer) + " "
        else:
            platsstatus = str(biljettNummer)
        
    else:
        platsstatus = "* "
    return platsstatus


def hämtaPlatsSekvens(platsSekvens,i):
    if (i % 2) == 0: # Läses som "i modulus 2" som blir 0 om i är ett jämnt tal (0, 2, 4 .. osv)
        return platsSekvens
    else:
        return platsSekvens[::-1] # Annars (om i är udda) lagras platserna i omvänd ordning.


def hämtaPlatsLista(biljettLista):
    platsLista = 8 * [None]
    platsSekvens = 4 * [None]
    biljettIndex = 0
    for i in range(8):
        for j in range(4):
            biljett = biljettLista[biljettIndex]
            biljettNummer = biljettIndex + 1
            platsSekvens[j] = hämtaPlatsStatus(biljett,biljettNummer)
            biljettIndex += 1
        
        platsLista[i] = hämtaPlatsSekvens(platsSekvens,i)
        platsSekvens = 4 * [None]
    return platsLista


def hanteraPlatser(biljettLista):
    """Tar in en lista med alla existerande biljettobjekt
        och hämtar information om platsnummer som i sin tur
        lagras i en ny lista. 
       Inparameter: en lista med objekt av typen Biljett()- biljettLista
        Returnerar: en lista med heltal- konverteraPlatsLista(platsListaKolumn)"""
    platsLista = hämtaPlatsLista(biljettLista)
    rättvändPlatslista = konverteraPlatsLista(platsLista)
    return rättvändPlatslista # Gör en sista konvertering av listan och returnerar den "rättvända" listan.


def skrivUtLedigaPlatser(biljettLista):
    """Skriver ut bilden av tågvagnen.
   Inparameter: en lista med objekt i- biljettLista
   Returnerar: ingenting """
    
    platsLista = hanteraPlatser(biljettLista)

    n = 0
    print("________________________________________________")
    for platsKolumn in platsLista:
        n += 1
        if n == 3:
            print("     TYST AVD           |")
            print(platsKolumn)
        else:
            print(platsKolumn)
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")


def bokaBiljett():
    """Skriver ut valmenyn
   Inparameter: ett objekt- biljett
   Returnerar:variabel som innehåller information om biljetten- nyBiljett """
    nyBiljett = hanteraBiljett(Biljett())
    sparaBiljett(nyBiljett)

    return nyBiljett
    

def sparaBiljett(biljett):
    """Sparar den bokade biljetten till en fil.
   Inparameter: ett objekt- biljett
   Returnerar: inget """
    dennaMapp = os.path.dirname(sys.argv[0])
    biljettMapp = os.path.join(dennaMapp,"biljetter")
    filnamn = os.path.join(biljettMapp,"biljett_" + str(biljett.plats) + ".txt")
    
    with open(filnamn, "w") as file:
        file.write(str(biljett))
    
    print("Plats nummer " + str(biljett.plats) + " är nu bokad!")
    print("\nHär är din biljett:\n")
    print(biljett)
    

def hanteraBiljett(biljett):
    """Ger attributen plats och ägare nya värden till biljettobjektet. 
   Inparameter: ett objekt- biljett
   Returnerar: ett objekt- biljett """
    print("Bokning av biljett: ")
    print("Vilken plats vill du ha?\n(Platser makerade med * är redan bokade): ")
    platsInput = input("Ange en ledig plats (1-32): ")
    while True:
        while not platsInput.isdigit():
            print("Du måste ange ett nummer mellan 1 och 32!")
            platsInput = input("Försök igen: ")
        while platsInput.isdigit():
            if int(platsInput) > 32 or int(platsInput) < 1:
                print("Du måste ange ett nummer mellan 1 och 32!")
                platsInput = input("Försök igen: ")
            else:
                biljett.plats = int(platsInput)
                gång = platser(biljett.plats)
                biljett.ägare = input("Vad heter du?: ")
                biljett.gång = gång
                return biljett


def skapaBiljettfiler():
    """Skapar tomma biljettfiler med defaultparametrar från
        klassen Biljett(), om de inte redan existerar.
        Inparameter: ingen
        Returnerar: inget"""
    dennaMapp = os.path.dirname(sys.argv[0])
    biljettMapp = os.path.join(dennaMapp,"biljetter")
    if not os.path.isdir(biljettMapp):
        os.mkdir(biljettMapp)
    biljettsträng = str(Biljett())
    for i in range(32):
        filnamn = os.path.join(biljettMapp,"biljett_" + str(i+1) + ".txt")
        finnsFil = os.path.isfile(filnamn)
        if not finnsFil: 
                with open(filnamn, "w") as file:
                    file.write(biljettsträng)


def läsaInBiljetter():
    """Går igenom samtliga biljettfiler och läser av rad för rad
        information som sedan lagras i biljettobjekt som i sin tur
        lagras i en lista. 
        Inparameter: ingen
        Returnerar: en lista- biljettLista"""
    biljettLista = 32 * [None]
    dennaMapp = os.path.dirname(sys.argv[0])
    biljettMapp = os.path.join(dennaMapp, "biljetter")
    for i in range(32):
        filnamn = os.path.join(biljettMapp, "biljett_" + str(i+1) + ".txt")
        with open(filnamn, "r") as file:
            file.readline()
            sträcka = file.readline()
            avgångstid = file.readline()
            plats = int(file.readline().split(' ')[1])
            ägare = file.readline()
            biljettLista[i] = Biljett(sträcka, avgångstid, plats, ägare)
    return biljettLista


def avbokaBiljett(biljettLista,plats):
    """Skriver över filer som innehåller de biljetter som ska avbokas.
   Inparameter: en lista med objekt och ett atribut- biljettLista och plats.
   Returnerar:  en lista med objekt- biljettLista"""
    print("Avboka biljett: ")
    skrivUtLedigaPlatser(biljettLista)
    dennaMapp = os.path.dirname(sys.argv[0])
    biljettMapp = os.path.join(dennaMapp,"biljetter")
    filnamn = os.path.join(biljettMapp,"biljett_" + str(plats) + ".txt")
    with open(filnamn, "w") as file:
        file.write(str( Biljett() ))
    
    biljettLista[plats-1] = Biljett()
    print("Plats nummer " + str(plats) + " är nu avbokad!")
    skrivUtLedigaPlatser(biljettLista)
    return biljettLista


def skrivUtSenasteBiljetter(biljettLista):
    """Skriver ut de biljetter som senast bokats.
   Inparameter: en lista med objekt- biljettLista
   Returnerar: två olika strängar beroende på värdet av plats """
    for i in range(32):
        if biljettLista[i].plats != 0:
            print(str(biljettLista[i]))


def platser(plats):
    """Hanterar de strängar som tillhör värdena på plats i biljettobjektet.
   Inparameter: ett attribut- plats
   Returnerar: Två olika strängar - MITTGÅNG eller FÖNSTERPLATS """
    if plats == 2 or plats == 3 or plats == 6 or plats == 7 or plats == 10 or plats == 11 or plats == 14 or plats == 15:
        return "MITTGÅNG"
    elif plats == 18 or plats == 19 or plats == 22 or plats == 23 or plats == 26 or plats == 27 or plats == 30 or plats == 31:
        return "MITTGÅNG"
    else:
        return "FÖNSTERPLATS"


def skrivUtAnvändarAlternativ():
    print("• Boka, skriv ’B’, på samma rad följt av önskat antal biljetter.\n\n• Avboka, skriv ’A’, på samma rad följt av ett platsnummer.\n")
    print("• Skriva ut de senast bokade biljetterna, skriv ’S’.\n\n• Avsluta, skriv ’Q’.\n")
    vad = str(input("Vad vill du göra?: "))
    while True:
        while vad == "":
            print("Du måste ange ett av alternativen så som det står angivet i instruktionerna ovan.")
            vad = input("Försök igen: ")
        if bool(vad):
            print("")
            return vad


def menyLoop():
    fortsätt = input("Vill du gå tillbaka till huvudmenyn och göra ett nytt val? (j/n): ")
    while True:
        while fortsätt == "":
            print("Du måste svara antingen 'j(ja)' eller 'n(nej)'.")
            fortsätt = input("Försök igen: ")
        while bool(fortsätt):
            if fortsätt[0] == "J" or fortsätt[0] == "j":
                print("")
                vad = skrivUtAnvändarAlternativ()
                return vad
            elif fortsätt[0] == "N" or fortsätt[0] == "n":
                print("")
                return "Q"
            else:
                fortsätt = ""


def huvudMeny(biljettLista):
    """Skriver ut valmenyn samt anropar resterande funktioner i programmet
   Inparameter: ingen
   Returnerar: inget"""

    vad = skrivUtAnvändarAlternativ()
    
    while True: #Fixa felhantering
        if vad[0] == "x":
            vad = menyLoop()
        elif vad[0] == "B" or vad[0] == "b":
            biljettLista = underMenyBokning(biljettLista,vad)
            vad = "x"
        elif vad[0] == "A" or vad[0] == "a":
            biljettLista = underMenyAvBokning(biljettLista,vad)
            vad = "x"
        elif vad[0] == "S" or vad[0] == "s": 
            skrivUtLedigaPlatser(biljettLista)
            vad = "x"
        elif vad[0] == "Q" or vad[0] == "q":
            print("Tack och välkommen åter!")
            break
        else:
            underMenyFelInmatning()
            vad = "x"


def underMenyFelInmatning():
    print("Du måste välja antingen B, A, S eller Q.")
    input("Tryck Enter för att fortsätta: ")


def underMenyBokning(biljettLista,vad):
    
    while True:
        vadLista = vad.split(' ')
        if len(vadLista) > 1:
            while len(vadLista) != 2:
                print("Biljettbokning måste anges med ett B följt av ett mellanslag och ett nummer1")
                print("för att ange antal bokningar, exempelvis 'B 1' ")
                print("")
                vad = str(input("Försök igen: "))
                vadLista = vad.split(' ')
            if vadLista[0] == 'B' or vadLista[0] == 'b' and vadLista[1].isdigit():
                skrivUtLedigaPlatser(biljettLista)
                antalBiljetter = int(vadLista[1])
                for i in range(antalBiljetter):
                    nyBiljett = bokaBiljett()
                    biljettLista[nyBiljett.plats - 1] = nyBiljett
                return biljettLista
        else:
            print("Biljettbokning måste anges med ett B följt av ett mellanslag och ett nummer2")
            print("för att ange antal bokningar, exempelvis 'B 1' ")
            print("")
            vad = str(input("Försök igen: "))



def underMenyAvBokning(biljettLista,vad):
    vadLista = vad.split(' ')
    vadListaLängd = len(vadLista)
    if vadListaLängd == 2 and vadLista[1].isdigit():
        avbokadPlats = int(vadLista[1])
        biljettLista = avbokaBiljett(biljettLista,avbokadPlats)
        return biljettLista
    else:
        print("Biljettavbokning måste anges med ett A följt av ett mellanslag och ett nummer.")
        print("")
        return biljettLista


def huvudProgram():
    """Anropar huvumenyn
   Inparameter: ingen
   Returnerar: inget """

    skapaBiljettfiler()
    biljettLista = läsaInBiljetter()
    print("Välkommen till SJ!\n")
    huvudMeny(biljettLista)


huvudProgram()


"""Algoritm:
1. Anropar funktion som skapar filer samt definerar biljettLista 
2. Hälsar användaren välkommen
3. Skriver ut menyn
4. Låter användaren välja menyval
5. Utför det menyval som användaren valt
6. Tills att användaren väljer att avsluta upprepas steg 3-5."""
