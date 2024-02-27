from clase_inmueble import *


class Casa(Inmueble):
    def __init__(self, direccion, ambientes, superficie, propietario, inmobiliaria, supPatio, cochera, tipo = 'casa'):
        super().__init__(direccion, ambientes, superficie, propietario, inmobiliaria, tipo)
        self._supPatio = supPatio
        self._cochera = cochera

    def __str__(self):
        datos = super().__str__()
        return datos + f'\nSuperficie Patio: {self.getSupPatio()}\nCochera: {self.getCochera()}'


    def getId(self):
        return self._id

    def getSupPatio(self):
        return self._supPatio

    def setSupPatio(self, supPatio):
        self._supPatio = supPatio

    def getCochera(self):
        return self._cochera

    def setCochera(self, nuevo):
        self._cochera = nuevo


