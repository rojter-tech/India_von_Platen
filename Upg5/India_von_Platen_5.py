# Kurs i programmeringsteknik
# India von Platen
# Påbörjades 27/9- 2018
# DD100N


def checkaSpelomgång():
    '''Frågar användaren om hen vill starta ny spelomgång, skapar lista, 
    Inparameter: ingenting

    Returnerar: inget'''
    check = int(input("Vill du starta en ny spelomgång? Ja(1), Nej(0): "))
    if check == 1:
        antalSpelare = int(input("Hur många spelare? : "))
        namnLista = ["null"] * antalSpelare
        for i in range(antalSpelare):
            namnLista[i] = str(input("Namn på spelare " + str(i + 1) + ": "))
        nySpelomgång(namnLista)
        

def nySpelomgång(namnLista):                    
    '''Skapar de filer som behövs vid en ny spelomgång, 

    Inparameter: en lista- namnLista

    Returnerar: inget'''
    with open("namnLista.txt", "w") as file:
        file.write(" ".join(namnLista))
    with open("resultatFil.txt", "w") as file:
        for i in namnLista:
            file.write(i + " " + "fick" + " " + "0" + " " + "poäng." + "\n")


def hämtaNamn():
    '''Öppnar en namnlista.txt för att återskapa listan med namn, läser av listan,

    Inparameter: ingenting

    Returnerar: en lista- namnLista'''
    file = open("namnLista.txt")
    readthisline = file.readline()
    namnLista = readthisline.split(' ')
    namnLista[-1] = namnLista[-1].split('\n')[0]
    return namnLista                             

def hämtaResultat(namnLista):
    resultatLista = [None] * len(namnLista)
    with open("resultatFiltmp.txt", "r") as fil:
        for i in range(len(namnLista)):
            readthisline = fil.readline()
            inputlist = readthisline.split(' ')
            result = int(inputlist[2])
            resultatLista[i] = result
    return resultatLista


def nyaResultat(nyaPersoner):                                
    '''
Läser in nya resultat från spelare,
    Inparameter: nyaPersoner- 

    Returnerar: inget'''

    resultatLista = [None] * len(nyaPersoner)
    
    k = 0
    
    file = open("resultatFil.txt")                           
    with open("resultatFiltmp.txt", "w") as filetmp:
        for i in nyaPersoner:                                
            readthisline = file.readline()                   
            inputlist = readthisline.split(' ')             
            result = int(inputlist[2])                       
            nyaPoäng = str(input("Hur många poäng fick " + i + ":"))   
            newResult = result + int(nyaPoäng)

            resultatLista[k] = newResult
            k += 1
            
            nyaPoäng = str(newResult)
            filetmp.writelines(i + " fick " + nyaPoäng + " poäng\n")  

    filetmp = open("resultatFiltmp.txt")                     
    with open("resultatFil.txt", "w") as file:                
        for i in nyaPersoner:                                
            readthisline = filetmp.readline()
            inputlist = readthisline.split(' ')
            result = int(inputlist[2])
            newResult = result
            nyaPoäng = str(newResult)
            file.writelines(i + " fick " + nyaPoäng + " poäng\n")

    return resultatLista

def läggTillPerson(namnLista, resultatLista1):
    nySpelare = input("Vad heter den nya spelaren?: ")
    nyttResultat = int(input("Vad fick hen för poäng?: "))
    resultatLista1[nySpelare] = nyttResultat
    with open("resultatFil.txt", "a") as file:
        file.write(str(nySpelare) + " fick " + str(nyttResultat) + " poäng\n")
    namnLista.append(nySpelare)
    return namnLista, resultatLista1


def skapaLista(namnLista,poängLista):
    resultatLista = {}
    for i in range(len(namnLista)):
        resultatLista[namnLista[i]] = poängLista[i]
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
    '''Huvudmeny, printar menyn, anropar flera metoder i programmet.

    Inparameter: ingenting
    Returnerar: inget'''
    
    checkaSpelomgång()   

    print("Välkommen till den årliga pilkaststävlingen!")
    print("\n1. Visa resultat.\n\n2. Skriv in nya resultat.\n\n3. Lägg till nya personer.\n\n4. Spara och avsluta.\n")
    namnLista = hämtaNamn()
    poängLista = hämtaResultat(namnLista)
    resultatLista1 = skapaLista(namnLista,poängLista)
    
    vad = int(input("Vad vill du göra?(1,2, 3 eller 4):"))

    while True:
        if vad == 0:
            vad = int(input("Vad vill du göra?(1,2, 3 eller 4): "))
        elif vad == 1:
            sorteradResultatLista = sorteraLista(resultatLista1)
            skrivUtLista(sorteradResultatLista)
            vad = 0
        elif vad == 2:
            resultatLista1 = nyaResultat(namnLista)
            
            vad = 0
        elif vad == 3:
            namnLista, resultatLista1 = läggTillPerson(namnLista, resultatLista1)
            vad = 0
        elif vad == 4:
            print("Välkommen åter!")
            break
           
main()
