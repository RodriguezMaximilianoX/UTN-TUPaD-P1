# PROGRAMACIÓN Ⅰ

## Práctico 3: Estructuras condicionales 

## Alumno: Maximiliano Xavier Rodriguez

### Actividades

"""1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

age = int(input("Ingrese su edad: "))
if age > 18:
  print("Eres mayor de edad")

"""2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”."""

score = int(input("Ingrese la nota de su examen: "))
if score >= 6:
  print("Aprobado")
else:
  print("Desaprobado")

"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar."""

number = int(input("Ingrese por favor un numero par: "))
if number % 2 == 0: 
  print("Ha ingresado un numero par")
else: 
  print("Por favor, ingrese un numero par")

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
"""

age = int(input("Ingrese su edad: "))
if age > 0 and age < 12: 
  print("Usted es un niño/a")
elif age >= 12 and age < 18:
  print("Usted es un adolescente")
elif age >= 18 and age < 30:
  print("Usted es un adulto/a joven")
elif age >= 30:
  print("Usted es un adulto/a mayor")
else:
  print("La edad ingresada no es valida")

"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
"""

password = input("Ingrese su contraseña que tenga entre 8 y 14 caracteres: ")
if len(password) >= 8 and len(password) <= 14:
  print("Ha ingresado una contraseña correcta")
else: print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

"""6) Escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
"""
from statistics import mode, median, mean
import random 

"""Lista de numeros"""
numeros_aleatorios = [random.randint(1,100) for i in range(50)]

"""Calcular media, mediana y moda"""
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

"""Valores de media, mediana y moda"""
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

"""Determinar sesgo"""
if media > mediana and mediana > moda:
  print("Sesgo positivo (asimetria a la derecha)")
elif media < mediana and mediana < moda: 
  print("Sesgo negativo (asimetria izquierda)")
else: print("No hay sesgo (distribucion simetrica)")

"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
"""

texto = input("Ingrese una frase o palabra: ")
if texto[-1].lower() in "aeiou": 
  texto += "!"
  print(texto)
else: print(texto)

"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas."""

name = input("Ingrese su nombre: ")
style_text = int(input("Ingrese 1 si quiere ver su nombre en mayusculas, 2 si quiere ver su nombre en minusculas o 3 si quiere ver su nombre con la primera letra mayúscula: "))

if style_text == 1: 
  print(name.upper())
elif style_text == 2: 
  print(name.lower())
elif style_text == 3:
  print(name.capitalize())
else: print("El numero ingresado no es correcto")

"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

magnitud_terremoto = int(input("Ingrese la escala del terremoto: "))

if magnitud_terremoto < 3: 
  print("Muy leve (imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4: 
  print("Leve (ligeramente perceptible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
  print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
  print("Fuerte (puede causar daños en estructuras debiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
  print("Muy fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
  print("Extremo (puede causar graves daños a gran escala)")
else: print ("El numero ingresado no es correcto")

"""10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano."""

hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Determinar estación según hemisferio
if hemisferio == "S":
    if (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia < 21):
        estacion = "otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia < 21):
        estacion = "invierno"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia < 21):
        estacion = "primavera"
    else:
        estacion = "verano"
elif hemisferio == "N":
    if (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia < 21):
        estacion = "primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia < 21):
        estacion = "verano"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia < 21):
        estacion = "otoño"
    else:
        estacion = "invierno"
else:
    estacion = "Hemisferio inválido"

print("Estás en", estacion)
