a = int(input("Saisir la 1ère valeur"))
b = int(input("Saisir la 2ère valeur"))
c = int(input("Saisir la 3ère valeur"))
d = int(input("Saisir la 4ère valeur"))
e = int(input("Saisir la 5ème valeur"))
f = int(input("Saisir la 6ère valeur"))
a=a+d
d=a-d
a=a-d
b=b+f
f=b-f
b=b-f
c=c+a
a=c-a
c=c-a

e=e+c
c=e-c
e=e-c
print("La 1ère valeur est égale à",a)
print("La 2ème valeur est égale à",b)
print("La 3ème valeur est égale à",c)
print("La 4ème valeur est égale à",d)
print("La 5ème valeur est égale à",e)
print("La 6ème valeur est égale à",f)
