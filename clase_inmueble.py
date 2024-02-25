from abc import ABC, abstractmethod
from clase_inmobiliaria import *
class Inmueble():
    _listaEstado=['inactivo','alquiler', 'alquilado', 'venta', 'vendido', 'alquiler y venta']
    _listaInmuebles = []
    def __init__(self, direccion, ambientes, superficie, propietario,inmobiliaria, inquilino=None, precioAlquilerPropietario=0, precioVentaPropietario=0, precioFinalAlquiler=0, precioFinalVenta=0, comisionAlquiler=0, comisionVenta=0):
        self._id = len(self._listaInmuebles)
        self._direccion = direccion
        self._ambientes = ambientes
        self._superficie = superficie
        self._propietario = propietario
        self._inmobiliaria = inmobiliaria
        self._inquilino = inquilino
        self._precioAlquilerPropietario = precioAlquilerPropietario
        self._precioVentaPropietario = precioVentaPropietario
        self._precioFinalAlquiler = precioFinalAlquiler
        self._precioFinalVenta = precioFinalVenta
        self._comisionVenta = comisionVenta
        self._comisionAlquiler = comisionAlquiler
        self._estado = self._listaEstado[0]

        self._listaInmuebles.append(self)

    @abstractmethod
    def __str__(self):
        return f'ID: {self._id}\nDireccion: {self.getDireccion()}\nAmbientes: {self.getAmbientes()} \nSuperficie: {self.getSuperficie()} mts2\nEstado: {self.getEstado()}\nPropietario: {self.getPropietario()}\nInmobiliaria: {str(self.getInmobiliaria())}\nInquilino: {self.getInquilino()}\nPrecio alquiler propietario: {self.getPrecioAlquilerPropietario()}\nPrecio venta propietario: {self.getPrecioVentaPropietario()}\nComision alquiler: {self.getComisionAlquiler()}\nComision venta: {self.getComisionVenta()}\nPrecio final alquiler: {self.getPrecioFinalAlquiler()}\nPrecio final venta: {self.getPrecioFinalVenta()}'

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

    def getPrecioAlquilerPropietario(self):
        return self._precioAlquilerPropietario

    def setPrecioAlquilerPropietario(self, nuevo):
        self._precioAlquilerPropietario = nuevo
    def getPrecioVentaPropietario(self):
        return self._precioVentaPropietario

    def setPrecioVentaPropietario(self, nuevo):
        self._precioVentaPropietario = nuevo

    def getPrecioFinalAlquiler(self):
        return self._precioFinalAlquiler

    # def setPrecioFinalAlquiler(self, nuevo):
    #     self._precioFinalAlquiler = nuevo

    def getPrecioFinalVenta(self):
        return self._precioFinalVenta

    # def setPrecioFinalVenta(self, nuevo):
    #     self._precioFinalVenta = nuevo

    def getComisionAlquiler(self):
        return self._comisionAlquiler

    # def setComisionAlquiler(self, nuevo):
    #     self._comisionAlquiler = nuevo

    def getComisionVenta(self):
        return self._comisionVenta

    # def setComisionVenta(self, nuevo):
    #     self._comisionVenta = nuevo


    # Metodo de clase
    @classmethod
    def getInmuebles(cls):
        for indice, inmueble in enumerate(cls._listaInmuebles):
            print(f'---------Inmueble {indice + 1}---------')
            print(inmueble)

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

    def calcular_precio(self, inmueble):
        if inmueble.getEstado() == 'alquiler':
            self._comisionAlquiler = Inmobiliaria.calcularComision(inmueble.getPrecioAlquilerPropietario())
        elif inmueble.getEstado() == 'venta':
            self._comisionVenta =  Inmobiliaria.calcularComision(inmueble.getPrecioVentaPropietario())
        elif inmueble.getEstado() == 'alquiler y venta':
            self._comisionAlquiler = Inmobiliaria.calcularComision(inmueble.getPrecioAlquilerPropietario())
            self._comisionVenta = Inmobiliaria.calcularComision(inmueble.getPrecioVentaPropietario())
        elif inmueble.getEstado() == 'alquilado' or inmueble.getEstado() == 'vendido' or inmueble.getEstado() == 'inactivo':
            return 'Estado no valido para calcular precios'
