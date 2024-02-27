from clase_inmueble import *

class Departamento(Inmueble):
    def __init__(self, direccion, ambientes, superficie,  propietario, inmobiliaria, expensas, nroDpto, cochera, tipo = 'departamento'):
        super().__init__(direccion, ambientes, superficie, propietario, inmobiliaria, tipo)
        self._expensas = expensas
        self._nroDpto = nroDpto
        self._cochera = cochera

    def __str__(self):
        datos = super().__str__()
        return datos + f'\nExpensas: {self.getExpensas()}\nNumero de departamento: {self.getNroDpto()}\nCochera: {self.getCochera()}'

    def getExpensas(self):
        return self._expensas

    def setExpensas(self, nuevo):
        self._expensas = nuevo

    def getNroDpto(self):
        return self._nroDpto

    def setNroDpto(self, nuevo):
        self._nroDpto = nuevo

    def getCochera(self):
        return self._cochera

    def setCochera(self, nuevo):
        self._cochera = nuevo
