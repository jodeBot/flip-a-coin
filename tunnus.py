def luo_tunnus(etu, suku, nro):
    osa1 = etu[0 : 3]
    osa2 = suku[0 : 3]
    osa3 = nro[-3:-1]
    tunnus = osa1 + osa2 + osa3

    return tunnus