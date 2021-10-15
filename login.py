
def hyva_salasana(salasana):
    oikea_pituus = False
    suuri_kirjain = False
    pieni_kirjain = False
    on_numero = False
    hyva = False

    if len(salasana) >= 7:
        oikea_pituus = True
        for m in salasana:
            if m.isupper():
                suuri_kirjain = True
            if m.islower():
                pieni_kirjain = True
            if m.isdigit():
                on_numero = True
        if suuri_kirjain and pieni_kirjain and on_numero:
            hyva = True
        else:
            hyva = False

    return hyva





