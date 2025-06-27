# PROGRAMACIÓN Ⅰ

## Práctico 5.1: Listas

## Alumno: Maximiliano Xavier Rodriguez

### Actividades

"""1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range."""
"""numeros_multiplos_4 = list(range(4, 101, 4))"""

"""2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo."""
"""my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[-2])"""

"""3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla."""
"""my_list = []
print(my_list)
my_list.append("Mario")
my_list.append("Luis")
my_list.append("Juan")
print(my_list)"""

"""4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente."""
"""animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1] = "loro"
animales[-1] = "oso"
print(animales)"""

"""5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza"""
"""numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)"""
"""En el programa dado existe una lista de numeros sin orden y con distintos valores. Luego con la funcion remove se elimina uno de los elementos de la lista
en este caso se pasa como parametro la funcion max que devuelve el numero mas grande de la lista. Por lo tanto el valor eliminado es el 22 y la lista resultante es [8, 15, 3, 7]"""

"""6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros."""
"""numeros = list(range(10, 31, 5))
print(numeros[0])
print(numeros[1])  """

"""7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera."""
"""autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "fiesta"
autos[2] = "focus" """

"""8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla."""
"""dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)"""

"""9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla"""
"""compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)"""

"""10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla."""
"""lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)"""