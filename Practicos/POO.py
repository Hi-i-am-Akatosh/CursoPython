class Vehiculo():
    color = "Blanco"
    marca = "Chevrolet"
    modelo = "Trooper"
    placa = "PDN-0971"
    anio = "1973"


class Propietario():
    nombre = "Ruth"
    apellido = "Rodríguez"
    cedula = "1706989744"

obj_propietario = Propietario()
obj_vehiculo = Vehiculo()

print("Formulario de matriculación\n")
print("Nombre del propietario:")
print (obj_propietario.nombre)
print("\nApellido del propietario:")
print (obj_propietario.apellido)
print("\nCédula del propietario:")
print (obj_propietario.cedula)

print("\nMarca del vehiculo:")
print (obj_vehiculo.marca)
print("\nModelo del vehiculo:")
print (obj_vehiculo.modelo)
print("\nPlaca del vehiculo:")
print (obj_vehiculo.placa)
