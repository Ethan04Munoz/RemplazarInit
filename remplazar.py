#Remplazador de palabras hecho en python

#limpiar pantalla
import os

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


borrarPantalla()

#Llenado de variables
print("Hola, bienvenido al remplazador de palabras!\nAhora, por favor, ingresa el texto en que buscaré\n")
textoIntroducido = input()
print("\n")
print("Genial! Ahora introduce la palabra que debo buscar\n")
palabraBuscar = input()
print("\n")
print("Finalmente, introduce por que debo remplazar la cadena que ingresaste\n")
palabraRemplazo = input()

print("\nTrabajando...\n")

#Proceso Busqueda

import re
textoIntroducidoProv = textoIntroducido
#Buscamos
print(re.findall(palabraBuscar, textoIntroducidoProv, flags=re.IGNORECASE))

print(re.sub(palabraBuscar, palabraRemplazo, textoIntroducidoProv, flags=re.IGNORECASE))