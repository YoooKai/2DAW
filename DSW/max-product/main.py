# ┌─────┬─────┬─────┬──────────────────┐
# │     │     │     │                  │
# │    FRAGMENT     │                  │ SEQUENCE
# │     │     │     │                  │
# └─────┴─────┴─────┴──────────────────┘
#
# ───────────────────
#        SPAN


def max_product(sequence: str, span: int) -> int:
    if len(sequence) < span:
        raise ValueError('El tama ̃no de la serie es mayor que la longitud de la secuencia.')
    elif span < 0:
        raise ValueError('El tama ̃no de la serie es un n ́umero negativo.')
    elif not sequence.isnumeric():
        raise ValueError('La secuencia incluye caracteres no numéricos.')
    max_prod = 0
    num_sequence = [int(s) for s in sequence]
    index = 0
    while index <= (len(sequence) - span):
        prod = 1
        for n in range(span):
            prod *= num_sequence[index + n]
        index += 1
        if max_prod < prod:
            max_prod = prod

    return max_prod


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(max_product)
