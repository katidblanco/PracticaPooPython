class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f'Estas haciendo una llamada desde un: {self.marca} {self.modelo}')

    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.marca} {self.modelo}')

celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 15","96MP")

celular2.llamar()
celular2.cortar()

celular1.llamar()
celular1.cortar()
