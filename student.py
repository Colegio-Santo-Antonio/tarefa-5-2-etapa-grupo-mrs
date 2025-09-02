cartao = input().strip()
digitos = [int(d) for d in cartao]
impares = digitos[-1::-2]
pares = digitos[-2::-2]
pares_dobrados = [(d*2 if d*2 < 10 else d*2 - 9) for d in pares]
total = sum(impares) + sum(pares_dobrados)
if total % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")
