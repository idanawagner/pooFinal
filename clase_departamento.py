from clase_inmueble import *

class Departamento(Inmueble):
    def __init__(self, id, direccion, ambientes, superficie,  propietario, estado, expensas, nroDpto, cochera):
        super().__init__(id, direccion, ambientes, superficie, propietario, estado)
        self._expensas = expensas
        self._nroDpto = nroDpto
        self._cochera = cochera



    def infoDepartamento(self):
        str = super().__str__()
        return f'Expensas: {self.getExpensas()}\nNumero de departamento: {self.getNroDpto()}\nCochera: {self.getCochera()}'

    def getExpensas(self):
        return self._expensas

    def setExpensas(self, expensas):
        self._expensas = expensas

    def getNroDpto(self):
        return self._nroDpto

    def setNroDpto(self, nroDpto):
        self._nroDpto = nroDpto

    def getCochera(self):
        return self._cochera

    def setCochera(self, nuevo):
        self._cochera = nuevo