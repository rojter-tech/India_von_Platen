# Kurs i programmeringsteknik
# India von Platen
# Påbörjad 14/9- 2018
# DD100N

print("Välkommen, här kan du hålla ordning på dina elevers längdhopp!")
print("")
print("Skriv in namnen på dina elever och längden på vardera hopp.")
print("")
ANTALELEVER = int(input("Hur många elever har hoppat?:"))
ANTALHOPP = int(input("Hur många gånger har vardera elev hoppat?:"))

namnLista = ANTALELEVER * [None]
elevHopp = ANTALHOPP * [None]
langdLista = ANTALELEVER * [None]

for i in range(ANTALELEVER):
    print("")
    inpt = input("Skriv in namnet på elev " + str(i+1) + ":")
    namnLista[i] = str(inpt)
    langdLista[i] = ANTALHOPP * [None]
    for j in range(ANTALHOPP):
        inpt = input("Skriv in hur långt " + namnLista[i] + " hoppade på hopp nummer " + str(j+1) + ":")
        langdLista[i][j] = float(inpt)
    print("")

allaResultat = {}
for i in range(ANTALELEVER):
    allaResultat.update({namnLista[i]: langdLista[i]})

bastaHopp = {}
for i in range(ANTALELEVER):
    bastaHopp.update({namnLista[i]: sorted(allaResultat[namnLista[i]])[-1]})

sistaHopp = {}
for i in range(ANTALELEVER):
    sistaHopp.update({namnLista[i]: langdLista[i][-1]})

vad = 0
while True:
    if vad == 0:
        print("###########################MENY###########################")
        print("# 1. Visa alla resultat.                                 #")
        print("# 2. Visa bästa hopp för varje elev.                     #")
        print("# 3. Visa hur långt det sista hoppet var för varje elev. #")
        print("# 4. Avsluta program.                                    #")
        print("##########################################################")
        print("")
        inpt = input("Välj vad du vill göra (1,2, 3 eller 4):")
        vad = int(inpt)

    elif vad == 1:
        print("")
        print("Det råkade visa sig att:")
        for i in range(ANTALELEVER):
            print(namnLista[i], "hoppade", end=' ')
            for prnt in allaResultat[namnLista[i]]:
                print(prnt, end=', ')
            print("meter pa sina " + str(ANTALHOPP) + " respektive hopp.")
        print("")
        vad = 5

    elif vad == 2:
        print("")
        print("Det kunde man inte tro men:")
        for i in range(ANTALELEVER):
            print(namnLista[i], "hoppade som längst", bastaHopp[namnLista[i]], "meter.")
        print("")
        vad = 5

    elif vad == 3:
        print("")
        print("Det visade sig tydligen att:")
        for i in range(ANTALELEVER):
            print(namnLista[i], "hoppade", sistaHopp[namnLista[i]], "meter på sitt sista hopp.")
        print("")
        vad = 5

    elif vad == 4:
        print("Tack, välkommen åter!")
        break

    elif vad == 5:
        inpt = input("Vill du visa något mer? (Ja[1] eller Nej[0]):")
        fortsatt = int(inpt)
        print("")
        if fortsatt == 1:
            vad = 0
        elif fortsatt == 0:
            vad = 4

    else:
        print("Du måste ange en siffra från 1 till 4.")
        inpt = input("Välj vad du göra (1,2,3 eller 4): ")
        vad = int(inpt)
