import random
prix=random.randint(1,10)
score=20
tentative=0

print("Devinez le nombre mystère compris dans [1,10]")

Game=True
while Game:
    nmbre = int (input())
    tentative +=1
    if nmbre < prix:
        print("Le nombre mystère est plus grand")
    if nmbre > prix:
        print("Le nombre mystère est plus grand")
    if nmbre==prix:
        print("Congratulations!!!! Vous avez trouvé le nombre mystère {} en {} essais et vous avez un score de {}".format(prix,tentative,int(score/tentative)) )
        
        break
    
    

    


