n = int(input("Entrer la valeur de n : n = "))
Tab = [i for i in range (n+1)]
for i in range(1,n+1):
    if not i%10:
        print(Tab[i])
    else:
        print(Tab[i],"\t",end=" ")

print("\n")
for i in range(2,n+1):
    for j in range(i+1,n+1):
        if not j%i:
            Tab[j]=0

print("Liste des entiers naturels premiers inférieurs ou égaux à ",n)
for i in range(2,n+1):
    if Tab[i]:
        print(Tab[i],end=" ")
