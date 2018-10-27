#India von Platen
#Påbärjades 11/10-2018
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
        return "PLATSBILJETT" + "\n" + str(self.sträcka) + "\n" + str(self.avgångstid) + "\n" + "Plats " + str(self.plats) + " \n" + str(self.ägare) + "\n" + str(self.gång) + "\n"


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


def hanteraPlatser(biljettLista):
    """Tar in en lista med alla existerande biljettobjekt
        och hämtar information om platsnummer som i sin tur
        lagras i en ny lista. 
       Inparameter: en lista med objekt av typen Biljett()- biljettLista
        Returnerar: en lista med heltal- konverteraPlatsLista(platsListaKolumn)"""
    platsListaKolumn = []
    platsKolumn = []
    k = 0
    for i in range(8):
        for j in range(4):
            if biljettLista[k].plats == 0:
                biljett = biljettLista[k]
                biljettNummer = biljettLista.index(biljett) + 1

                if biljettNummer < 10:
                    platsKolumn.append(str(biljettNummer) + " ")
                else:
                    platsKolumn.append(str(biljettNummer))
            
            else:
                platsKolumn.append("* ")
            
            k += 1

        if (i % 2) == 0:
            platsListaKolumn.append(platsKolumn)
        else:
            platsListaKolumn.append(platsKolumn[::-1])
        
        platsKolumn = []
    return konverteraPlatsLista(platsListaKolumn)


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


def bokaBiljett(biljett):
    """Skriver ut valmenyn
   Inparameter: ett objekt- biljett
   Returnerar:variabel som innehåller information om biljetten- nyBiljett """
    nyBiljett = hanteraBiljett(biljett) 
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
    

def hanteraBiljett(biljett):
    """Ger attributen plats och ägare nya värden till biljettobjektet. 
   Inparameter: ett objekt- biljett
   Returnerar: ett objekt- biljett """
    print("Bokning av biljett: ")
    biljett.plats = int(input("Vilken plats vill du ha? (1-32)\n(Platser makerade med * är redan bokade): "))

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


def avbokaBiljett(biljettLista, plats):
    """Skriver över filer som innehåller de biljetter som ska avbokas.
   Inparameter: en lista med objekt och ett atribut- biljettLista och plats.
   Returnerar:  en lista med objekt- biljettLista"""
    dennaMapp = os.path.dirname(sys.argv[0])
    biljettMapp = os.path.join(dennaMapp, "biljetter")
    skrivUtLedigaPlatser(biljettLista)

    filNamnAvboka = os.path.join(biljettMapp, "biljett_" + str(plats) + ".txt") 

    with open(filNamnAvboka, "w") as file:
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
    if plats == 2 or plats == 3 or plats == 7 or plats == 6 or plats == 10 or plats == 11 or plats == 15 or plats == 14 or plats == 18 or plats == 19 or plats == 23 or plats == 22 or plats == 26 or plats == 27 or plats == 31 or plats == 30:
        return "MITTGÅNG"

    if plats == 1 or plats == 4 or plats == 8 or plats == 5 or plats == 9 or plats == 12 or plats == 16 or plats == 13 or plats == 17 or plats == 20 or plats == 24 or plats == 21 or plats == 25 or plats == 28 or plats == 32 or plats == 29:
        return "FÖNSTERPLATS"


def huvudMeny():
    """Skriver ut valmenyn samt anropar resterande funktioner i programmet
   Inparameter: ingen
   Returnerar: inget"""
    skapaBiljettfiler()
    biljettLista = läsaInBiljetter()

    print("Välkommen till SJ!\n")
    print("• Boka, skriv ’B’, på samma rad följt av önskat antal biljetter.\n\n• Avboka, skriv ’A’, på samma rad följt av ett platsnummer.\n")
    print("• Skriva ut de senast bokade biljetterna, skriv ’S’.\n\n• Avsluta, skriv ’Q’.\n")
    
    vad = str(input("Vad vill du göra?: "))
    
    while True: 
        if vad == "x":
            fortsätt = input(str("Vill du göra något mer?: "))
            if fortsätt == "Ja" or fortsätt == "ja":
                vad = input(str("Vad vill du göra?(A, B, S eller Q): "))
            else:
                print("Tack och välkommen åter!")
                break
        elif vad[0] == "B" or vad[0] == "b":
            skrivUtLedigaPlatser(biljettLista)
            vadLista = vad.split(' ')
            antalBiljetter = int(vadLista[1])
            for i in range(antalBiljetter):
                nyBiljett = bokaBiljett(Biljett())
                print(nyBiljett)
                biljettLista[nyBiljett.plats - 1] = nyBiljett
            vad = "x"
            print("Plats nummer " + str(nyBiljett.plats) + " är nu bokad")
        elif vad[0] == "A" or vad[0] == "a":
            print("Avboka biljett: ")
            vadLista = vad.split(' ')
            antalAvbokadeBiljetter = int(vadLista[1])
            biljettLista = avbokaBiljett(biljettLista, antalAvbokadeBiljetter)
            vad = "x"
        elif vad == "S" or vad == "s": 
            skrivUtSenasteBiljetter(biljettLista)
            vad = "x"
        elif vad == "Q" or vad == "q":
            print("Tack och välkommen åter!")
            break
        else:
            print("Välj antingen B, A, S eller Q.")
            vad = "x"


def huvudProgram():
    """Anropar huvumenyn
   Inparameter: ingen
   Returnerar: inget """
    
    huvudMeny()

huvudProgram()


"""Algoritm:
1. Anropar funktion som skapar filer samt definerar biljettLista 
2. Hälsar användaren välkommen
3. Skriver ut menyn
4. Låter användaren välja menyval
5. Utför det menyval som användaren valt
6. Tills att användaren väljer att avsluta upprepas steg 3-5."""
