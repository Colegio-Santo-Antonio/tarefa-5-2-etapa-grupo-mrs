def luhn_check(card_number: str) -> bool:
    digits = [int(d) for d in card_number]
    soma = 0

    
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 0:
            # posição ímpar (da direita)
            soma += d
        else:
            dobro = d * 2
            if dobro > 9:
                
                dobro -= 9
            soma += dobro

    return soma % 10 == 0


if __name__ == "__main__":
    card = input().strip()
    if luhn_check(card):
        print("Cartão válido")
    else:
        print("Cartão inválido")
