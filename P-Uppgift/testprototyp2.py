class Biljett:
    
    def __init__(self, sträcka, avgånstid, plats, ägare):
        self.sträcka = sträcka
        self.avgångstid = avgångstid
        self.plats = plats
        self.ägare = ägare
        

    def __repr__():
        return "PLATSBILJETT\n" + self.sträcka + "\n" + "Plats " + self.plats


def bokaBiljett(plats):

    filnamn = "biljett_" + plats + ".txt" 
    biljett = Biljett(sträcka, avgånstid, plats, ägare)

    
    with open(filnamn, "w") as file:
        file.write(biljett)
        

def hanteraBiljett(biljett):

    print("Boka biljett: ")
    var = ("Vart vill du åka?: ")
    tid = int(input("När vill du åka?: "))
    plats = str(input("Vilken plats vill du ha?: "))
    namn = str(input("Vad heter du?: "))

    bokaBiljett(plats)
    
        
def meny():

    biljett = Biljett(sträcka, avgånstid, plats, ägare)
    vad = str(input("Vad vill du göra?: "))
    
    
    while True: #Fixa felhantering
        if vad == "B":
            print("b")
            hanteraBiljett(biljett)
            bokaBiljett(plats)
        else:
            print("fel")

meny()
