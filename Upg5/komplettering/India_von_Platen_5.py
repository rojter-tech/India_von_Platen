# Kurs i programmeringsteknik
# India von Platen
# Påbörjades 27/9- 2018
# DD100N


def checkaSpelomgång():
    check = int(input("Vill du starta en ny spelomgång? Ja(1), Nej(0): "))
    if check == 1:
        antalSpelare = int(input("Hur många spelare? : "))
        namnLista = ["null"] * antalSpelare
        for i in range(antalSpelare):
            namnLista[i] = str(input("Namn på spelare " + str(i + 1) + ": "))
        nySpelomgång(namnLista)


def nySpelomgång(namnLista):                      # En parameter, skapar de filer som behövs vid ny spelomgång
    with open("namnLista.txt", "w") as file:      # Skapar en namnlista.txt för att använda igen om programmet avslutas
        file.write(" ".join(namnLista))           # Skriver ut namnlistan på en rad med mellanslag emellan
    with open("resultatFil.txt", "w") as file:
        for i in namnLista:                       # Skapar en resultatFil.txt med startvärdet 0 for samtliga spelare
            file.write(i + " " + "fick" + " " + "0" + " " + "poäng." + "\n")


def hämtaNamn():                                  # Använder namnlista.txt för att återskapa listan med namn
    file = open("namnLista.txt")
    readthisline = file.readline()
    namnLista = readthisline.split(' ')
    namnLista[-1] = namnLista[-1].split('\n')[0]
    return namnLista                              # Returnerar listan så att man kan använda den i programmet igen.


def nyaResultat(nyaPersoner):                                #En parameter

    file = open("resultatFil.txt")                           # Öppnar befintlig resultatfil
    with open("resultatFiltmp.txt", "w") as filetmp:         # Säger att det ska skrivas över till temporär resultatfil
        for i in nyaPersoner:                                # Itererar "i" över listan nyapersoner
            readthisline = file.readline()                   # Rad for rad i befintlig reultatfil
            inputlist = readthisline.split(' ')              # Delar upp radtext i ord genom att separera ' '
            result = int(inputlist[2])                       # Gör om "tredje ordet" som ar en siffra till int
            nyaPoäng = str(input("Hur många poäng fick " + i + ":"))   # Användaren matar in nya poäng
            newResult = result + int(nyaPoäng)               # Poängresultatet uppdateras som en int
            nyaPoäng = str(newResult)                        # Det nya resultatet görs om till sträng
            filetmp.writelines(i + " fick " + nyaPoäng + " poäng\n")  # Skriver in nya resultatet i temporär resultatfil

    filetmp = open("resultatFiltmp.txt")                     # Öppnar temporär resultatfil
    with open("resultatFil.txt", "w") as file:               # Säger att det ska skrivas över till befintlig resultatfil
        for i in nyaPersoner:                                #
            readthisline = filetmp.readline()                #
            inputlist = readthisline.split(' ')              #
            result = int(inputlist[2])
            newResult = result                               ########################## SE OVAN #########################                               #
            nyaPoäng = str(newResult)                        
            file.writelines(i + " fick " + nyaPoäng + " poäng\n") # Skriver in  nya resultatet i befintlig resultatfil


def main():
    checkaSpelomgång()   # Användaren kan välja om den vill påbörja en ny spelomgång, namn läggs till sparad textfil.

    print("Välkommen till den årliga pilkaststävlingen!")
    print("1.Visa resultat.\n\n2.Skriv in nya resultat.\n\n3.Spara och avsluta.\n")
    namnLista = hämtaNamn()                                 # Hämtar namn fran sparad textfil
    vad = int(input("Vad vill du göra?(1,2 eller 3):"))

    while True:
        if vad == 0:
            vad = int(input("Vad vill du göra?(1,2 eller 3): "))
        elif vad == 1:
            file = open("resultatFil.txt", "r")
            for line in file:
                print(line)
            file.close()
            vad = 0
        elif vad == 2:
            nyaResultat(namnLista)
            vad = 0
        elif vad == 3:
            print("Välkommen åter!")
            break


if __name__ == '__main__':          # Startar automatiskt huvudmetoden när python-scriptet laddas.
    main()
