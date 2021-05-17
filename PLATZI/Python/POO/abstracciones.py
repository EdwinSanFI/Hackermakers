
class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura) #son variables privadas, ya que no están dentro del self con paréntesis
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self): #estos son métodos privados
        print('Anadiendo jabon')

    def _lavar(self):
        print('lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')


if __name__ == '__main__' :
    lavadora = Lavadora()
    lavadora.lavar()