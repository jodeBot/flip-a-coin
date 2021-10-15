import pankkitili

def main():
    alku_saldo = float(input('Anna tilin alkusaldo:'))
    talletukset = pankkitili.PankkiTili(alku_saldo)
    # Luodaan pankkitili-object
    maksu = float(input('\nKuinka paljon haluat tallettaa? '))
    print('Talletetaan summa tilille.')
    talletukset.talletus(maksu)

    # Näytetään tilin saldo
    print('Tililläsi on rahaa', format(talletukset.get_saldo(), '.2f' ,'euroa.\n')

    # Kysytään nosto
    otto = float(input('Paljonko haluat nostaa tililtä?: '))
    print('Nostetaan summa')
    talletukset.nosto(otto)

    print('Tililläsi on rahaa', format(talletukset.get_saldo(), '.2f', 'euroa'))