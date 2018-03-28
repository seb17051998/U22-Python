phrase = input("Entrer une phrase en MAJUSCULE").upper()
compteur = 0
voyelle = 'AEIOUY'
for k in range(len(phrase)):
    if k in voyelles:
        compteur+=1
print("Cette phrase comporte,",compteur,"voyelles")
