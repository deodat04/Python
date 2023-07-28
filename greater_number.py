from traceback import print_tb


x=int(input("Entrez le premier entier:\n"))
y=int(input("Entrez le deuxième entier:\n"))
z=int(input("Entrez le troisième entier:\n"))

if x > y and x > z:
    print("{}".format(x))
if x < y and x < z:
    print("{}".format(z))
if z < x and y > x:
    print("{}".format(y)) 