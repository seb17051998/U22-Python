nbAnnee = int(input("Saisir le nombre d'années"))
taux = float(input("Saisir les intérets"))
capIni = float(input("Saisir le capital initial"))
total = capIni
if taux>0 and taux<=100 and capIni>=0:
    if nbAnnee<=0:
        print("Le nombre d'année doit être supérieur à 0")
    else:
            for k in range(1,nbAnnee+1):
                
                total+=(total/100)*taux
                print("Le total sera de",total,'€ dans',nbAnnee,"ans.")
            total=capIni
            increment=0

            while total<capIni:
                total+=(total/100)*taux
                increment+=1
                print("Doublé au bout de",increment,"ans avec un capital de",total,"€")
            else:
                print("Votre taux ou votre capital initial n'est pas valide.")
            
