# Kurs i programmeringsteknik
# India von Platen
# Paborjades 27/9- 2018
# DD100N


def checkaspelomgang():
    check = int(input("Vill du starta ny spelomgang? Ja(1), Nej(0): "))
    if check == 1:
        antalspelare = int(input("Hur manga spelare? : "))
        namnlista = ["null"] * antalspelare
        for i in range(antalspelare):
            namnlista[i] = str(input("Namn pa spelare " + str(i + 1) + ": "))
        nyspelomgang(namnlista)


def nyspelomgang(namnlista):                    # Skapar de filer som behovs vid ny spelomgang
    with open("namnlista.txt", "w") as file:    # Skapar en namnlista.txt for att anvanda igen nar programmet avslutas
        file.write(" ".join(namnlista))         # Skriver ut namnlistan pa en rad med mellanslag emellan
    with open("resultatFil.txt", "w") as file:
        for i in namnlista:                     # Skapar en resultatFil.txt med startvardet 0 for samtliga spelare
            file.write(i + " " + "fick" + " " + "0" + " " + "poang." + "\n")


def hamtanamn():                                             # Anvander namnlista.txt for att aterskapa listan med namn
    namnlista = open("namnlista.txt").readline().split(' ')
    return namnlista                                         # Returnerar listan sa att programmet kan anvanda den igen.


def nyaresultat(nyapersoner):

    file = open("resultatFil.txt")                         # Oppnar befintlig reultatfil
    with open("resultatFiltmp.txt", "w") as filetmp:       # Sager att det ska skrivas over till temporar resultatfil
        for i in nyapersoner:                              # Itererar "i" over listan nyapersoner
            inputlist = file.readline().split(' ')         # Delar upp radtext till en lista genom att separera ' '
            result = int(inputlist[2])                     # Gor om "tredje ordet" som ar en siffra till int
            nyapoang = str(input("Hur manga poang fick " + i + ":"))   # Anvandaren matar in nya poang
            newresult = result + int(nyapoang)               # Poangresultatet uppdateras som en int
            nyapoang = str(newresult)                        # Det nya resultatet gors om till strang
            filetmp.writelines(i + " fick " + nyapoang + " poang\n")  # Skriver in nya resultatet i temporar resultatfil

    filetmp = open("resultatFiltmp.txt")                     # Oppnar temporar reultatfil
    with open("resultatFil.txt", "w") as file:               # Sager att det ska skrivas over till befintlig resultatfil
        for _ in nyapersoner:                                #
            file.writelines(filetmp.readline())              # Skriver over nya resultatet i befintlig resultatfil


def spelanu(namnlista):
    vad = int(input("Vad vill du gora?(1,2 eller 3):"))

    while True:
        if vad == 0:
            vad = int(input("Vad vill du gora?(1,2 eller 3): "))
        elif vad == 1:
            file = open("resultatFil.txt", "r")
            for line in file:
                print(line)
            file.close()
            vad = 0
        elif vad == 2:
            nyaresultat(namnlista)
            vad = 0
        elif vad == 3:
            print("Valkommen ater!")
            break


def main():
    checkaspelomgang()   # Anvandaren kan valja om den vill paborja en ny spelomgang, namn laggs till sparad textfil.

    print("Valkommen till den arliga pilkaststavlingen!")
    print("1.Visa resultat.\n\n2.Skriv in nya resultat.\n\n3.Spara och avsluta.\n")
    namnlista = hamtanamn()                                 # Hamtar namn fran sparad textfil
    spelanu(namnlista)


if __name__ == '__main__':          # Startar automatiskt huvudmetoden nar python-scriptet laddas.
    main()
