inicio = int(input("Digite o número de início do intervalo: "))
fim = int(input("Digite o número de fim do intervalo: "))
soma_pares = 0

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pares += numero
else:
    if soma_pares == 0:
        print("Não há números pares no intervalo.")
    else:
        print(f"A soma dos números pares no intervalo é: {soma_pares}")