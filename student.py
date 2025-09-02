cartao = input().strip()
digitos = [int(d) for d in cartao]

# soma dos dígitos em posição ímpar (contando da direita)
soma_impares = sum(digitos[-1::-2])

# soma dos dígitos em posição par (contando da direita)
soma_pares = 0
for d in digitos[-2::-2]:
    dobro = d * 2
    if 10 <= dobro <= 18:
        soma_pares += (dobro // 10) + (dobro % 10)  # soma dígitos do dobro
    else:
        soma_pares += dobro

# soma total
soma_total = soma_impares + soma_pares

# validação final
if soma_total % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")
