phrase1 = input("Entrer une phrase : ").upper()
phrase2 = input('Entrer une autre phrase :').upper()
phrase = phrase1 + phrase2
voyelles , spéciaux = 'AEIOUY' , "!" 
print(phrase," a une longueur de",len(phrase))
for car in phrase(len(phrase)):
    if car in voyelles:
        print(car,'est une voyelle ')
    elif car not in spéciaux:
        print(car,' est une consonne .')
