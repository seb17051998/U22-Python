n =int(input("Saisir le nombre à convertir en binaire"))
bin, q = [],n
while q//2 !=0:
    bin = [q%2] + bin
    q= q//2
bin = [q%2] + bin
print("l'écriture binaire de l'entier",n,"est ")
for k in range(len(bin)):
    print(bin[k],end=' ')



