phrase , compteur = input("Entrer une phrase : ").lower() , 0
lettre = input("Entrer la lettre à dénombrer.").lower()
for k in range(len(phrase)):
    if phrase[k] == lettre:
        compteur+=1
print("Cette phrase comporte,",compteur,"Lettres de ",lettre)
