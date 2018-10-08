with open('husdjur.txt', 'w') as file:
    file.write('Katt\n')
    file.write('Hund\n')

pets = []
with open('husdjur.txt', 'r', encoding="utf-8") as file:
    for line in file:
        pets.append(line)
print(pets)