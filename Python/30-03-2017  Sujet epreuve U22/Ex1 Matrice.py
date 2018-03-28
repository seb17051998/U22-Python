def ecrire_matrice(Mat):
    for i in range(3):
        print(Mat[i])
Mat= [[i+j*3+1for i in range(3)]for j in range(3)]
print("la matrice Mat est : Mat = ","\t")
ecrire_matrice(Mat)
