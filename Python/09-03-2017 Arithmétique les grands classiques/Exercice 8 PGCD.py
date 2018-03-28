a=int(input("A : a = "))
b=int(input("B : b = "))
a1 , b1 = a , b
while a1%b1:
    a1 , b1 = b1 , a1%b1
print("Le PGCD de",a,"et de",b,"vaut : ",b1)
