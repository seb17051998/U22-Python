n = int(input("Saisir n"))
fact = 1
for i in range(2,n+1):
    fact=fact*i
print("La factorielle de",n,"vaut",fact)
