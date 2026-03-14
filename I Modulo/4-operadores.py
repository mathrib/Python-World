num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1%num2
exponenciacao = num1 ** num2


print(f"A soma dos números é: {soma}")
print(f"A subtração dos números é: {subtracao}")
print(f"A multiplicação dos números é: {multiplicacao}")
print(f"A divisão dos números é: {divisao}")
print(f"O resto da divisão é de: {resto}")
print(f"A exponenciação dos números é: {exponenciacao}")

bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2

bigger_equal = num1 >= num2
smaller = num1 <= num2

print(f"O primeiro número é maior que o segundo? {bigger}")
print(f"O primeiro número é menor que o segundo? {smaller}")

num1 += 1 #num1 = num1 + 1
num1-= 1 #num1 = num1 - 1
num1 *= 1 #num1 = num1 * 1
num1 /= 1 #num1 = num1 / 1