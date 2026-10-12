def não_possui_a_letra_u(palavra):
    temu = 0
    for letra in palavra:
        if (letra in 'uûüùúUÛÜÙÚ'):
            temu = 1

    if temu != 0:
        return False
    else:
        return True