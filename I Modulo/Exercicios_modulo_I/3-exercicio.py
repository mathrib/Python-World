"""
Substituindo caractere repetido
Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro
caractere foram alteradas para '$', exceto o próprio primeiro caractere
"""

string = "Fifa 23"
primeiro_caractere = string[0].lower()
nova_string = primeiro_caractere + string[1:].replace(primeiro_caractere, '$')
print(nova_string)
