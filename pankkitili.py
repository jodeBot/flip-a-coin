class PankkiTili:

    def __init__(self, saldo):
        self.__saldo = saldo

    def talletus(self, maara):
        self.__saldo += maara

    def nosto(self, maara):
        if self.__saldo >= maara:
            self.__saldo -= maara
        else:
            print('Virhe: Tilillä ei tarpeeksi rahaa.')

    def get_saldo(self):
        return self.__saldo


