# conv inverse
liste_chiffres="ABCDEF"
héxa = input("Saisir l'écriture héxa d'un entier naturel n : ")
l , n = len(héxa), 0
for i in range(l):
    if héxa[i] in liste_chiffres:
        n = n + (ord(héxa[i])-55)*16**(l-1-i)
    else:
        p = int(héxa[i])
        n = n+p*16**(l-1-i)
print("Lentier ayant pour écriture héxadécimale ",héxa  'est :' ,n)
