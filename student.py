
cartao = input().strip()

# Transforma cada dígito em inteiro e armazena em uma lista
digitos = [int(d) for d in cartao]

# Pega os dígitos em posições ímpares (contando da direita, índices negativos)
impares = digitos[-1::-2]

# Pega os dígitos em posições pares e aplica o dobro
pares = digitos[-2::-2]
pares_dobrados = []
for d in pares:
    dobro = d * 2
    if dobro < 10:
        pares_dobrados.append(dobro)
    else:
        # se o dobro estiver entre 10 e 18, soma os dígitos (ex: 12 -> 1+2 = 3)
        pares_dobrados.append(dobro - 9)

# Soma todos os dígitos
total = sum(impares) + sum(pares_dobrados)

# Verifica se a soma é múltiplo de 10
if total % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")
