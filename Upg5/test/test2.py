def skapaLista(namnLista,poangLista):
    resultatLista = {}
    for i in range(len(namnLista)):
        resultatLista[namnLista[i]] = poangLista[i]
    return resultatLista


def sorteraLista(resultatLista):
    def andraVärdet(listelement):
        return listelement[1]
    sorteradResultatLista = sorted(resultatLista.items(), key = andraVärdet, reverse = True)
    return sorteradResultatLista


def skrivUtLista(sorteradResultatLista):
    for i in range(len(sorteradResultatLista)):
        namn = sorteradResultatLista[i][0]
        poang = str(sorteradResultatLista[i][1])
        print(namn + " fick " + poang + " poang")    


def main():
    namnLista = ['Erik','Bosse','Gregor','Adam']
    poangLista = [2,1,45,8]
    resultatLista = skapaLista(namnLista,poangLista)
    sorteradResultatLista = sorteraLista(resultatLista)
    skrivUtLista(sorteradResultatLista)


main()

