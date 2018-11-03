# Titel: 'Har vi tid?' - kodskelett

# Uppgifts nr. 7

# Författare: Reuben Vas

# Datum: 2018-10-14



#Det här programmet hanterar mötesbokning i alla dess former.

#Användaren kan välja att skapa en ny träff eller delta i en redan skapad träff. Vid skapandet av en ny träff anger man

#namn på träffen och olika möjliga datum för den. Vid deltagandet av en redan skapad träff väljer man träffen som passar,

#sitt namn och den tid man kan av alla möjliga tider alternativt väljer om man kan alla tider eller inte. 

#Varje användares tider och träffar sparas i en fil så att man kan se vilka som kan delta.

#De sparas i en fil bredvid där upplägget är klasser med attributen: namn -str,

#föreslagna tider samt tillgängliga människor -list. Varje träff är en lista vars element är listor där det första elementet är datumet

#och de efterföljande namnen är deltagare som kan komma. Därefter får alla anmäla sig.

#När många anmält sig sker en summering där programmet tar fram det datum för en träff där flest anmält sig till och bestämmer det.

#Detta innebär också att denna träff försvinner från listan med möjliga träffar. När programmet avslutas sparas alla information till en fil.





#klassen:   Namn på träffen -str

#           Datum samt deltagare upplagt i lista där datum kommer först efterföljt av tillgängliga människor (blir flera listor i en lista sorterat efter datum)

#Denna klass används för strukturen på möten

class Meeting:

    def __init__(self, name, date, month, participants, participants_maybe=[]): 

        """Skapar en ny träff.

        Inparametrar: self, month, name (str), date (int), participants (lista där första elementet är datum och de andra deltagare)(list)"""

        self.name = name #namnet på träffen (string)

        self.date = date #datum i månaden då träffen infaller (int)

        self.month = month #månad då träffen infaller (string)

        self.participants = participants #deltagare i en lista (list)

        self.participants_maybe = participants_maybe #deltagare som svarar kanske på om de kan

        self.datum = str(date) + ' ' + month #GÖR OM TILL ENGELSKA

        

        

    def __repr__(self): 

        """Returnerar en sträng som beskriver mötet.

        Inparametrar: self

        Returnerar: en sträng som beskriver mötet"""

        return 'meeting name: ' + self.name + '\n\ndate:         ' + str(self.date) + ' ' + self.month + '\n\nparticipants: ' + self.sort_participants() + '\n\nMaybe:' + str(self.participants_maybe)





    def __lt__(self, other): #SORTERA EFTER MÅNADER OCH DATUM t.ex jan=1, feb=2 osv VIKTIGT VIKTIGT VIKTIGT (https://stackoverflow.com/questions/32290801/sort-a-list-of-dates-by-month-in-python)

        '''Används för att sortera de olika mötena efter namn ordning'''        

        if self.name < other.name:

            return True

        elif self.name == other.name:

            if self.date_digital() < other.date_digital():

                return True

        else:

            return False



    def date_digital(self):

        '''Gör om alla datum till digital enheter så att klasserna sedan kan sorteras efter datum

        Inparametrar: self

        Returnerar: datum (som kan användas vid sortering)'''

        from datetime import datetime,date

        d = int(self.date)

        months_of_year = ['januari', 'februari', 'mars', 'april', 'maj', 'juni', 'juli', 'augusti', 'september', 'oktober', 'november', 'december']

        for i in range(len(months_of_year)):

            if self.month.lower() == months_of_year[i]:

                m = int(i+1)

        y = 2018

        return date(y, m, d)

                                    



    def sort_participants(self):

        '''Sorterar deltagarna efter namn och gör om dem från en lista till en slinga.

        Inparameter: ingen

        Returnerar: namelist_string (deltagarlistan med namnen uppradade)'''

        self.participants.sort()    

        namelist_string = ''

        for participant in self.participants:

            namelist_string += participant + '\n                   '

        return namelist_string



    def sort_participants_maybe(self):

        '''Sorterar deltagarna efter namn och gör om dem från en lista till en slinga.

        Inparameter: ingen

        Returnerar: namelist_string (deltagarlistan med namnen uppradade)'''

        self.participants_maybe.sort()    

        namelist_string = ''

        for participant in self.participants_maybe:

            namelist_string += participant + '\n                              '

        return namelist_string







#------------------funktioner-----------------





def read_file():

    """ Läser möten från filen meetngs.txt till attributet Meetings.

    Parametrar: self

    Returnerar: lista med mötetn skapad med Meeting och lagt i Schedule"""

    file = open('meetings.txt', 'r')

    name = file.readline().strip()

    meetings_list = []

    while name:

        date = int(file.readline().strip()) 

        month = file.readline().strip()

        participants = file.readline().strip().split(' ')

        participants_maybe = file.readline().strip().split(' ')

        meeting_ = Meeting(name, date, month, participants, participants_maybe)

        meetings_list.append(meeting_)

        name = file.readline().strip()

    file.close()

    meetings_list.sort()    

    return meetings_list



def save_to_file(list_of_meetings):

    """ Skriver ut (lagrar) alla möten på filen meetings.txt 

    Parametrar: self

    Returnerar: inget """

    file = open('meetings.txt', 'w')

    list_of_meetings.sort()

    for meeting in list_of_meetings:

        file.write(meeting.name + '\n')

        file.write(str(meeting.date) + '\n')

        file.write(meeting.month + '\n')

        file.write(' '.join(meeting.participants) + '\n')

        file.write(' '.join(meeting.participants_maybe) + '\n')

    file.close()

    



def exist_digits(string):

    '''Känner av om strängen i inparametern innehåller siffror.

    Inparameter: string

    Returnerar: True eller False beroende på ifall det är en siffra eller ej i strängen'''

    return any(character.isdigit() for character in string)



def digits_in_name(intake):

    name = intake

    while True:

        if exist_digits(name):

            print('Notera att namnet inte får innehålla några siffror. Vänligen välj ett annat namn.')

            name = input('Ange namn: ')  

        else:

            break

    return name



def reasonable_name():

    '''Känner av ifall namnet är rimligt, i detta fall så att det inte innehåller några siffror. Det ersätter ockå mellanslag med "_".

    Inparametrar: inget

    Returnerar: namn'''

    name = input('\nAnge ditt namn: ')

    name = name.title()

    name = digits_in_name(name)

    name_list = list(name)

    for i in range(len(name_list)):

        if name_list[i] == ' ':

            name_list[i] = '_'

    name = ''.join(name_list)

        

    return name

            



def reasonable_month():

    months_of_year = ['januari', 'februari', 'mars', 'april', 'maj', 'juni', 'juli', 'augusti', 'september', 'oktober', 'november', 'december']

    i=0

    month = input('Månad: ')

    while i < len(months_of_year):

        if months_of_year[i] == month.lower():

            break

        elif i == len(months_of_year)-1:

            print(month.title() + ' är ingen riktig månad. Notera att Mötesbokaren endast accepterar riktiga månader. Vänligen ange en riktig månad.')

            month = input('Månad: ')

            i = 0

            continue

        i += 1

    return month



def integer(intake):

    '''Testar ifall inmatningen är ett heltal.

    Inparameter: inmatning

    Returnerar: True eller False beroende på om inmatningen är ett heltal eller ej.'''

    try:

        int(intake)

        return True

    except ValueError:

        return False



def choice_integer():

    '''Om det inmatade valet inte är ett heltal behöver användaren mata in det igen.

    Inparamter: inget

    Returnerar: val'''

    choice = (input('VAL: '))

    while not integer(choice):

        print('Notera att val måste vara ett giltigt heltal. Vänligen ange valet igen.')

        choice = (input('VAL: '))

    choice = int(choice)

    return choice



def date_integer():

    '''Om det inmatade datumet inte är ett heltal behöver användaren mata in det igen.

    Inparamter: inget

    Returnerar: dag'''

    date = (input('Dag: '))

    while not integer(date):

        print('Notera att datumet måste vara ett giltigt datum, dvs t.ex ett heltal. Vänligen ange datumet igen.')

        date = (input('Dag: '))

    date = int(date)

    return date



def reasonable_date(intake): 

    '''Känner av så att det inmatade datumet stämmer överens med det antal dagar som finns i den valda månaden

    Inparameter: mån

    Returnerar: dag'''

    date = date_integer()

    month_ = intake.lower()

    for month in ['januari', 'mars', 'maj', 'juli', 'augusti', 'oktober', 'december']:

        if month_ == month:

            while date < 1 or date > 31:

                print('Notera att ' + month_ + ' endast har datum mellan 1-31. Vänligen ange ett rimligt datum.')

                date = date_integer()    

    for month in ['april', 'juni', 'september', 'november']:

        if month_ == month:

            while date < 1 or date > 30:

                print('Notera att ' + month_ + ' endast har datum mellan 1-30. Vänligen ange ett rimligt datum.')

                date = date_integer()      

    if month_ == 'februari':

        while date < 1 or date > 28:

            print('Notera att ' + month_ + ' endast har datum mellan 1-28. Vänligen ange ett rimligt datum.')

            date = date_integer()

    return date



def valid_choice(intake):

    '''Känner av om valet är ett heltal och om det motsvarar ett av alternativen. Fyller inte inmatningen dessa villkor får användaren göra en ny inmatning.

    Inparameter: listan med alla alternativ, dvs alla träffars namn

    Returnerar: val'''

    choice = choice_integer()

    while choice < 1 or choice > len(intake):

        print('Valet är inte giltigt. Vänligen ange ett val mellan 1-' + str(len(intake)))

        choice = choice_integer()

    return choice



def choose_y_n(intake):

    '''Känner av om inmatningen är antingen "J" eller "N" annars behöver användaren göra en ny inmatning.

    Inparameter: inmatning

    Returenerar: val (J eller N)'''

    choice = intake[0].lower()

    while True:

        if choice == 'n' or choice == 'j':

            break

        else:

            print('Fel inmatning. Notera att Mötesbokaren endast accepterar "J" eller "N" som inmatning.')

            choice = input('Vänligen ange nytt val: ')[0].lower()

    return choice



def choice_y_n_m(intake):

    '''Känner av om inmatningen är antingen "J" eller "N" eller "K" annars behöver användaren göra en ny inmatning.

    Inparameter: inmatning

    Returenerar: val (J eller N)'''

    choice = intake[0].lower()

    while True:

        if choice == 'n' or choice == 'j' or choice == 'k':

            break

        else:

            print('Fel inmatning. Notera att Mötesbokaren endast accepterar "J", "N" eller "K" som inmatning.')

            choice = input('Vänligen ange nytt val: ')[0].lower()

    return choice

           

def name_creator():

    '''Vid skapandet av en ny träff tar denna funktion namn på skaparen till mötet

    Inparametrar: inget

    Returnerar: en deltagarlista där skaparen ännu så länge bara finns'''

    participants = []

    creator = reasonable_name() + '*'#Markerar så vi vet vem som skapade träffen 

    participants.append(creator.title()) 

    return participants



def design_conditions_meeting():

    '''Tar in information om träffan vid skapandet av den som t.ex namn och datum

    Inparametrar: inget

    Returnerar: namn på träffen, det datum som träffen infaller på, månad där träffen infaller'''

    name = input('\nNamn på träffen: ')

    name = digits_in_name(name)

    print('\nAnge månad och dag för när det preliminära datumet på träffen')

    month = reasonable_month()

    date = reasonable_date(month)

    return name, date, month



def set_preliminary_dates(list_of_meetings, name, participants):

    '''Låter användaren få lägga till fler preliminära datum för träffen

    Inparametrar: möteslista, namn, deltagare

    Returnerar: möteslista (den är uppdaterad efter de nya datumen'''

    while True:

        choice = input('Lägga till fler preliminära datum? (J/N): ')

        choice = choose_y_n(choice)

        if choice[0].lower() == 'j':

            print('\nAnge månad och dag för preliminärt datum')

            month = reasonable_month()

            date = reasonable_date(month)

            new_meeting = Meeting(name.title(), date, month, participants)

            list_of_meetings.append(new_meeting)

        elif choice[0].lower() == 'n':

            break

    return list_of_meetings

    



def create_new_meeting(list_of_meetings):

    '''Skapar en ny träff genom att användaren får mata in detaljer om träffen.

    Inparametrar: möteslista

    Returnerar: möteslista (uppdaterad med de nya träffarna)'''

    print('\nSKAPA NY TRÄFF')

    participants = name_creator()

    name, date, month = design_conditions_meeting()

    new_meeting = Meeting(name.title(), date, month, participants)

    list_of_meetings.append(new_meeting)

    list_of_meetings = set_preliminary_dates(list_of_meetings, name, participants)

    return list_of_meetings



def advertise_meetings(intake):

    '''Skapar en lista med alla mötens namn

    Inparametrar: möteslista

    Returnerar: träffar_namn (listan med namnen på alla träffar)'''

    list_of_meetings = intake

    list_of_meetings.sort()

    meetings_name = []

    for meeting in list_of_meetings:

        if meeting.name not in meetings_name:

            meetings_name.append(meeting.name)

    return meetings_name





def print_selectable_meetings(meetings_list_intake, meetings_name_intake):

    '''Skriver ut alla träffarnas namn och låter användaren få välja en av dessa. Därefter sparar den alla preliminära datum av detta möte i en separat lsita.

    Inparametrar: möteslista, träffar_namn

    Returnerar: vald_träff ( en lista där alla möten med samma namn men olika datum ligger )'''

    list_of_meetings = meetings_list_intake

    meetings_name = meetings_name_intake

    for i in range(len(meetings_name)):

        print(str(i+1) + '. ' + meetings_name[i])

    choice = valid_choice(meetings_name)

    chosen_meeting = []

    for i in range(len(list_of_meetings)):

        if list_of_meetings[i].name == meetings_name[int(choice)-1]:

            chosen_meeting.append(list_of_meetings[i])

    return chosen_meeting



def list_dates_chosen_meeting(intake):

    '''Listar upp datumen för den träff som användaren valt.

    Inparamtrar: intake

    Returnerar: inget'''

    chosen_meeting = intake

    print('\nSummerar träffen ' + chosen_meeting[0].name + '.\n')

    print('Preliminära datum: ', end='') 

    for i in range(len(chosen_meeting)):

        print(str(i+1) + '. ' + chosen_meeting[i].datum, end='\n                   ')

    print()



def which_dates_participate(chosen_meeting, participant):

    available_dates, maybe_available_dates = '', ''

    i = 0

    while i < len(chosen_meeting):

        choice = input('\nTillgänglig den ' + chosen_meeting[i].datum + '? (Ja/Nej/Kanske): ')

        choice = choice_y_n_m(choice)#JA NEJ ELLER KANSKE

        if choice[0].lower() == 'j':

            chosen_meeting[i].participants.append(participant.title())

            available_dates += chosen_meeting[i].datum + ', '

            i += 1

        elif choice[0].lower() == 'k':

            chosen_meeting[i].participants_maybe.append(participant.title())

            maybe_available_dates += chosen_meeting[i].datum + ', '



            i += 1

        elif choice[0].lower() == 'n':

            i += 1

    return chosen_meeting, available_dates, maybe_available_dates



def add_preliminary_dates(chosen_meeting_list_intake, participant_intake): 

    '''Frågar användaren vilka av de preliminära datumen som hen kan deltaga på.

    Inparamtrar: vald_träff, deltagare

    Returnerar: vald_träff (uppdaterad med deltagarens namn tillagd bland deltagarna)'''

    chosen_meeting = chosen_meeting_list_intake

    participant = participant_intake

    choice = input('Har du möjlighet att delta vid samtliga preliminära dagar? (Ja/Nej/Kanske): ') #NYA DELTAGARENS NAMN LÄGGS TILL DET ANTAL GÅNGER SOM DEN KAN PÅ TILLFÄLLEN PÅ VARJE DATUM. Gäller vid nyskapade möten

    choice = choice_y_n_m(choice)

    available_dates, maybe_available_dates = '', ''

    if choice[0].lower() == 'j':

        for meeting in chosen_meeting:

            meeting.participants.append(participant.title())

            available_dates += meeting.datum + ', '

    elif choice[0].lower() == 'k':

        for meeting in chosen_meeting:

            meeting.participants_maybe.append(participant.title())

            maybe_available_dates += meeting.datum + ', '

    elif choice[0].lower() == 'n': 

        if len(chosen_meeting) > 1:

            chosen_meeting, available_dates, maybe_available_dates = which_dates_participate(chosen_meeting, participant)

    if len(available_dates) > 0:

        available_dates = available_dates[:len(available_dates)-2]

        print('\nAnmäler till datumen: ' + available_dates)

    if len(maybe_available_dates) > 0:

        maybe_available_dates = maybe_available_dates[:len(maybe_available_dates)-2]

        print('\nAnmäler som kanske till datumen: ' + maybe_available_dates)

        

    for meeting_i in chosen_meeting:#DENNA LOOP LÖSER OVAN BESKRIVEN BUGG

        for i in range(len(meeting_i.participants)-1):

            if meeting_i.participants[i] == meeting_i.participants[len(meeting_i.participants)-1]:

                meeting_i.participants.remove(meeting_i.participants[i])           

    return chosen_meeting



def update_list_of_meetings(chosen_meeting_list_intake, list_of_meetings_intake):

    '''Sparar över mötena med den uppdaterade deltagarlistan över de redan existerande mötena.

    Inparametrar: vald_träff, möteslista

    Returnerar: möteslista (uppdaterad med deltagaren tillagd)'''

    chosen_meeting = chosen_meeting_list_intake

    list_of_meetings = list_of_meetings_intake

    for i in range(len(chosen_meeting)):

        for a in range(len(list_of_meetings)):

            if chosen_meeting[i].name == list_of_meetings[a].name:

                if chosen_meeting[i].datum == list_of_meetings[a].datum:

                    list_of_meetings[a] = chosen_meeting[i]

    return list_of_meetings

    

def participate_in_existing_meeting(list_of_meetings_intake):

    '''Låter användaren få välja en träff och preliminöra datum på denna träffen där hen kan delta på.

    Inparametrar: möteslista

    Returnerar: uppdaterade_möten (möteslistan uppdaterad'''

    list_of_meetings = list_of_meetings_intake

    participant = reasonable_name()

    meetings_name = advertise_meetings(list_of_meetings)

    print('\nVänligen välj en utav följande träffar att delta i:')

    chosen_meeting = print_selectable_meetings(list_of_meetings, meetings_name)

    list_dates_chosen_meeting(chosen_meeting)

    chosen_meeting = add_preliminary_dates(chosen_meeting, participant)

    updated_meetings = update_list_of_meetings(chosen_meeting, list_of_meetings)

    return updated_meetings

    



def  list_dates(intake):

    '''Listar upp antalet anmälda på alla preliminära datum för en vald träff och frågar användaren om hen vill fortsätta summeringen.

    Inparametrar: vald_träff_summera

    Returnerar: val: j eller n'''

    meeting_summarize = intake

    print('\nSummerar träffen ' + meeting_summarize[0].name + '.\n')   

    number_registered_participants_str = ''

    for meeting in meeting_summarize:

        number_registered_participants_str += str(len(meeting.participants)) + ' personer anmälda den ' + meeting.datum + '\n                         '

    print('\nAntal anmälda per datum: ' + number_registered_participants_str)

    choice = input('Summera träffen ' + meeting_summarize[0].name + '? (J/N): ')

    choice = choose_y_n(choice)

    return choice



def number_participants_by_dates(intake):  

    '''Gör en lista med det antal som anmält sig till varje tillfälle och tar fram det index där antalet är flest.

    Inparamtetrar: vald_träff_summera

    Returnerar: flest_antal_index'''

    chosen_meeting = intake         

    number_registered_participants = []

    for meeting in chosen_meeting:

        number_registered_participants.append(len(meeting.participants))

    return number_registered_participants



def determine_appropriate_date(chosen_meeting_list_intake, number_registered_participants_intake):

    '''Beskriver det preliminära datum som passar bäst för mötet och frågar användaren om hen vill fastställa detta datum.

    Inparametrar: vald_träff_summera, max_deltagare_index

    Returnerar: val: j eller n'''

    chosen_meeting = chosen_meeting_list_intake

    number_registered_participants = number_registered_participants_intake

    biggest_amount_index = number_registered_participants.index(max(number_registered_participants))



    if number_registered_participants.count(max(number_registered_participants)) > 1:

        biggest_meetings_indexes = []

        for i in range(len(number_registered_participants)):

            if number_registered_participants[i] == number_registered_participants[biggest_amount_index]:

                biggest_meetings_indexes.append(i)

        maybes_meeting = []

        for index in biggest_meetings_indexes:

            maybes_meeting.append(chosen_meeting[index])   

        maybes_meeting_length = []

        for meeting in maybes_meeting:

            maybes_meeting_length.append(len(meeting.participants_maybe))  

        if maybes_meeting_length.count(max(maybes_meeting_length)) > 1:

            print('\nFlera datum har lika många anmälda. Vänligen välj ett av dessa: ')

            for i in range(len(maybes_meeting)):

                if len(maybes_meeting[i].participants_maybe) == max(maybes_meeting_length):

                    print(str(i+1) + '. ' + maybes_meeting[i].datum)

            val = valid_choice(maybes_meeting)

            most_suitable_meeting = maybes_meeting[val-1]

        else:

            most_suitable_meeting = maybes_meeting[maybes_meeting_length.index(max(maybes_meeting_length))] 

    else:                                            

        most_suitable_meeting = chosen_meeting[biggest_amount_index]



    return most_suitable_meeting



def describe_chosen_meeting(intake):

    '''Beskriver det datum som passar bäst för summeringen.

    Inparameter: 'intake' dvs det möte som passar bäst

    Returnerar: val, most_suitable_meeting'''

    most_suitable_meeting = intake

    print('\nDet datum som passar samtliga bäst är och har valts: ' + most_suitable_meeting.datum)

    print('I dagsläget kan ' + str(len(most_suitable_meeting.participants)) + ' personer definitivt delta och ' + str(len(most_suitable_meeting.participants_maybe)) + ' eventuellt delta under detta datum')   

    print('\nAnmälda deltagare: ' + most_suitable_meeting.sort_participants())

    if len(most_suitable_meeting.participants_maybe) > 1:

       print('Anmälda deltagare som kanske: ' + most_suitable_meeting.sort_participants_maybe()) 

    val = input('\n\nFastställ detta datum för denna träff? (J/N): ')

    val = choose_y_n(val)

    return val, most_suitable_meeting



def remove_non_current_dates(list_of_meetings_intake, chosen_meeting_list_intake):

    '''Tar bort alla möten av ett visst specifikt namn från möteslistan.

    Inparametrar: möteslista, vald_träff_summera

    Returnerar: möteslista'''

    list_of_meetings = list_of_meetings_intake

    chosen_meeting = chosen_meeting_list_intake

    

    i = 0

    while i < len(list_of_meetings):

        if list_of_meetings[i].name == chosen_meeting[0].name:

            list_of_meetings.remove(list_of_meetings[i])

            i -= 1

        i += 1

    return list_of_meetings



def determine_other_final_date(chosen_meeting_list_intake):

    '''Låter användaren få välja vilket datum som ska användas som slutgiltigt datum.

    Inparamtrar: vald_träff_summera

    Returnerar: val - j eller n'''

    chosen_meeting = chosen_meeting_list_intake

    print('\nVilket datum vill du faställa som slutgiltigt? :')

    for i in range(len(chosen_meeting)):

        print(str(i+1) + '. ' + chosen_meeting[i].datum)

    choice = valid_choice(chosen_meeting)

    return choice



def list_founders(list_of_meetings_intake):

    '''Gör en lista med alla mötens namn och dess skapare.

    Inparametrar: list_of_meetings_intake

    Returnerar: lista med mötets namn efterföljt av dess skapare'''

    list_of_meetings = list_of_meetings_intake

    founders_list = []

    for meeting in list_of_meetings:

        if meeting.name not in founders_list:

            for participant in meeting.participants:

                if participant[len(participant)-1:] == '*':

                    founders_list.append(meeting.name)

                    founders_list.append(participant)

    return founders_list

            

                

def name_of_founder(list_of_meetings_intake):

    '''Känner av om namnet som användaren matat in stämmer överens med något av namnen på skaparna av mötena. Om så är fallet kommer användaren bara ha möjlighet att summera det mötet som namnet stämmer överens med.

    Inparameter: list_of_meetings_intake

    Returnerar: chosen_meeting'''

    list_of_meetings = list_of_meetings_intake

    meeting_founder_list = list_founders(list_of_meetings)

    name = reasonable_name()

    name += '*'

    selectable_meetings = []

    if name in meeting_founder_list:

        if meeting_founder_list.count(name) > 1:

            print('\nNotera att detta namn använts som skapare för flera möten.')

            print('\nVilket möte vill du summera? : ')

            n = 1

            for i in range(len(meeting_founder_list)):

                if meeting_founder_list[i] == name:

                    print(str(n) + '. ' + meeting_founder_list[i-1])

                    selectable_meetings.append(meeting_founder_list[i-1])

                n += 1

            val = valid_choice(selectable_meetings)

            for i in range(len(selectable_meetings)):

                if val == i+1:

                    chosen_meeting = selectable_meetings[i]

        else:

            for i in range(len(meeting_founder_list)):

                if name == meeting_founder_list[i]:

                    chosen_meeting = meeting_founder_list[i-1]

    else:

        print('Det namn som angavs stämmer inte överens med någon skaparna.')

        print('\nÅTERGÅR TILL HUVUDMENY')

        main_menu(list_of_meetings)

        

    return chosen_meeting

               

def choose_meeting_by_name(list_of_all_meetings_intake, name_of_meeting_intake):

    list_of_all_meetings = list_of_all_meetings_intake

    name_of_meeting = name_of_meeting_intake

    chosen_meeting_list = []

    for i in range(len(list_of_all_meetings)):

        if list_of_all_meetings[i].name == name_of_meeting:

            chosen_meeting_list.append(list_of_all_meetings[i])

    return chosen_meeting_list





        



def summarize_meeting(list_of_meetings_intake):

    '''Låter användaren få bestämma ett slutgiltigt datum till en träff.

    Inparamtetrar: möteslista

    Returnerar: möteslista (uppdaterad)'''

    list_of_meetings = list_of_meetings_intake

    chosen_meeting_name = name_of_founder(list_of_meetings)

    chosen_meeting_list = choose_meeting_by_name(list_of_meetings, chosen_meeting_name)

    choice = list_dates(chosen_meeting_list)

    if choice[0].lower() == 'j':#FELHANTERING ja/nej-fråga

        number_registered_participants = number_participants_by_dates(chosen_meeting_list)



        most_suitable_meeting = determine_appropriate_date(chosen_meeting_list, number_registered_participants)

        

        choice, most_suitable_meeting = describe_chosen_meeting(most_suitable_meeting)

        list_of_meetings = remove_non_current_dates(list_of_meetings, chosen_meeting_list)                   

        if choice[0].lower() == 'j':                    

            list_of_meetings.append(most_suitable_meeting) 

            print('\nDen ' + most_suitable_meeting.datum + ' är fastställt.')

        elif choice[0].lower() == 'n':

            choice = determine_other_final_date(chosen_meeting_list)

            list_of_meetings.append(chosen_meeting_list[int(choice)-1])

            print('Den ' + chosen_meeting_list[int(choice)-1].datum + ' är fastställt.\n')

    elif choice[0].lower() == 'n':

        pass

    return list_of_meetings

        

        

def main_menu(list_of_meetings_intake):

    '''Huvudmenyn för programmet. Användaren kan välja att: Skapa ny träff, Delta i en befintlig träff, Summera en träff eller Avsluta

    Inparametrar: möteslista

    returnerar: inget'''



    list_of_meetings = list_of_meetings_intake

    

    print('\n\nMÖTESBOKAREN 1.0\nMötesbokarprogrammet för kollegorna, kompisgänget eller varför inte föreläsningen.')

    

    print('\n\nVänligen välj ett av följande alternativ:\n1. Skapa ny träff\n2. Delta i en befintlig träff\n3. Summera en träff\n4. Avsluta')

    number_of_choices=[1, 2, 3, 4]

    choice = valid_choice(number_of_choices)

    if choice == 1:

        list_of_meetings = create_new_meeting(list_of_meetings)

                            

    elif choice == 2:

        print('\nDELTA I BEFINTLIG TRÄFF\n')

        list_of_meetings = participate_in_existing_meeting(list_of_meetings)

            



    elif choice == 3:

        print('\nSUMMERA TRÄFF\n')

        list_of_meetings = summarize_meeting(list_of_meetings)



    elif choice == 4:

        save_to_file(list_of_meetings)

        print('\nSPARAR OCH AVSLUTAR.')

        raise SystemExit

                

    print('\n\nÅTERVÄNDER TILL HUVUDMENYN')           

    main_menu(list_of_meetings)                

                    





            

            

            

        

        

    



# Huvudprogram



    """Algoritm:

    1. Hälsar välkommen till 'Har vi tid?'

    2. Läser in filen med mötena och skapar objekt till av meeting som läggs i attributet Schedule till ett Libary-objekt

    3. Presenterar en meny

    4. Låter användare välja ett menyval eller att avsluta

    5. Om användaren inte väljer att avsluta, utför det valda menyvalet

    6. Upprepar steg 3-5, tills det att användaren väljer att avsluta

    7. Sparar till fil

    8. Avslutar programmet

    """







main_menu(read_file())

