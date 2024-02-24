# Importaciones
from clase_propietario import *
from clase_casa import *
from clase_departamento import *

print('------- Se crean los propietarios -----------')
propietario1 = Propietario(id=1, nombre='Idana',apellido= 'Wagner',dni= 36477183)
propietario2 = Propietario(2, 'Juan', 'Perez', 32443153)
print(propietario1.__dict__)
print(propietario2.__dict__)
print('\n')

print('----- Se crea una casa ----------')
casa1 = Casa(id=1, direccion='calvo 16', ambientes=2,superficie= 300,propietario=1,estado= 1,supPatio= 30,cochera= True)
print(casa1.__dict__)

print('\n')
print('---------- Se cambia el estado de la casa a "alquiler" ------------')
casa1.setEstado('alquiler')
print(casa1.__dict__)
print('\n')

print('------- Se crea un departamento -----------')
departamento1 = Departamento(id=2, direccion= 'Rodriguez 15',ambientes= 5,superficie= 400,propietario= 2,estado= 2,expensas=39440,nroDpto= 9,cochera= True)
print(departamento1.__dict__)
print('\n')

print('---------- Se cambia el estado del departamento a "venta" ------------')
departamento1.setEstado('venta')
print(departamento1.__dict__)
print('\n')

print('------- Se asigna el propietario a la casa -----------')
casa1.setPropietario(propietario1.getId())
print(casa1.__dict__)
print('\n')

print('------- Se asigna el propietario al departamento -----------')
departamento1.setPropietario(propietario1.getId())
print(departamento1.__dict__)


# Se agrega la casa a la lista de inmuebles
Inmueble.agregarInmueble(casa1)
print('\n')
print('-----------Lista inmuebles ----------')
print(Inmueble.getInmuebles())
print('\n')

# Se agrega el departamento a la lista de inmuebles
Inmueble.agregarInmueble(departamento1)
print('-----------Lista inmuebles----------')
print(Inmueble.getInmuebles())
print('\n')

# Se elimina el departamento de la lista de inmuebles
Inmueble.eliminarInmueble(departamento1.getId())
print('-----------Lista inmuebles----------')
print(Inmueble.getInmuebles())
print('\n')

print('----------- Imprimir inmueble 1 ----------')
print(Inmueble.getInmueble(1))
print('\n')

print('----------- Imprimir inmueble 2 ----------')
print(Inmueble.getInmueble(2))
















































