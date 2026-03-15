gameSet = {"Fifa 23", "GTA V", "Minecraft", "The Witcher 3", "Cyberpunk 2077"}
print("Set de jogos: ", gameSet)
print(type(gameSet))

#No set o 1 e o true são considerados iguais, assim como o 0 e o false, por isso não é possível ter ambos no mesmo set

#1- buscar o tamanho do set:
print(len(gameSet))

#2- true e 1 são considerados iguais, assim como false e 0, por isso não é possível ter ambos no mesmo set
exampleSet = {1,0,True,False}
print(exampleSet)

#adicionar um item ao set:
gameSet.update(exampleSet)
print(gameSet)

#remover um item do set:
gameSet.remove("GTA V")
print(gameSet)

