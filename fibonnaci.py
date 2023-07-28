
def suite_fibonacci(n):
    if n <= 1:
        return n
    else:
        return suite_fibonacci(n-2) + suite_fibonacci(n-1)


nombre = int(input("Entrez le nombre de termes que vous souhaitez afficher:"))

print("Les {} termes de la suite de fibonacci sont:".format(nombre), end=" ")

for i in range(nombre):
    print(suite_fibonacci(i))
