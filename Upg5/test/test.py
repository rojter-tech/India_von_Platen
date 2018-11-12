namnLista = ['Erik','Bosse','Gregor','Adam']
poangLista = [2,1,45,8]
resultatLista = {}
for i in range(len(namnLista)):
    resultatLista[namnLista[i]] = poangLista[i]

sorteradResultatLista = sorted(resultatLista.items(), key=lambda x: x[1], reverse = True)

for i in range(len(sorteradResultatLista)):
    namn = sorteradResultatLista[i][0]
    poang = str(sorteradResultatLista[i][1])
    print(namn + " fick " + poang + " poang")
