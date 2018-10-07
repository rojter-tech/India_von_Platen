#Paborjad 19/9- 2018
#DD100N
#Kurs i prorgammeringsteknik

#For att rita ut spelplanen anvands Box Drawing Characters": https://en.wikipedia.org/wiki/Box-drawing_character


def skrivutspelplan(spelplan):#lagg till vad spelplan star for ?
    print('      A     B      C  ')
    print('  ┏━━━┳━━━┳━━━┓')
    radRaknare = 0
    for rad in spelplan:
        radRaknare += 1
        print(str(radRaknare) +' ┃', end=' ')
        for ruta in rad:
            print(' ' + ruta, end='  ')
            print('┃', end=' ')
        print()
        if radRaknare < 3:          #Efter sista raden vill vi inte gora detta
            print('  ┣━━━╋━━━╋━━━┫')
    print('  ┗━━━┻━━━┻━━━┛')          #Utan istallet detta


def kontrollerarader():
    """Kontrollerar om det finns tre likadana tecken pa nagon rad och returnerar da True, annars False
    Inparameter: spelplan (matris)
    Returvarde: True om det finns vinnare annars False (booleskt varde)
    """


def kontrollerakolumner(spelplan):
    for i in range(3):
        if ' ' not in [spelplan[0][i], spelplan[1][i], spelplan[2][i]]:
            if spelplan[0][i] == spelplan[1][i] == spelplan[2][i]:
                return True
            else:
                return False

    return False


def kontrolleradiagonaler(spelplan):
    #forsta diagonalen, uppe till vanster till nere till hoger
    if ' ' not in [spelplan[0][0], spelplan[1][1], spelplan[2][2]] and spelplan[0][0] == spelplan[1][1] == spelplan[2][2]:
        return True
    else:
        return False


def finnsvinnare(spelplan):
    if kontrollerakolumner(spelplan) or kontrolleradiagonaler(spelplan):
        return True
    else:
        return False


def oavgjort(spelplan):
    for rad in spelplan:
        for element in rad:
            if element ==' ':
                return False
    return False


def tolkainmatning(inmatning):
    bokstav = inmatning[0].upper() #Anvander .upper() for att gora om alla inmatade bokstaver till versaler
    rad = int(inmatning[1])-1
    if bokstav == 'A':
        kolumn = 0
    elif bokstav == 'B':
        kolumn = 1
    else:
        kolumn = 2
    return rad, kolumn


def spela(spelarNamn1, spelarNamn2):
    print("Da kor vi!")
    print("Ange de koordinater du vill lagga pa pa formatet A1, B3 osv.")
    spelplan = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    spelarLista = [spelarNamn1, spelarNamn2]
    vemsTur = 1
    while finnsvinnare(spelplan) == False:
        vemsTur = (vemsTur+1)% 2 #vemsTur ska aldrig bli 2, utan borja om igen pa 0, %-ar modul dvs resten vid heltals division.
        skrivutspelplan(spelplan)
        if vemsTur == 0:
            markor = 'X'
        else:
            markor = 'O'
        inmatning = input(str(spelarLista[vemsTur]) + "s tur att spela: ")
        rad,kolumn = tolkainmatning(inmatning)
        spelplan[rad][kolumn] = markor
        if oavgjort(spelplan) == True:
            skrivutspelplan(spelplan)
            print("Det blev oavgjort!")
            break

    if not oavgjort(spelplan):
        skrivutspelplan(spelplan)
        print("Grattis " + str(spelarLista[vemsTur]) + " du vann!")


def main():
    print("Hej och vakommen till Tre-i-rad!")
    spelarNamn1 = input("Vad heter spelare 1? ")
    spelarNamn2 = input("Vad heter spelare 2? ")
    spela(spelarNamn1, spelarNamn2)


if __name__ == '__main__':          # Startar automatiskt huvudmetoden nar python-scriptet laddas.
    main()

