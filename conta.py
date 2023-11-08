class Conta:
    def __init__(self, numero, titular, saldo, limite):         #aqui eu defini uma função encapsulando os atributos
                                                                #deixando tudo privado
        print("Construindo um objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #métodos
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor): #método
        if(self.__pode_sacar(valor)):

            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def inadimplente(self, cliente):
        cliente

    @property #usando propriedades
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod #método estático
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos(): #método estático
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}