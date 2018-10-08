# En klass som beskriver ett virtuellt husdjur.
# Attribut:
#    namn - djurets nanm
#    skick - ett heltal som beskriver djurets skick
class Husdjur:

    # Konstruktorn, initierar attributen namn och skick.
    def __init__(self, djurnamn):
        self.namn = djurnamn
        self.skick = 0

    # Visar husdjurets namn och skick
    def visaSkick(self):       
        print(self.namn, "är ", end=" ")
        if self.skick > 5:
            print("glad: (^_^)")
        elif self.skick > 0:
            print("trött: (T_T)")
        else:
            print("hungrig: ('o')")
        print

    # Ger husdjuret bannor. Skick minskas.
    def banna(self):
        print()
        print("- Fy på dig", self.namn, "!")
        self.skick -= 3

    # Ger husdjuret mat. Skick ökar.
    def mata(self, mat):
        print()
        for i in range(mat):
            print("GLUFS", end=" ")
        self.skick += mat

    # Leker med husdjuret. Skick kan öka eller minska.
    def leka(self):
        print()
        if self.skick < 0:
            self.skick -= 1
            print(self.namn, " vill inte leka.")
        else:
            self.skick += 1
            print("~~~~~~~~~~~ WHEEEEEEE! ~~~~~~~~~~~")

    # Skriver ut avskedet.
    def avsked(self):
        print()
        print("Hejdå,", self.namn, "kommer att sakna dig!")

# Här slutar Husdjursklassen


#  --------  Här börjar huvudprogrammet -----------
def main():
    djurnamn = input("Vad vill du döpa ditt husdjur till? ")
    djur = Husdjur(djurnamn)
    djur.visaSkick()
    svar = input(" Vill du \n  banna \n  mata \n  leka med \n ditt husdjur? " )
    while svar:
        if svar[0]=="m":
            bullar = int(input("Hur många bullar? "))
            djur.mata(bullar)    
        elif svar[0]=="b":
            djur.banna()
        elif svar[0]=="l":
            djur.leka()
        else:
            print("Hursa? ")
        djur.visaSkick()
        svar = input(" Vill du \n  banna \n  mata \n  leka med \n ditt husdjur? " )
    djur.avsked()

# Vi lägger in huvudprogrammet i en funktion för att undvika globala variabler.
main()