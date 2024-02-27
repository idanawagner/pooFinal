class Persona:
    _listaPersonas=[]
    def __init__(self, nombre, apellido, dni):
        self._id = len(self._listaPersonas)
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni

        self._listaPersonas.append(self)

    def __str__(self):
        return f'{self._nombre} {self._apellido}, Dni: {self._dni}'
    
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

    @classmethod
    def existePersona(cls, idPersona):
        for persona in cls._listaPersonas:
            if idPersona == persona.getId():
                return True
        return False

