
cartao = input().strip()
digitos = [int(d) for d in cartao]
impares = digitos[-1::-2]
pares = digitos[-2::-2]
pares_dobrados = []
for d in pares:
    dobro = d * 2
    if dobro < 10:
        pares_dobrados.append(dobro)
    else:
        pares_dobrados.append(dobro - 9)
total = sum(impares) + sum(pares_dobrados)
if total % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")
