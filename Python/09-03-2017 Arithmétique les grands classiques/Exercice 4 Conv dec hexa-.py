# Conversion en héxa

déc = int(input("Saisir l'écriture décimale d'un entier naturel n : "))
héx = []
liste_chiffres = "ABCDEF"
q= déc
while q!=0:
    héx = [q%16] + héx
    q = q//16
print("l'écriture de",déc,"dans le système héxadécimal est ",end="")
for i in range(len(héx)):
    if héx[i]<+10
