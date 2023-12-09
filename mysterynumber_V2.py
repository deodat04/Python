import random
secret = random.randint(0,100)

print("         ---------------------------------------------------             ")
print(" BIENVENUE DANS NOTRE PROGRAMME DE DEVINETTE D'UN NOMBRE ENTIER NATUREL ")
print("         ---------------------------------------------------             ")
print("\t")
print("Vous devrez deviner la valeur d'un nombre aléatoire compris entre 0 et 100. Le nombre d'essai dépendra du niveau choisi." )
print("\t")

niveau = str(input("Veuillez choisir un niveau :  1 pour Beginner, 2 pour Intermediate et 3 pour Advanced :"))

nbr_essai = 0

if(niveau == "1"):
     nbr_essai = 10
elif(niveau == "2"):
     nbr_essai = 5
elif(niveau == "3"):
     nbr_essai = 3
else:
     print("Choix Invalide. Le niveau Beginner est choisi par défaut")
     nbr_essai = 10

print("Vous devrez trouvé le nombre secret en", nbr_essai, "essais !!!")
print("Bonne chance !!!")
print("\t")

essai = 0

while(essai < nbr_essai) :
    essai += 1
    n =  int(input("Entrez une valeur entre 0 et 100 : "))

    if(secret > n):
        print("Trop Petit")
    elif(secret < n):
         print("Trop Grand")
    else:
         print("Gagné en ", essai, " essai !!!")
         break

if(essai == nbr_essai ):
    print("Perdu ! Le secret était ", secret, ".")
