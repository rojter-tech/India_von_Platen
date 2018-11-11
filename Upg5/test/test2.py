def func(x):
    return x[1]

namnLista = ['Erik','Bosse','Gregor','Adam']
poangLista = [2,1,45,8]
resultatLista = {}
for i in range(len(namnLista)):
    resultatLista[namnLista[i]] = poangLista[i]

print(resultatLista.items())
sorteradeResultatLista = sorted(resultatLista.items(), key= func, reverse = True)

for i in range(len(sorteradeResultatLista)):
    namn = sorteradeResultatLista[i][0]
    poang = str(sorteradeResultatLista[i][1])
    print(namn + " fick " + poang + " poang")
