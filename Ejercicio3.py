# Ejercicio 3:
_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]

def validate_discount_code(discount_code):
    for code in _AVAILABLE_DISCOUNT_CODES:
        diff = set()
        for i in range(len(discount_code)):
            if discount_code[i] not in code:
                diff.add(discount_code[i])
        for j in range(len(code)):
            if code[j] not in discount_code:
                diff.add(code[j])
        if len(diff) < 3:
            return True
    return False
