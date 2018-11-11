namnLista = ['Erik','Bosse','Gregor','Adam']
poangLista = [2,1,45,8]
resultatLista = {}
for i in range(len(namnLista)):
    resultatLista[namnLista[i]] = poangLista[i]

sorteradeResultatLista = sorted(resultatLista.items(), key=lambda x: x[1], reverse = True)

for i in range(len(sorteradeResultatLista)):
    namn = sorteradeResultatLista[i][0]
    poang = str(sorteradeResultatLista[i][1])
    print(namn + " fick " + poang + " poang")
