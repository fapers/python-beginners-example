from os import read


arquivo = open("fruits.txt", "r")
frutas = arquivo.read()
arquivo.close()
print(frutas)
    