class Propietario:
    def __init__(self, id, nombre, apellido, dni):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni

    def __str__(self):
        return f' Nombre: {self._nombre}\nApellido: {self._apellido}\nDni:{self._dni}'
    
    def getId(self):
        return self._id

    def getNombre(self):
        return self._nombre

    def setNombre(self, nuevo):
        self._nombre = nuevo

    def getApellido(self):
        return self._apellido

    def setApellido(self, nuevo):
        self._apellido = nuevo

    def getDni(self):
        return self._dni

    def setDni(self, nuevo):
        self._dni = nuevo

