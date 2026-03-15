pessoa = {
    "nome": "Matheus",
    "idade": 25,
    "cidade": "Natal"
}

print(pessoa)
print(type(pessoa))


gameFifa = {
	"name": "Fifa 23",
	"yearLaunch": 2022,
	"gamePrice": 250.99,
	"classification": 7.9,
	"genre": ["esporte", "familia"]

}

print(gameFifa)
#1 - recuperar elementos do dicionário:
print(gameFifa['name'])
print(gameFifa['genre'][0])

#2 - Buscar chaves do dicionário:
print(gameFifa.keys())

#3 - Buscar valores do dicionário:
print(gameFifa.values())

#4- Buscar itens do dicionário:
print(gameFifa.items())

#5- Adicionar um item ao dicionario
gameFifa["developer"] = "EA Sports"
print(gameFifa)

#6-update um item do dicionário:
gameFifa.update({"gamePrice": 199.99})
print(gameFifa)

#7-remover um item do dicionário:
gameFifa.pop("developer")
print(gameFifa) 