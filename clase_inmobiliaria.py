class Inmobiliaria():
    _cuadroTarifario = (
    (0, 0.03), (500000, 0.025), (1000000, 0.02), (5000000, 0.015), (10000000, 0.01), (10000001, 0.005))
    _listaInmobiliarias = []

    def __init__(self, razonSocial, cuit):
        self._id = len(self._listaInmobiliarias)
        self._razonSocial = razonSocial
        self._cuit = cuit

        self._listaInmobiliarias.append(self)

    def __str__(self):
        return f'Id: {self.getId()}, Razon Social: {self.getRazonSocial()}, Cuit: {self.getCuit()}'

    def getId(self):
        return self._id

    def getRazonSocial(self):
        return self._razonSocial

    def setRazonSocial(self, nuevo):
        self._razonSocial = nuevo

    def getCuit(self):
        return self._cuit

    def setCuit(self, nuevo):
        self._cuit = nuevo

    @classmethod
    def calcularComision(self, precio):
        for i in range(len(self._cuadroTarifario)):
            if precio <= self._cuadroTarifario[i][0]:
                return self._cuadroTarifario[i][1]
