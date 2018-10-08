#Kurs i programmeringsteknik
#India von Platen
#Påbörjades den 7/10- 2018
#DD100N
import random
import os

class Husdjur:
    def __init__(self, namn, hunger = 100, klappBehov = 100):
        self.namn = namn
        self.hunger = hunger
        self.klappBehov = klappBehov
    """Tre paramametrar, visar de tre attributen som varje husdjur har.
    """

    def __repr__(self): 
        return self.namn + " " + str(self.hunger) + " " + str(self.klappBehov)
    """Anropar objektet självt, returnerar ordnad sträng.
    """

    def __lt__(self, other):
        return self.namn < other.namn
    """En parameter, sorterar namnen.
    """

    def mata(self, mat):
        self.hunger -= mat
    """En parameter, drar bort värdet 10 från attributets värde då användaren väljer att mata djuret.
    """

    def klappa(self, klapp):
        self.klappBehov -= klapp
    """En parameter, drar bort värdet 10 från attributets värde då användaren väljer att klappa djuret.
    """


def mojligaPlatser():
    a = " fanns under soffan.."
    b = " hade gomt sig i garderoben.."
    c = " har ramlat fran balkongen.."
    d = " ser helt lost ut.."
    e = " har saknat dig.."
    platsLista = [a,b,c,d,e]
    randomIndex = random.randint(0, len(platsLista))
    plats = platsLista[randomIndex - 1]
    return plats


def hanteraHusdjur(djur):
    """En parameter, skriver ut menyn för varje husdjur.
    """
    plats = mojligaPlatser()
    print("")
    print(djur.namn + plats)
    print("1. Mata " + djur.namn + "\n2. Klappa " + djur.namn + "\n3. Tillbaka till huvudmenyn.")
    svar= input("Vad vill du göra?(1,2 eller 3): ")
    while svar:
        if svar[0] == "1":
            mat = 10
            djur.mata(mat)
            print(djur.namn + " är nu så här mätt: " + str(djur.hunger))
            svar = "0"
        elif svar[0] == "2":
            klapp = 10
            djur.klappa(klapp)
            print(djur.namn + " är så här klappad: " + str(djur.klappBehov))
            svar="0"
        elif svar[0] == "3":
            break
        else:
            print("")
            print("1. Mata " + djur.namn + "\n2. Klappa " + djur.namn + "\n3. Tillbaka till huvudmenyn.")
            svar = input("Vad vill du göra?(1,2 eller 3): ")
            print("")


def sparaHusdjur(husdjursLista):
    """En parameter, spara nya husdjur samt nya värden på attributen hos varje husdjur.
    """
    husdjursLista.sort(key=lambda husdjur:husdjur.namn)
    husdjurTXT = open("husdjursLista.txt", "w")
    for dj in husdjursLista:
        husdjurTXT.write(dj.namn + ' ' + str(dj.hunger) + ' ' + str(dj.klappBehov) + '\n')
    print("")
    print("Välkommen åter!")


def taBortHusdjur(husdjursLista):
    print("")
    print("Vilket djur vill du ta bort?")
    i = 1
    for pr in husdjursLista:
        print(str(i) + ': ' + pr.namn)
        i += 1
    taBort = int(input("Välj nummer: "))
    djur = husdjursLista[taBort-1]
    del husdjursLista[taBort-1]
    print("")
    print("Vad trakigt att " + djur.namn + " inte langre ar med oss! :(")
    print("")


def laggTillHusdjur(husdjursLista):
    print("")
    nyttDjur = input("Vad heter ditt nya djur?: ")
    husdjursLista.append(Husdjur(nyttDjur))
    husdjursLista.sort(key=lambda husdjur:husdjur.namn)
    print("")
    print("Vi valkomnar " + nyttDjur + " till familjen, som just flyttat in!")
    print("")


def hittaHusdjur(husdjursLista):
    print("")
    for pr in husdjursLista:
        print(pr.namn[0] + ': ' + pr.namn)
    hittaDjur = input("Vilket djur vill du hitta?: ")
    for dj in husdjursLista:
        if dj.namn[0] == hittaDjur[0]:
            hanteraHusdjur(dj)
    print("")


def listaHusdjur(husdjursLista):
    print("")
    for pr in husdjursLista:
        print(pr.namn + " ar " + str(pr.hunger) + "% tom i magen och behover " + str(pr.klappBehov) + "% karlek.")
    print("")


def printaHuvudMeny():
    print("1. Lista husdjuren och deras status.\n2. Leta upp ett husdjur.")
    print("3. Lägg till ett nytt husdjur.\n4. Ta bort ett husdjur. \n5. Avsluta.")
    svar = input("Vad vill du göra?: ")
    return svar


def körPetRobo(husdjursLista):
    """En parameter, skriver ut menyn.
    """
    print("Välkommen till PetRobo!\n")
    svar = printaHuvudMeny()
    while svar:
        if svar[0] == "1":
            listaHusdjur(husdjursLista)
            svar = "0"
        elif svar[0] =="2":
            hittaHusdjur(husdjursLista)
            svar = "0"
        elif svar[0] == "3":
            laggTillHusdjur(husdjursLista)
            svar = "0"
        elif svar[0] == "4":
            taBortHusdjur(husdjursLista)
            svar = "0"
        elif svar[0]== "5":
            sparaHusdjur(husdjursLista)
            break
        else:
            svar = printaHuvudMeny()


def hämtaHusdjur():
    """Ingen parameter, hämtar sparad lista
    """

    husdjursLista = []

    husdjurTXT = open("husdjursLista.txt", "r")
    j = '\n'
    husdjurSträng = "nySträng"
    while j == '\n' and husdjurSträng != '':
        husdjurSträng = husdjurTXT.readline()
        for i in husdjurSträng:
            if i == '\n':
                djurObjektLista = husdjurSträng.split(' ')
                djur = Husdjur(djurObjektLista[0], int(djurObjektLista[1]), int(djurObjektLista[2]))
                husdjursLista.append(djur)
        j = i
    husdjursLista.sort(key=lambda husdjur:husdjur.namn)
    return husdjursLista


def kollaHudjurslistaTextFil():
    txtFil = "./husdjursLista.txt"
    finnsFil = os.path.isfile(txtFil)
    if finnsFil:
        husdjurTXT = open(txtFil, "r")
        husdjurSträng = husdjurTXT.readline()
        if husdjurSträng == '':
            husdjurTXT = open(txtFil, "w")
            husdjurTXT.write("Exempeldjur" + ' ' + str(100) + ' ' + str(100) + '\n')
    else:
        husdjurTXT = open(txtFil, "w")
        husdjurTXT.write("Exempeldjur" + ' ' + str(100) + ' ' + str(100) + '\n')


def main():
    """Ingen parameter, huvudfunktion, hämtar husdjurslistan och kor programmet.
    """
    kollaHudjurslistaTextFil()
    körPetRobo(hämtaHusdjur())


main()
"""Globalt anrop av huvudfunktion.
"""