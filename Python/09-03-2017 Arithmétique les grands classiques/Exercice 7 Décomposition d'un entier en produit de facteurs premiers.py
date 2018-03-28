n = int(input("Saisir un entier n"))
d, div= 2, [1]
e, exp= 1, [1]
while d<=n:
    if n%d == 0:
        div = div + [d]
    d+=1
    
    else:
        exp = exp + [e]
print(exp)
