def luhn_check(card_number: str) -> bool:
   
    digits = [int(d) for d in card_number]
    soma = 0

   
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 0:
          
            soma += d
        else:
            dobro = d * 2
            if 10 <= dobro <= 18:
                # soma dos dígitos do resultado
                soma += (dobro // 10) + (dobro % 10)
            else:
                soma += dobro

   
    return soma % 10 == 0


if __name__ == "__main__":
    card = input().strip()
    if luhn_check(card):
        print("Cartão válido")
    else:
        print("Cartão inválido")

