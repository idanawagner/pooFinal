
# Importaciones
from clase_persona import *
from clase_inmobiliaria import *
from clase_casa import *
from clase_departamento import *
from clase_quincho import *

print('------- Se crean las inmobiliarias -----------')
inmobiliariaWagner =  Inmobiliaria('Wagner&Asociados',22323)
inmobiliariaLopez  = Inmobiliaria('Lopez&Asociados', 32565)
print(inmobiliariaWagner.__dict__)
print(inmobiliariaLopez.__dict__)
print('\n')


print('------- Se crean los propietarios -----------')
propietarioIdana = Persona( nombre='Idana',apellido= 'Wagner',dni= 36477183)
propietarioJuan = Persona('Juan', 'Perez', 32443153)
propietarioMaria = Persona('Maria', 'Rodriguez', 22182828)
propietarioRosa = Persona('Rosa', 'Garcia', 23223232)
propietario4 = Persona('Julian', 'Martinez', 23223232)

print(propietarioIdana.__dict__)
print(propietarioJuan.__dict__)
print('\n')

print('------- Se crean los inquilinos -----------')
inquilinoJose = Persona('Jose','Notararigo',32999999)
inquilinoRamon = Persona('Ramon', 'Garcia', 21232112)
print(inquilinoJose.__dict__)
print(inquilinoRamon.__dict__)
print('\n')


print('----- Se crean las casas ----------')
casa0 = Casa(direccion='Av alem 100', ambientes=4,superficie= 600,propietario=propietarioIdana,inmobiliaria=inmobiliariaWagner,supPatio= 30,cochera= True)
casa1 = Casa(direccion='Belgrano 20', ambientes=2,superficie= 300,propietario=propietarioMaria,inmobiliaria=inmobiliariaWagner,supPatio= 10,cochera= False)
casa2 = Casa(direccion='Gorriti 30', ambientes=5,superficie= 1000,propietario=propietarioIdana,inmobiliaria=inmobiliariaWagner,supPatio=80,cochera= True)
print(casa0)
print('\n')



print('------- Se crean los departamentos -----------')
departamento3 = Departamento( direccion= 'Rodriguez 15',ambientes= 5,superficie= 400,propietario=propietarioJuan,inmobiliaria=inmobiliariaLopez,expensas=39440,nroDpto= 9,cochera= True)
departamento4 = Departamento( direccion= 'Sarmiento 122',ambientes= 2,superficie= 100,propietario=propietarioIdana,inmobiliaria=inmobiliariaLopez,expensas=20000,nroDpto= 9,cochera= True)
departamento5 = Departamento( direccion= 'Alvarado 300',ambientes= 1,superficie= 100,propietario=propietarioJuan,inmobiliaria=inmobiliariaLopez,expensas=10000,nroDpto= 9,cochera= False)
departamento6 = Departamento( direccion= 'Martin Rodriguez 200',ambientes= 3,superficie= 300,propietario=propietarioJuan,inmobiliaria=inmobiliariaLopez,expensas=40000,nroDpto= 9,cochera= False)
print(departamento3)
print('\n')

print('---------- Se cambia el estado de la casa a "alquiler" ------------')
casa0.setEstado('en alquiler')
print(casa0)
print('\n')


print('---------- Se cambia el estado del departamento a "venta" ------------')
departamento3.setEstado('en venta')
print(departamento3)
print('\n')

print('------- Se asigna un inquilino a la casa con estado "inactivo" -----------')
asignado = casa1.setInquilino(inquilinoRamon)
print(asignado, '\n')
print(casa1)
print('\n')


print('----------- Se setea el precio del alquiler en la casa con estado "inactivo"----------')
casa1.setPrecioAlquilerPropietario(10000)
precio = casa1.calcular_precio(casa1)
print(precio, '\n')
print(Inmueble.getInmueble(1))
print('\n')



print('------- Se vende el departamento -----------')
departamento3.setEstado('vendido')
departamento3.setPropietario(propietarioMaria)
print(departamento3)
print('\n')


# Se cambia el estado del departamento a 'inactivo'
Inmueble.eliminarInmueble(departamento3.getId())
print('-----------Inmueble inactivo ----------')
print(f'Departamento {departamento3.getId()} - {departamento3.getEstado()}')
print('\n')

print('----------- Se intenta setear el valor de venta al departamento que tiene estado inactivo ----------')
departamento3.setPrecioVentaPropietario(10000001222)
precio = departamento3.calcular_precio(departamento3)
print(precio)
print('----------- Imprimir inmueble ----------')
print(Inmueble.getInmueble(3))
print('\n')





print('----------- Se setea el estado del departamento a "venta" ----------')
print(departamento4.getEstado())
departamento4.setEstado('en venta')
print(departamento4.getEstado())

print('----------- Se setea el valor de venta del departamento y se calcula el precio ----------')
departamento4.setPrecioVentaPropietario(101222)
precio = departamento4.calcular_precio(departamento4)
print(precio)
print('----------- Imprimir inmueble ----------')
print(Inmueble.getInmueble(4))
print('\n')

print('----------- Lista de inmuebles segun id del propietario ----------')
# Se declara una variable adicional llamada prop para poder realizar rapidamente el cambio y mostrar los distintos casos posibles, por ejemplo cuando existe el propietario y no tiene inmuebles, cuando no existe, o cuando existe y tiene inmuebles
try:
    prop = propietario4
    inmueblesPropietario0 = Inmueble.inmueblesPorPropietario(prop.getId())
    print(prop)
    for inmueble in inmueblesPropietario0:
        print(inmueble.getTipo(), inmueble.getDireccion())
except ValueError as e:
    print(f'Error: {e}')
except NameError:
    print('Propietario sin definir')
print('\n')


print('----------- Lista de inmuebles segun id de la inmobiliaria ----------')
print(inmobiliariaWagner)
try:
    inmueblesInmobiliariaWagner = Inmueble.inmueblesPorInmobiliaria(1)
    for inmueble in inmueblesInmobiliariaWagner:
        print(inmueble.getTipo(), inmueble.getDireccion())
except ValueError as e:
    print(f'Error: {e}')
print('\n')

print('----------- Se crea un quincho y se intenta agregar la fecha reservada ----------')
quincho = Quincho('Av Cabrera 2111', 200, propietarioIdana, inmobiliariaWagner, True, True,40)
lista = quincho.setListaReservas('3/3/24')
print(lista)
print('\n')
# print(quincho)
print('----------- Se setea el estado "en alquiler" y se ingresan las fechas de reservas ----------')
quincho.setEstado('en alquiler')
quincho.setListaReservas('3/3/24')
quincho.setListaReservas('3/4/24')
quincho.setListaReservas('3/8/24')
quincho.setListaReservas('3/9/24')
print(quincho)



# print('-----------Lista inmuebles ----------')
# listarInmuebles = Inmueble.getInmuebles()
# for inmueble in listarInmuebles:
#     print(inmueble)
# print('\n')
#
#
























