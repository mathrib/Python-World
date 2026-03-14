gameDescription = """
    Fifa 23 is a football simulation video game developed by EA Vancouver and EA Romania,
    and published by Electronic Arts. It is the 30th installment in the FIFA series and
    was released on September 30, 2022, for Microsoft Windows, Nintendo Switch, PlayStation 4,
    PlayStation 5, Xbox One, and Xbox Series X/S.
"""
gameName = "Fifa 23"

print(gameName.upper()) #Deixa a string toda em maiúscula
print(gameName.lower()) #Deixa a string toda em minúscula
print(gameName.title()) #Deixa a primeira letra de cada palavra em maiúscula
print(gameName.capitalize()) #Deixa a primeira letra da string em maiúscula e o restante em minúscula
print(gameName.find("i")) #Retorna o índice da primeira ocorrência do caractere "i"
print(gameName.count("f")) #Retorna o número de vezes que o caractere "f" aparece na string
print(gameName.replace("Fifa", "PES")) #Substitui a palavra "Fifa" por "PES"
print(gameDescription.split(",")) #Divide a string em uma lista de substrings, utilizando a vírgula como separador
print(gameDescription.strip()) #Remove os espaços em branco do início e do fim da string

print("Teste commit")
print("Teste commit 3")
print("Teste commit 4")
print("teste commit branch Testes Matheus")