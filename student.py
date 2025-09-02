cartao = input().strip()
digitos = [int(d) for d in cartao]

soma_impares = 0
soma_pares = 0

for i in range(len(digitos)):
    posicao = len(digitos) - i  
    valor = digitos[i]

    if posicao % 2 == 1:
        soma_impares += valor
    else:
        dobro = valor * 2
        if 10 <= dobro <= 18:
            soma_pares += (dobro // 10) + (dobro % 10)
        else:
            soma_pares += dobro

soma_total = soma_impares + soma_pares

if soma_total % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")
