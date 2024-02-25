from abc import ABC, abstractmethod
class Inmueble():
    _listaEstado=['inactivo','alquiler', 'alquilado', 'venta', 'vendido', 'alquiler y venta']
    _listaInmuebles = []
    def __init__(self, direccion, ambientes, superficie, propietario,inmobiliaria, inquilino=None):
        self._id = len(self._listaInmuebles)
        self._direccion = direccion
        self._ambientes = ambientes
        self._superficie = superficie
        self._propietario = propietario
        self._inquilino = inquilino
        self._inmobiliaria = inmobiliaria
        self._estado = self._listaEstado[0]

        self._listaInmuebles.append(self)

    @abstractmethod
    def __str__(self):
        return f'ID: {self._id}\nDireccion: {self.getDireccion()}\nAmbientes: {self.getAmbientes()} \nSuperficie: {self.getSuperficie()} mts2\nEstado: {self.getEstado()}\nPropietario: {self.getPropietario()}\nInmobiliaria: {str(self.getInmobiliaria())}\nInquilino: {self.getInquilino()}'

    def getId(self):
        return self._id

    # Se comenta el set porque no se debe poder modificar el id, dado que esta seteado automaticamente por la longitud de listaInmuebles
    # def setId(self, nuevo):
    #     self._id = nuevo

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
        if nuevo in self._listaEstado :
            self._estado = nuevo
        else:
            print('Estado no valido')

    def getPropietario(self):
        return self._propietario

    def setPropietario(self, idPropietario):
        self._propietario = idPropietario

    def getInmobiliaria(self):
        return self._inmobiliaria

    def setInmobiliaria(self, nuevo):
        self._inmobiliaria = nuevo


    def getInquilino(self):
        return self._inquilino

    def setInquilino(self, nuevo):
        self._inquilino = nuevo


    # Metodo de clase
    @classmethod
    def getInmuebles(cls):
        for indice, inmueble in enumerate(cls._listaInmuebles):
            print(f'---------Inmueble {indice + 1}---------')
            print(inmueble)
            print('----------termina------------')

    @classmethod
    def getInmueble(cls, id):
        for inmueble in cls._listaInmuebles:
            if inmueble.getId() == id:
                return inmueble
        return 'No se encontro el inmueble'
    
    @classmethod
    def eliminarInmueble(cls, id):
        for inmueble in cls._listaInmuebles:
            if inmueble.getId() == id:
                inmueble.setEstado('inactivo')
                return True
        return False

    @classmethod
    @abstractmethod
    def calcular_precio(cls, monto_solicitado, porcentaje_ganancia):
        pass

# Polimorfismo, se agrega con fines educativos dado que no seria necesaria,
# se podria llamar al metodo str() con una instancia de las clases hijas y seria lo mismo
# def informacion(inmueble):
#     return inmueble.__str__()