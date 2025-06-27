# PROGRAMACIÓN Ⅰ

## Práctico 5: Funciones

## Alumno: Maximiliano Xavier Rodriguez

### Funciones Secundarias
"""1"""
"""def imprimir_hola_mundo(mensaje): 
  print(mensaje)"""

"""2"""
"""def saludar_usuario(nombre):
  print(f"Hola {nombre}!")"""

"""3"""
"""def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")"""

"""4"""
"""import math
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio"""

"""5"""
"""def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas"""

"""6"""
"""def tabla_multiplicar(num):
  for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")"""

"""7"""
"""def operaciones_basicas(a, b):
  suma = a + b
  resta = a - b
  multiplicacion = a * b
  division = a / b
  resultados = (suma, resta, multiplicacion, division)
  return resultados """

"""8"""
"""def calcular_imc(peso, altura):
  imc = peso / (altura ** 2)
  return imc"""


"""9"""
"""def celsius_a_fahrenheit(celsius):
  temp_f = (celsius * (9/5) + 32)
  return temp_f"""

"""10"""
"""def calcular_promedio(a, b, c):
  promedio = (a+b+c)/3
  print(f"El promedio de sus notas es: {promedio: .2f}")

def pedir_numero(dato):
  numero = int(input(f"Ingrese {dato}: "))
  return numero"""

### Funciones principales
"""1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""
"""imprimir_hola_mundo("Hola Mundo!")"""

"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""
"""nombre_usuario = input("Ingrese su nombre: ")
saludar_usuario(nombre_usuario)"""

"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
dir los datos al usuario y llamar a esta función con los valores in-
gresados."""
"""nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ") 
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)"""

"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
dio como parámetro y devuelva el área del círculo. calcular_peri-
metro_circulo(radio) que reciba el radio como parámetro y devuel-
va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
bas funciones para mostrar los resultados."""
"""radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")"""

"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos-
trar el resultado usando esta función."""
"""pedir_segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(pedir_segundos) 
print(f"{pedir_segundos} segundos equivalen a {horas} horas.")"""

"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun-
ción."""
"""multiplicar = int(input("Ingrese un numero para conocer su tabla de multiplicar: "))
tabla_multiplicar(multiplicar)"""

"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta-
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
sultados de forma clara."""
"""primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))
resultado = operaciones_basicas(primer_numero, segundo_numero)
print(f"El resultado de sumar {primer_numero} + {segundo_numero} es {resultado[0]}")
print(f"El resultado de restar {primer_numero} - {segundo_numero} es {resultado[1]}")
print(f"El resultado de multiplicar {primer_numero} * {segundo_numero} es {resultado[2]}")
print(f"El resultado de dividir {primer_numero} / {segundo_numero} es {resultado[3]}")"""

"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
ción para mostrar el resultado con dos decimales."""
"""peso = int(input("Ingrese su peso en kg: "))
altura = int(input("Ingrese su altura en centimetros: ")) / 100
imc = calcular_imc(peso, altura)
print(f"Su indice de masa corporal es: {imc: .2f}")"""

"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""
"""temp_c = float(input("Ingrese una temperatura en Celsius: "))
temp_f = celsius_a_fahrenheit(temp_c)
print(f"La temperatura en grados Fahrenheit es de: {temp_f}")"""

"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función."""
"""nota_1 = pedir_numero("la primera nota")
nota_2 = pedir_numero("la segunda nota")
nota_3 = pedir_numero("la tercera nota")
calcular_promedio(nota_1, nota_2, nota_3)"""