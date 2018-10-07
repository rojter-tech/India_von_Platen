import os
from tv import TV


#  --------------------  Här börjar huvudprogrammet -------------------- #

# Metod för att rensa skärmen från data mellan menybyten och variabelbyten (kanal och volym)
def clear():
    os.system('cls')


# Metod för att hämta och kontrollera TV data
def checktextfile():
    data = [''] * 4

    # Kontrollsats för att checka om tvdata.txt finns lokaliserad i samma mapp som pythonfilen
    if os.path.isfile('./tvdata.txt'):
        with open('tvdata.txt') as f:
            for line in f:
                data = line.split()

    # Om inte så skapa en textfil med initialdata
    else:
        file = open("tvdata.txt", "w")
        file.write("1 ")
        file.write("10 ")
        file.write("1 ")
        file.write("10")
        file.close()
        with open('tvdata.txt') as f:
            for line in f:
                data = line.split()

    return data


# Metod för att skriva över textfilen med senaste TV-data
def writedata(x_kanal, x_volym, y_kanal, y_volym):
    file = open("tvdata.txt", "w")
    file.write(x_kanal + " ")
    file.write(str(x_volym) + " ")
    file.write(y_kanal + " ")
    file.write(str(y_volym))
    file.close()


# Separat metod för "byte av kanal"-funtionen i menyn
def bytkanal(obj):
    ch_string = input("Ange kanal nummer: ")
    if ch_string.isdigit():
        ch = int(ch_string)
        while ch_string:
            if 0 < ch < 100:
                obj.bytKanal(ch_string)
                ch_string = ""
            else:
                print("Kanal ska vara mellan 1 till 99,")
                ch_string = input("försök igen: ")
                ch = int(ch_string)
    else:
        print("Du kan bara ange siffror som inmatningstecken!")
        bytkanal(obj)


# Själva programmet, huvudmetoden
def main():
    data = checktextfile()

    # Skapa TV-objekten med indata från textfil
    x = TV("Vardagsrums TV", data[0], int(data[1]))
    y = TV("Köks TV", data[2], int(data[3]))

    # Initialparametrar för huvudmenyn
    print("**Välkommen till TV-simulatorn***\n", "1.", x.namn, "\n", "2.", y.namn, "\n", "3. Avsluta")
    kontroll_menu = "1. Byt kanal\n2. Sänk ljudvolym\n3. Höj ljudvolym\n4. Gå till huvudmenyn"
    tv_val = input("Välj: ")

    # ------- While loop för menyhanteringen av huvudmenyn, när TV apparat ska väljas -------
    while tv_val:

        # Val av inre meny till Vardagsrums TV'n när den ska modifieras
        if tv_val[0] == "1":

            clear()
            print(x.namn, "\nKanal:", x.kanal, "\nLjudvolymen", x.volym, "\n")
            print(kontroll_menu)
            tv_kontroll = input("Välj: ")

            while tv_kontroll:
                if tv_kontroll[0] == "1":
                    bytkanal(x)
                    tv_kontroll = ""
                    tv_val = "1"
                elif tv_kontroll[0] == "2":
                    x.sankVolym()
                    tv_kontroll = ""
                    tv_val = "1"
                elif tv_kontroll[0] == "3":
                    x.hojVolym()
                    tv_kontroll = ""
                    tv_val = "1"
                elif tv_kontroll[0] == "4":
                    tv_kontroll = ""
                    clear()
                    print("**Välkommen till TV-simulatorn***\n", "1.", x.namn, "\n", "2.", y.namn, "\n", "3. Avsluta")
                    tv_val = input("Välj: ")
                else:
                    tv_kontroll = input("Fel val, försök igen: ")

        # Val av inre meny till Köks TV'n när den ska modifieras
        elif tv_val[0] == "2":

            clear()
            print(y.namn, "\nKanal:", y.kanal, "\nLjudvolymen", y.volym, "\n")
            print(kontroll_menu)
            tv_kontroll = input("Välj: ")

            while tv_kontroll:
                if tv_kontroll[0] == "1":
                    bytkanal(y)
                    tv_kontroll = ""
                    tv_val = "2"
                elif tv_kontroll[0] == "2":
                    y.sankVolym()
                    tv_kontroll = ""
                    tv_val = "2"
                elif tv_kontroll[0] == "3":
                    y.hojVolym()
                    tv_kontroll = ""
                    tv_val = "2"
                elif tv_kontroll[0] == "4":
                    tv_kontroll = ""
                    clear()
                    print("**Välkommen till TV-simulatorn***\n", "1.", x.namn, "\n", "2.", y.namn, "\n", "3. Avsluta")
                    tv_val = input("Välj: ")
                else:
                    tv_kontroll = input("Fel val, försök igen: ")

        # Stänger menyn
        elif tv_val[0] == "3":
            tv_val = ""

        # Ogiltigt val
        else:
            tv_val = input("Fel val, försök igen: ")
    # -------------------- While loop för menyhanteringen slutar här -------------------- #

    # Skriver data till textfil
    writedata(x.kanal, x.volym, y.kanal, y.volym)


#  --------------------  Här slutar huvudprogrammet -------------------- #


# Huvudprogrammet körs
main()
