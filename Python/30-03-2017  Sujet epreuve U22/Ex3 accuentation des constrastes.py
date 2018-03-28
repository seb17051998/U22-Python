def luminosite(Mat):
    somme = 0
    for i in range(len[Mat]):
            somme = somme+Mat[i][j]   
    lum = somme/len[Mat]
    return(lum)

Mat = eval(input("Entrer les coeff de la matrice: "))

print(Mat)
print("La luminosité de l'image vaut : ",luminosite(Mat))

def contraste(Mat,luminosite):
    for i in range(len(Mat)):
        if Mat[i]< lum:
            Mat[i]=Mat[i]/2
        else:
            if 2*Mat[i]<=100:
                Mat[i] = 2*Mat[i]
            else:
                Mat[i]= 100

print(Mat)

