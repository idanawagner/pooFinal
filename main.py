# Importaciones
from clase_inmobiliaria import *
from clase_persona import *
from clase_casa import *
from clase_departamento import *


print('------- Se crean las inmobiliarias -----------')
inmobiliariaWagner =  Inmobiliaria('Wagner&Asociados',22323)
inmobiliariaLopez  = Inmobiliaria('Lopez&Asociados', 32565)
print(inmobiliariaWagner.__dict__)
print(inmobiliariaLopez.__dict__)
print('\n')


print('------- Se crean los propietarios -----------')
propietarioIdana = Persona(id=1, nombre='Idana',apellido= 'Wagner',dni= 36477183)
propietarioJuan = Persona(2, 'Juan', 'Perez', 32443153)
propietarioMaria = Persona(2, 'Maria', 'Rodriguez', 22182828)

print(propietarioIdana.__dict__)
print(propietarioJuan.__dict__)
print('\n')

print('------- Se crean los inquilinos -----------')
inquilinoJose = Persona(id=1, nombre='Jose',apellido= 'Notararigo',dni= 32999999)
inquilinoRamon = Persona(2, 'Ramon', 'Garcia', 21232112)
print(inquilinoJose.__dict__)
print(inquilinoRamon.__dict__)
print('\n')


print('----- Se crea una casa ----------')
casa1 = Casa(direccion='calvo 16', ambientes=2,superficie= 300,propietario=propietarioIdana,inmobiliaria=inmobiliariaWagner,supPatio= 30,cochera= True)
print(str(casa1))

print('\n')
print('---------- Se cambia el estado de la casa a "alquiler" ------------')
casa1.setEstado('alquiler')
print(str(casa1))
print('\n')

print('------- Se crea un departamento -----------')
departamento1 = Departamento( direccion= 'Rodriguez 15',ambientes= 5,superficie= 400,propietario=propietarioJuan,inmobiliaria=inmobiliariaLopez,expensas=39440,nroDpto= 9,cochera= True)
print(str(departamento1))
print('\n')

print('---------- Se cambia el estado del departamento a "venta" ------------')
departamento1.setEstado('venta')
print(str(departamento1))
print('\n')

print('------- Se asigna el inquilino a la casa -----------')
casa1.setInquilino(inquilinoRamon)
print(str(casa1))
print('\n')

print('------- Se vende el departamento -----------')
departamento1.setPropietario(propietarioMaria)
print(str(departamento1))


# lista de inmuebles
print('\n')
print('-----------Lista inmuebles ----------')
print(Inmueble.getInmuebles())
print('\n')


# Se elimina el departamento de la lista de inmuebles
Inmueble.eliminarInmueble(departamento1.getId())
print('-----------Lista inmuebles----------')
print(Inmueble.getInmuebles())
print('\n')

print('----------- Imprimir inmueble 1 ----------')
print(Inmueble.getInmueble(0))
print('\n')
















































