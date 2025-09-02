def luhn_check(card_number: str) -> bool:
    digits = [int(ch) for ch in card_number.strip()]
    total = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 0:
            total += d
        else:
            doubled = d * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
    return total % 10 == 0


if __name__ == "__main__":
    s = input().strip()
    s = s.replace(" ", "").replace("-", "")
    if luhn_check(s):
        print("Cartão válido")
    else:
        print("Cartão inválido")
