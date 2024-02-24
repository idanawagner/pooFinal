from clase_inmueble import *


class Casa(Inmueble):
    def __init__(self, id, direccion, ambientes, superficie, propietario, estado, supPatio, cochera):
        super().__init__(id, direccion, ambientes, superficie, propietario, estado)
        self._supPatio = supPatio
        self._cochera = cochera


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

    def infoCasa(self):
        str = super().__str__()
        return str + f'Superficie Patio: {self.getSupPatio()}\nCochera: {self.getCochera()}'

