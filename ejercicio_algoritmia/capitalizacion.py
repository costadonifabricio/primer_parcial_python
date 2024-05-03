# Funcion que recibe un parametro str y debe convetir solo la primera letra en Mayuscula y las demas sin cambios
def capitalizar_palabra(str):
    # Se crea la variable "cadena" para guardar el str capitalizado
    cadena = str.capitalize()
    return cadena

# Se hace una variable para guardar la cadena que se espera ingresar
insertar_cadena = input("Escribe algo para capitalizar solo la primer letra:")
# Se imprime el resultado
print(capitalizar_palabra(insertar_cadena))