
class Inmueble():
    _listaEstado=['alquiler', 'alquilado', 'venta', 'vendido', 'alquiler y venta']
    _listaInmobiliaria = []
    def __init__(self, partida, direccion, ambientes, superficie, propietario, estado):
        self._id = partida
        self._direccion = direccion
        self._ambientes = ambientes
        self._superficie = superficie
        self._propietario = propietario
        self._estado = ''

    def __str__(self):
        return f'ID: {self._id}\nDireccion: {self.getDireccion()}\nAmbientes: {self.getAmbientes()} \nSuperficie: {self.getSuperficie()} mts2\nEstado: {self.getEstado()}'

    def getId(self):
        return self._id

    def setId(self, nuevo):
        self._id = nuevo

    def getDireccion(self):
        return self._direccion

    def setDireccion(self, nuevo):
        self._direccion = nuevo

    def getAmbientes(self):
        return self._ambientes

    def setAmbientes(self, nuevo):
        self._ambientes = nuevo

    def getSuperficie(self):
        return self._superficie

    def setSuperficie(self, nuevo):
        self._superficie = nuevo

    def getEstado(self):
        return self._estado

    def setEstado(self, nuevo):
        if nuevo in self._listaEstado:
            self._estado = nuevo
        else:
            print('Estado no valido')



    def getPropietario(self):
        return self._propietario

    def setPropietario(self, idPropietario):
        self._propietario = idPropietario
    
    # Metodo de clase
    @classmethod
    def agregarInmueble(cls, inmueble):
        cls._listaInmobiliaria.append(inmueble)

    @classmethod
    def getInmuebles(cls):
        for inmueble in cls._listaInmobiliaria:
            print(inmueble.__dict__)
    
    @classmethod
    def getInmueble(cls, id):
        for inmueble in cls._listaInmobiliaria:
            if inmueble.getId() == id:
                return inmueble
        return 'No se encontro el inmueble'
    
    @classmethod
    def eliminarInmueble(cls, id):
        for inmueble in cls._listaInmobiliaria:
            if inmueble.getId() == id:
                cls._listaInmobiliaria.remove(inmueble)
                return True
        return False

        

