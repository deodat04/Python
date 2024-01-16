#liste des clients
list_clients = {
    "Paul" : 400000,
    "Marie": 550200,
    "Jean": 90000,
    "Pauline": 1000500
}

#affichage de la liste
def affichage(list_clients):
    print("Compte en Banque")
    print("Client \t Solde(FCFA)")
    print("------------------")
    for ele in list_clients.keys() :
         print(ele, "===>", list_clients[ele])

#depot sur un compte client
def depot(ancien_solde, depot_add):
    return ancien_solde + depot_add

#retrait sur un compte client
def retrait(ancien_solde, retrait_remove):
    return ancien_solde - retrait_remove

#quitter le programme
def quitter():
    quit()
    
while True:

    operation = str(input("Veuillez choisir votre operation: \n  D : Depot \n  R : Retrait \n  A : Affichage \n  Q : Quitter : \n\n"))

    if operation == "D" or operation == "d":
        new_solde = 0
        depot_add = 0
        client = str(input("Entrez le nom du compte du client sur lequel vous voulez faire le depot : "))

        while client not in list_clients:
            print("Le client n'existe pas")
            client = input("Veuillez entrer le nom du compte du client sur lequel vous voulez faire le depot : ")

        depot_add = int(input("Entrez le montant que vous voulez deposer : "))

        for cle,solde in list_clients.items():
            if cle == client:
                ancien_solde = solde
                new_solde = depot(ancien_solde,depot_add)
                list_clients[cle] = new_solde
                affichage(list_clients)
        

    elif operation == "R" or operation == "r":
        new_solde = 0
        retrait_remove = 0
        client = str(input("Entrez le nom du compte du client sur lequel vous voulez faire le retrait : "))

        while client not in list_clients:
            print("Le client n'existe pas")
            client = input("Veuillez entrer le nom du compte du client sur lequel vous voulez faire le retrait : ")

        retrait_remove = int(input("Entrez le montant que vous voulez retirer : "))

        while retrait_remove > list_clients[client] or retrait_remove <= 0:
            print("Le montant doit être positif et ne peut pas dépasser le solde actuel.")
            retrait_remove = int(input("Entrez le montant que vous voulez retirer : "))
    
        for cle,solde in list_clients.items():
            if cle == client:
                ancien_solde = solde
                new_solde = retrait(ancien_solde,retrait_remove)
                list_clients[cle] = new_solde
                affichage(list_clients)


    elif operation == "A" or operation == "a":
        affichage(list_clients)


    elif operation == "Q" or operation == "q":
        print("Merci et à bientot ! ")
        quitter()


    else:
        print("Vous n'avez choisi aucune option")
