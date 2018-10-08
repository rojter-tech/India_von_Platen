import random

# En klass som beskriver ett virtuellt husdjur.
# Attribut:
#    namn - djurets nanm
#    skick - ett heltal som beskriver djurets skick


class Husdjur:

    # Konstruktorn, initierar attributen namn och skick.
    def __init__(self, djurnamn):
        self.namn = djurnamn
        self.skick = random.randrange(-5,6)
        
    # För utskrift av ett objekt med print
    def __str__(self):
        return self.namn + "*" + str(self.skick)
    
#  -------  Här slutar Husdjursklassen ---------


# En funktion för utskrift av listan
def skrivListan(listan):
    for o in listan:
        print(o, end=" ")
    print("\n")


#  --------  Här börjar huvudprogrammet ---------
def main():
    djurlista = [Husdjur("Missan"), Husdjur("Blixten"), Husdjur("Fido"), Husdjur("Miso")]

    print("Så här ser listan ut från början:")
    skrivListan(djurlista)

    djurlista.sort(key = lambda husdjur:husdjur.namn)
    print("Nu är listan sorterad efter namn, i bokstavsordning:")
    skrivListan(djurlista)
        
    djurlista.sort(key = lambda husdjur:husdjur.skick)
    print("Nu är listan sorterad efter skick, i stigande ordning:")
    skrivListan(djurlista)
        
    djurlista.sort(key = lambda husdjur:husdjur.skick)
    djurlista.reverse()
    print("Nu är listan sorterad efter skick, i fallande ordning:")
    skrivListan(djurlista)


# Vi lägger in huvudprogrammet i en funktion för att undvika globala variabler.
main()