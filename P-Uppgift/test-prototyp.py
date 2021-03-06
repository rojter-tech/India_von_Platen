import sys, os #Tillåter Python att anropa operativsystemrelaterad information, kollar av filnamn             


class Biljett:
    

    def __init__(self, sträcka = "Stockholm - Malmö", avgångstid = "15.00", plats = 0, ägare = "Ingen vald", gång = "Ingen vald" + "\n"):
        self.sträcka = sträcka
        self.avgångstid = avgångstid
        self.plats = plats
        self.ägare = ägare
        self.gång = gång
    

    def __repr__(self):
        return "PLATSBILJETT" + "\n" + str(self.sträcka) + "\n" + str(self.avgångstid) + "\n" + "Plats " + str(self.plats) + " \n" + str(self.ägare) + "\n" + str(self.gång) + "\n"


def konverteraPlatsLista(platsListaKolumn):
    platsLista = []
    platsRad = []
    for i in range(4): #Kör en forloop genom samtliga 32 biljetter fast i omvänd ordning.
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
    platsLista = hämtaPlatsLista(biljettLista)
    rättvändPlatslista = konverteraPlatsLista(platsLista)
    return rättvändPlatslista # Gör en sista konvertering av listan och returnerar den "rättvända" listan.


def skrivUtLedigaPlatser(biljettLista):
    #⏊  ⏉ ⏌⎾ ⏋⎿
    platsLista = hanteraPlatser(biljettLista) # Hämtar den rättvända listan.

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
    dennaMapp = os.path.dirname(sys.argv[0]) # Argumentet sys.argv[0] anger i vilken mapp python-scriptet ligger.
    biljettMapp = os.path.join(dennaMapp,"biljetter") # Anger sökvägen till mappen "biljetter" som finns i dennaMapp.
    filnamn = os.path.join(biljettMapp,"biljett_" + str(biljett.plats) + ".txt") # Anger sökvägen till själva biljetten.
    
    with open(filnamn, "w") as file:
        file.write(str(biljett))

    print("Plats nummer " + str(biljett.plats) + " är nu bokad!")
    print("\nHär är din biljett:\n")
    print(biljett)


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
    print("Bokning av biljett: ")
    #biljett.sträcka = input("Vart vill du åka?: ")
    #biljett.avgångstid = input("När vill du åka?: ")
    biljett.plats = int(input("Vilken plats vill du ha? (1-32)\n(Platser makerade med * är redan bokade): "))

    gång = platser(biljett.plats)
    
    biljett.ägare = input("Vad heter du?: ")
    biljett.gång = gång

    return biljett


def skapaBiljettfiler():
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


def läsaInBiljetter():#Lagrar dem i biljettLista
    biljettLista = 32 * [None]
    dennaMapp = os.path.dirname(sys.argv[0])
    biljettMapp = os.path.join(dennaMapp,"biljetter")
    for i in range(32):
        filnamn = os.path.join(biljettMapp,"biljett_" + str(i+1) + ".txt")
        with open(filnamn, "r") as file:
            file.readline()
            sträcka = file.readline()
            avgångstid = file.readline()
            plats = int(file.readline().split(' ')[1])
            ägare = file.readline()
            biljettLista[i] = Biljett(sträcka, avgångstid, plats, ägare)
    return biljettLista


def avbokaBiljett(biljettLista):
    print("Avboka biljett: ")
    skrivUtLedigaPlatser(biljettLista)
    dennaMapp = os.path.dirname(sys.argv[0])
    biljettMapp = os.path.join(dennaMapp,"biljetter")
    plats = int(input("Vilken plats vill du avboka?(1-32): "))
    filnamn = os.path.join(biljettMapp,"biljett_" + str(plats) + ".txt")
    with open(filnamn, "w") as file:
        file.write(str( Biljett() ))
    
    biljettLista[plats-1] = Biljett()
    print("Plats nummer " + str(plats) + " är nu avbokad!")
    skrivUtLedigaPlatser(biljettLista)
    return biljettLista


def skrivUtSenasteBiljetter(biljettLista):
    for i in range(32):
        if biljettLista[i].plats != 0:
            print(str(biljettLista[i]))


def platser(plats):
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
    return vad


def menyLoop():
    fortsätt = input("Vill du göra något mer? (j/n): ")
    if fortsätt[0] == "J" or fortsätt[0] == "j":
        print("")
        vad = skrivUtAnvändarAlternativ()
    elif fortsätt[0] == "N" or fortsätt[0] == "n":
        print("")
        vad = "Q"
    else:
        print("Du måste svara antingen 'j(ja)' eller 'n(nej)'.")
        input("Tryck Enter för att fortsätta: ")
        print("")
        vad = "x"
    return vad


def huvudMeny(biljettLista):
    vad = skrivUtAnvändarAlternativ()
    
    while True: #Fixa felhantering
        if vad[0] == "x":
            vad = menyLoop()
        elif vad[0] == "B" or vad[0] == "b":
            biljettLista = underMenyBokning(biljettLista)
            vad = "x"
        elif vad[0] == "A" or vad[0] == "a":
            biljettLista = avbokaBiljett(biljettLista)
            vad = "x"
        elif vad[0] == "S" or vad[0] == "s": 
            skrivUtSenasteBiljetter(biljettLista)
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


def underMenyBokning(biljettLista):
    skrivUtLedigaPlatser(biljettLista)
    nyBiljett = hanteraBiljett(Biljett()) #nyBiljett = det som hanteraBiljett(biljett) returnerar. Det skickas vidare till bokaBiljett(nyBiljett) 
    bokaBiljett(nyBiljett)
    biljettLista[nyBiljett.plats - 1] = nyBiljett #Uppdaterar biljettstatus i biljettLista
    return biljettLista


def huvudProgram():
    skapaBiljettfiler()
    biljettLista = läsaInBiljetter()
    print("Välkommen till SJ!\n")
    huvudMeny(biljettLista)


huvudProgram()