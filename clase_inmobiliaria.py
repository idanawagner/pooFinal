class Inmobiliaria():
    _listaPropiedades = []
    def __init__(self, razonSocial, cuit, porcentajeAlquiler, porcentajeVenta):
        self._razonSocial = razonSocial
        self._cuit = cuit
        self._porcentajeAlquiler = porcentajeAlquiler
        self._porcentajeVenta = porcentajeVenta

        def getRazonSocial(self):
            return self._razonSocial

        def setRazonSocial(self, nuevo):
            self._razonSocial = nuevo

        def getCuit(self):
            return self._cuit

        def setCuit(self, nuevo):
            self._cuit = nuevo

        def getPorcentajeAlquiler(self):
            return self._porcentajeAlquiler

        def setPorcentajeAlquiler(self, nuevo):
            self._porcentajeAlquiler = nuevo

        def getPorcentajeVenta(self):
            return self._porcentajeVenta

        def setPorcentajeVenta(self, nuevo):
            self._porcentajeVenta = nuevo

        def agregarPropiedad(self, nuevaPropiedad):
            _listaPropiedades.append(nuevaPropiedad)
