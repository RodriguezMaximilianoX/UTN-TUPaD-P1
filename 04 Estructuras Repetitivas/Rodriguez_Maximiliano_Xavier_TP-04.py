# PROGRAMACIÓN Ⅰ

## Práctico 4: Estructuras repetitivas

## Alumno: Maximiliano Xavier Rodriguez

### Actividades

"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""
"""for i in range(101):
    print(i)"""

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""
"""numero = int(input("Ingrese un numero entero: "))
contador = 0
numero_original = numero
while numero > 0: 
    numero //= 10
    contador += 1
print(f"El numero {numero_original} tiene {contador} digitos.")"""

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""
"""inicio = int(input("Ingrese el valor inicial: "))
fin = int(input("Ingrese el valor final: "))
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print(f"La suma de los numeros entre {inicio} y {fin} es: {suma}")"""

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""
"""numero = int(input("Ingrese un numero entero (0 para terminar): "))
suma = 0
while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro numero entero (0 para terminar): "))
print(f"La suma total es: {suma}")"""

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
"""import random
numero_aleatorio = random.randint(0, 9)
numero_usuario = int(input("Adivina un numero entre 0 y 9: "))
intentos = 1
while numero_usuario != numero_aleatorio:
    intentos += 1
    if numero_usuario < numero_aleatorio:
        print("El numero es mayor. Intenta de nuevo.")
    else:
        print("El numero es menor. Intenta de nuevo.")
    numero_usuario = int(input("Adivina un numero entre 0 y 9: "))
print(f"¡Felicidades! Has adivinado el numero {numero_aleatorio} en {intentos} intentos.")"""

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""
"""for i in range(100, -1, -2):
    print(i)"""

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""
"""numero = int(input("Ingrese un numero entero positivo: "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print(f"La suma de los numeros entre 0 y {numero} es: {suma}")"""

"""8) Escribe un programa que permita al usuario ingresar 5 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos."""
"""cont = 0
pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range(100):
    numero = int(input(f"Ingrese el numero {i + 1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1
    cont += 1
print(f"Cantidad de numeros pares: {pares}")
print(f"Cantidad de numeros impares: {impares}")  
print(f"Cantidad de numeros negativos: {negativos}")
print(f"Cantidad de numeros positivos: {positivos}")"""

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. """
"""suma = 0
for i in range(100):
    numero = int(input(f"Ingrese el numero {i + 1}: "))
    suma += numero
media = suma / 100
print(f"La media de los numeros ingresados es: {media}")"""

"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario."""
numero = int(input("Ingrese un numero entero: "))
numero = abs(numero)
numero_invertido = 0
while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10
print(f"El numero invertido de {numero} es: {numero_invertido}")
