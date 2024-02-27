from clase_inmueble import *


class Quincho(Inmueble):
    _listaReservas = []
    def __init__(self, direccion, superficie, propietario, inmobiliaria, parrilla, pileta, capacidad, ambientes=1, tipo = 'quincho'):
        super().__init__(direccion, ambientes, superficie, propietario, inmobiliaria, tipo)
        self._parrilla = parrilla
        self._pileta = pileta
        self._capacidad = capacidad


    def __str__(self):
        datos = super().__str__()
        return datos + f'\nParrilla: {self.getParrilla()}\nPileta: {self.getPileta()}\nCapacidad: {self.getCapacidad()}\nFechas reservadas: {self.getListaReservas()}'


    def getId(self):
        return self._id

    def getParrilla(self):
        return self._parrilla
        
    def setParrilla(self, nuevo):
        self._parrilla = nuevo
    
    def getPileta(self):
        return self._pileta
        
    def setPileta(self, nuevo):
        self._pileta = nuevo
    
    def getCapacidad(self):
        return self._capacidad
        
    def setCapacidad(self, nuevo):
        self._capacidad = nuevo
        
    def getListaReservas(self):
        return self._listaReservas

    def setListaReservas(self, fecha):
        if self.getEstado() == 'en alquiler':
            self._listaReservas.append(fecha)

