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
    for i in range(4):
        for j in range(8):
            platsRad.append(platsListaKolumn[j][i])
        platsLista.append(platsRad)
        platsRad = []
    return platsLista


def hanteraPlatser(biljettLista):
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
    #⏊  ⏉ ⏌⎾ ⏋⎿
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
    dennaMapp = os.path.dirname(sys.argv[0])
    biljettMapp = os.path.join(dennaMapp,"biljetter")
    filnamn = os.path.join(biljettMapp,"biljett_" + str(biljett.plats) + ".txt")
    
    with open(filnamn, "w") as file:
        file.write(str(biljett))
    

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
    skrivUtLedigaPlatser(biljettLista)
    plats = int(input("Vilken plats vill du avboka?(1-32): "))

    filnamnAvboka = "biljett_" + str(plats) + ".txt"

    with open(filnamnAvboka, "w") as file:
        file.write(str( Biljett() ))
    biljettLista[plats-1] = Biljett()
    print("Plats nummer " + str(plats) + " är nu avbokad!")
    skrivUtLedigaPlatser(biljettLista)
    return biljettLista


def skrivUtSenasteBiljetter(biljettLista):
    for i in range(32):
        if biljettLista[i].plats != 0:
            print(str(biljettLista[i]))


def platser(plats):###############
    if plats == 2 or plats == 3 or plats == 7 or plats == 6 or plats == 10 or plats == 11 or plats == 15 or plats == 14 or plats == 18 or plats == 19 or plats == 23 or plats == 22 or plats == 26 or plats == 27 or plats == 31 or plats == 30:
        return "MITTGÅNG"

    if plats == 1 or plats == 4 or plats == 8 or plats == 5 or plats == 9 or plats == 12 or plats == 16 or plats == 13 or plats == 17 or plats == 20 or plats == 24 or plats == 21 or plats == 25 or plats == 28 or plats == 32 or plats == 29:
        return "FÖNSTERPLATS"


def huvudmeny():
    skapaBiljettfiler()
    biljettLista = läsaInBiljetter()

    print("Välkommen till SJ!\n")
    print("• Boka, skriv ’B’, på samma rad följt av önskat antal biljetter.\n\n• Avboka, skriv ’A’, på samma rad följt av ett platsnummer.\n")
    print("• Skriva ut de senast bokade biljetterna, skriv ’S’.\n\n• Avsluta, skriv ’Q’.\n")
    
    biljett= Biljett()
    
    vad = str(input("Vad vill du göra?: "))
    
    while True: #Fixa felhantering
        if vad == "x":
            fortsätt = input(str("Vill du göra något mer?: "))
            if fortsätt == "Ja" or fortsätt == "ja":
                vad = input(str("Vad vill du göra?(A, B, S eller Q): "))
            else:
                print("Tack och välkommen åter!")
                break
        elif vad == "B" or vad == "b":
            skrivUtLedigaPlatser(biljettLista)
            nyBiljett = hanteraBiljett(biljett) #nyBiljett = det som hanteraBiljett(biljett) returnerar. Det skickas vidare till bokaBiljett(nyBiljett) 
            bokaBiljett(nyBiljett)
            print(nyBiljett)
            biljettLista[nyBiljett.plats - 1] = nyBiljett
            vad = "x"
            print("Plats nummer" + str(nyBiljett.plats) + " är nu bokad")
        elif vad == "A" or vad == "a":
            print("Avboka biljett: ")
            biljettLista = avbokaBiljett(biljettLista)
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
    huvudmeny()


huvudProgram()