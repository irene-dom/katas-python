# =============================================================
# Katas de Python · Bootcamp Data & Analytics (ThePower)
# Autora: Irene Domínguez
# Cada kata lleva encima su enunciado (resumido) como comentario
# y debajo una prueba con print().
# Las katas que piden datos al usuario (8, 11, 31, 38 y 41) usan input().
# =============================================================

from functools import reduce


# =============================================================
# KATAS 1
# =============================================================

# -------------------------------------------------------------
# Kata 1
# Escribe una función que reciba una cadena de texto y devuelva un
# diccionario con la frecuencia de cada letra. Los espacios no se cuentan.
# -------------------------------------------------------------
def frecuencia_letras(texto):
    frecuencias = {}
    for letra in texto:
        if letra == " ":
            continue                      # saltamos los espacios
        if letra in frecuencias:
            frecuencias[letra] += 1       # ya estaba: sumamos 1
        else:
            frecuencias[letra] = 1        # primera vez que aparece
    return frecuencias

print("Kata 1:", frecuencia_letras("hola mundo"))


# -------------------------------------------------------------
# Kata 2
# Dada una lista de números, obtén una nueva lista con el doble de cada
# valor. Usa la función map().
# -------------------------------------------------------------
def doblar_valores(numeros):
    return list(map(lambda x: x * 2, numeros))

print("Kata 2:", doblar_valores([1, 2, 3, 4]))


# -------------------------------------------------------------
# Kata 3
# Escribe una función que reciba una lista de palabras y una palabra
# objetivo, y devuelva las palabras de la lista que contienen el objetivo.
# -------------------------------------------------------------
def palabras_que_contienen(lista_palabras, objetivo):
    return [palabra for palabra in lista_palabras if objetivo in palabra]

print("Kata 3:", palabras_que_contienen(["casa", "casco", "perro", "cascada"], "cas"))


# -------------------------------------------------------------
# Kata 4
# Genera una función que calcule la diferencia entre los valores de dos
# listas. Usa la función map().
# -------------------------------------------------------------
def diferencia_listas(lista1, lista2):
    return list(map(lambda a, b: a - b, lista1, lista2))

print("Kata 4:", diferencia_listas([10, 20, 30], [1, 2, 3]))


# -------------------------------------------------------------
# Kata 5
# Escribe una función que reciba una lista de números y un parámetro
# opcional nota_aprobado (por defecto 5). Calcula la media y devuelve una
# tupla con la media y el estado: "aprobado" si la media es mayor o igual
# que nota_aprobado, o "suspenso" si es menor.
# -------------------------------------------------------------
def media_y_estado(notas, nota_aprobado=5):
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

print("Kata 5:", media_y_estado([6, 4, 7, 5]))
print("Kata 5 (aprobado en 7):", media_y_estado([6, 4, 7, 5], nota_aprobado=7))


# -------------------------------------------------------------
# Kata 6
# Escribe una función que calcule el factorial de un número de forma
# recursiva.
# -------------------------------------------------------------
def factorial(n):
    if n <= 1:                            # caso base: 0! = 1! = 1
        return 1
    return n * factorial(n - 1)           # la función se llama a sí misma

print("Kata 6:", factorial(5))


# -------------------------------------------------------------
# Kata 7
# Genera una función que convierta una lista de tuplas en una lista de
# cadenas (strings). Usa la función map().
# -------------------------------------------------------------
def tuplas_a_cadenas(lista_tuplas):
    return list(map(lambda t: " ".join(str(x) for x in t), lista_tuplas))

print("Kata 7:", tuplas_a_cadenas([("hola", "mundo"), (1, 2, 3)]))


# -------------------------------------------------------------
# Kata 8
# Escribe un programa que pida al usuario dos números e intente
# dividirlos. Si el usuario escribe un valor no numérico o intenta dividir
# entre cero, maneja esas excepciones. Muestra un mensaje si la división
# se hace correctamente.
# -------------------------------------------------------------
def dividir_numeros():
    try:
        num1 = float(input("Kata 8 · Escribe el primer número: "))
        num2 = float(input("Kata 8 · Escribe el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        print("Kata 8: error, tienes que escribir un número.")
    except ZeroDivisionError:
        print("Kata 8: error, no se puede dividir entre cero.")
    else:
        print(f"Kata 8: la división fue exitosa. Resultado = {resultado}")

dividir_numeros()


# -------------------------------------------------------------
# Kata 9
# Escribe una función que reciba una lista de nombres de mascotas y
# devuelva una nueva lista sin las prohibidas en España: "Mapache",
# "Tigre", "Serpiente Pitón", "Cocodrilo" y "Oso". Usa la función filter().
# -------------------------------------------------------------
def mascotas_permitidas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, mascotas))

print("Kata 9:", mascotas_permitidas(["Perro", "Tigre", "Gato", "Oso", "Loro"]))


# -------------------------------------------------------------
# Kata 10
# Escribe una función que calcule el promedio de una lista de números.
# Si la lista está vacía, lanza una excepción personalizada y manéjala.
# -------------------------------------------------------------
class ListaVaciaError(Exception):
    """Excepción personalizada para cuando la lista no tiene elementos."""
    pass

def promedio(numeros):
    if len(numeros) == 0:
        raise ListaVaciaError("La lista está vacía, no se puede calcular el promedio.")
    return sum(numeros) / len(numeros)

try:
    print("Kata 10:", promedio([4, 8, 6]))
    print("Kata 10:", promedio([]))
except ListaVaciaError as error:
    print("Kata 10: error ->", error)


# -------------------------------------------------------------
# Kata 11
# Escribe un programa que pida al usuario su edad. Si escribe un valor no
# numérico o fuera de rango (menor que 0 o mayor que 120), maneja las
# excepciones.
# -------------------------------------------------------------
def pedir_edad():
    try:
        edad = int(input("Kata 11 · Escribe tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("fuera de rango")
    except ValueError as error:
        if str(error) == "fuera de rango":
            print("Kata 11: error, la edad tiene que estar entre 0 y 120.")
        else:
            print("Kata 11: error, tienes que escribir un número entero.")
    else:
        print(f"Kata 11: tu edad es {edad} años.")

pedir_edad()


# -------------------------------------------------------------
# Kata 12
# Genera una función que, dada una frase, devuelva una lista con la
# longitud de cada palabra. Usa la función map().
# -------------------------------------------------------------
def longitud_palabras(frase):
    return list(map(len, frase.split()))

print("Kata 12:", longitud_palabras("me gusta mucho programar"))


# -------------------------------------------------------------
# Kata 13
# Genera una función que, para un conjunto de caracteres, devuelva una
# lista de tuplas con cada letra en mayúscula y en minúscula. Las letras
# no pueden estar repetidas. Usa la función map().
# -------------------------------------------------------------
def mayus_minus(caracteres):
    letras_unicas = sorted(set(c for c in caracteres.lower() if c.isalpha()))  # solo letras, sin repetir
    return list(map(lambda c: (c.upper(), c), letras_unicas))

print("Kata 13:", mayus_minus("Hola mama"))


# -------------------------------------------------------------
# Kata 14
# Crea una función que devuelva las palabras de una lista que empiezan
# por una letra concreta. Usa la función filter().
# -------------------------------------------------------------
def empiezan_por(palabras, letra):
    return list(filter(lambda p: p.lower().startswith(letra.lower()), palabras))

print("Kata 14:", empiezan_por(["Pera", "manzana", "piña", "uva"], "p"))


# -------------------------------------------------------------
# Kata 15
# Crea una función lambda que sume 3 a cada número de una lista.
# -------------------------------------------------------------
sumar_tres = lambda numeros: [n + 3 for n in numeros]

print("Kata 15:", sumar_tres([1, 2, 3]))


# -------------------------------------------------------------
# Kata 16
# Escribe una función que reciba un texto y un número entero n, y
# devuelva las palabras más largas que n. Usa la función filter().
# -------------------------------------------------------------
def palabras_mas_largas(texto, n):
    return list(filter(lambda p: len(p) > n, texto.split()))

print("Kata 16:", palabras_mas_largas("el análisis de datos es divertido", 4))


# -------------------------------------------------------------
# Kata 17
# Crea una función que convierta una lista de dígitos en el número
# correspondiente. Por ejemplo, [5, 7, 2] -> 572. Usa la función reduce().
# -------------------------------------------------------------
def digitos_a_numero(digitos):
    return reduce(lambda acumulado, d: acumulado * 10 + d, digitos)

print("Kata 17:", digitos_a_numero([5, 7, 2]))


# -------------------------------------------------------------
# Kata 18
# Escribe un programa que cree una lista de diccionarios con información
# de estudiantes (nombre, edad, calificación) y extraiga los que tienen
# una calificación mayor o igual que 90. Usa la función filter().
# -------------------------------------------------------------
estudiantes = [
    {"nombre": "Ana", "edad": 21, "calificacion": 95},
    {"nombre": "Luis", "edad": 23, "calificacion": 82},
    {"nombre": "Marta", "edad": 22, "calificacion": 90},
    {"nombre": "Pablo", "edad": 24, "calificacion": 67},
]
sobresalientes = list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

print("Kata 18:", sobresalientes)


# -------------------------------------------------------------
# Kata 19
# Crea una función lambda que filtre los números impares de una lista.
# -------------------------------------------------------------
filtrar_impares = lambda numeros: list(filter(lambda n: n % 2 != 0, numeros))

print("Kata 19:", filtrar_impares([1, 2, 3, 4, 5, 6, 7]))


# -------------------------------------------------------------
# Kata 20
# Para una lista con elementos de tipo entero y cadena, obtén una nueva
# lista solo con los enteros. Usa la función filter().
# -------------------------------------------------------------
def solo_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))

print("Kata 20:", solo_enteros([1, "dos", 3, "cuatro", 5]))


# -------------------------------------------------------------
# Kata 21
# Crea una función que calcule el cubo de un número usando una lambda.
# -------------------------------------------------------------
cubo = lambda x: x ** 3

print("Kata 21:", cubo(3))


# -------------------------------------------------------------
# Kata 22
# Dada una lista numérica, obtén el producto total de sus valores. Usa la
# función reduce().
# -------------------------------------------------------------
def producto_total(numeros):
    return reduce(lambda a, b: a * b, numeros)

print("Kata 22:", producto_total([2, 3, 4]))


# -------------------------------------------------------------
# Kata 23
# Concatena una lista de palabras. Usa la función reduce().
# -------------------------------------------------------------
def concatenar(palabras):
    return reduce(lambda a, b: a + " " + b, palabras)

print("Kata 23:", concatenar(["Python", "es", "genial"]))


# -------------------------------------------------------------
# Kata 24
# Calcula la diferencia total de los valores de una lista. Usa la función
# reduce().
# -------------------------------------------------------------
def diferencia_total(numeros):
    return reduce(lambda a, b: a - b, numeros)

print("Kata 24:", diferencia_total([100, 20, 5]))


# -------------------------------------------------------------
# Kata 25
# Crea una función que cuente el número de caracteres de una cadena de
# texto.
# -------------------------------------------------------------
def contar_caracteres(texto):
    return len(texto)

print("Kata 25:", contar_caracteres("Hola mundo"))


# =============================================================
# KATAS 2
# =============================================================

# -------------------------------------------------------------
# Kata 26
# Crea una función lambda que calcule el resto de la división entre dos
# números.
# -------------------------------------------------------------
resto = lambda a, b: a % b

print("Kata 26:", resto(17, 5))


# -------------------------------------------------------------
# Kata 27
# Crea una función que calcule el promedio de una lista de números.
# -------------------------------------------------------------
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

print("Kata 27:", calcular_promedio([3, 5, 7, 9]))


# -------------------------------------------------------------
# Kata 28
# Crea una función que busque y devuelva el primer elemento duplicado de
# una lista.
# -------------------------------------------------------------
def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento               # ya lo habíamos visto: es el primero repetido
        vistos.add(elemento)
    return None                           # no hay duplicados

print("Kata 28:", primer_duplicado([3, 1, 4, 1, 5, 3]))


# -------------------------------------------------------------
# Kata 29
# Crea una función que convierta una variable en cadena y enmascare todos
# los caracteres con '#', excepto los cuatro últimos.
# -------------------------------------------------------------
def enmascarar(valor):
    texto = str(valor)
    return "#" * (len(texto) - 4) + texto[-4:]

print("Kata 29:", enmascarar(1234567890123456))


# -------------------------------------------------------------
# Kata 30
# Crea una función que compruebe si dos palabras son anagramas (tienen
# las mismas letras en distinto orden).
# -------------------------------------------------------------
def son_anagramas(palabra1, palabra2):
    limpia1 = palabra1.replace(" ", "").lower()
    limpia2 = palabra2.replace(" ", "").lower()
    return sorted(limpia1) == sorted(limpia2)

print("Kata 30:", son_anagramas("Roma", "amor"), son_anagramas("casa", "cosa"))


# -------------------------------------------------------------
# Kata 31
# Crea una función que pida al usuario una lista de nombres y un nombre
# para buscar. Si el nombre está en la lista, muestra un mensaje de que se
# ha encontrado; si no, lanza una excepción.
# -------------------------------------------------------------
def buscar_nombre():
    nombres = input("Kata 31 · Escribe nombres separados por comas: ")
    lista_nombres = [n.strip() for n in nombres.split(",")]
    buscado = input("Kata 31 · ¿Qué nombre quieres buscar?: ").strip()
    if buscado in lista_nombres:
        print(f"Kata 31: {buscado} está en la lista.")
    else:
        raise ValueError(f"{buscado} no está en la lista.")

try:
    buscar_nombre()
except ValueError as error:
    print("Kata 31: error ->", error)


# -------------------------------------------------------------
# Kata 32
# Crea una función que reciba un nombre completo y una lista de empleados.
# Si el nombre está en la lista, devuelve su puesto; si no, devuelve un
# mensaje indicando que la persona no trabaja aquí.
# -------------------------------------------------------------
def buscar_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aquí."

empleados = [
    {"nombre": "Laura Gómez", "puesto": "Analista de datos"},
    {"nombre": "Carlos Ruiz", "puesto": "Jefe de proyecto"},
]
print("Kata 32:", buscar_puesto("Laura Gómez", empleados))
print("Kata 32:", buscar_puesto("Pedro López", empleados))


# -------------------------------------------------------------
# Kata 33
# Crea una función lambda que sume los elementos correspondientes de dos
# listas.
# -------------------------------------------------------------
sumar_listas = lambda l1, l2: list(map(lambda a, b: a + b, l1, l2))

print("Kata 33:", sumar_listas([1, 2, 3], [10, 20, 30]))


# -------------------------------------------------------------
# Kata 34
# Crea la clase Arbol con un tronco (longitud inicial 1) y una lista de
# ramas (vacía al principio), y los métodos:
#   - crecer_tronco(): aumenta 1 la longitud del tronco.
#   - nueva_rama(): añade una rama de longitud 1.
#   - crecer_ramas(): aumenta 1 la longitud de todas las ramas.
#   - quitar_rama(posicion): elimina la rama de esa posición.
#   - info_arbol(): devuelve la longitud del tronco, el número de ramas y
#     la longitud de cada una.
# Caso de uso: crear un árbol, crecer el tronco 1 unidad, añadir 1 rama,
# crecer las ramas 1 unidad, añadir 2 ramas, quitar la rama de la
# posición 2 y mostrar la información del árbol.
# -------------------------------------------------------------
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        # La posición empieza a contar en 0 (como los índices de Python)
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("No existe una rama en esa posición.")

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitud_ramas": self.ramas,
        }

arbol = Arbol()            # 1. crear el árbol
arbol.crecer_tronco()      # 2. el tronco pasa a medir 2
arbol.nueva_rama()         # 3. ramas = [1]
arbol.crecer_ramas()       # 4. ramas = [2]
arbol.nueva_rama()         # 5. ramas = [2, 1]
arbol.nueva_rama()         #    ramas = [2, 1, 1]
arbol.quitar_rama(2)       # 6. quitamos la de la posición 2 -> [2, 1]
print("Kata 34:", arbol.info_arbol())   # 7. información del árbol


# -------------------------------------------------------------
# Kata 36
# Crea la clase UsuarioBanco con nombre, saldo y si tiene cuenta corriente
# (True o False), y los métodos:
#   - retirar_dinero(cantidad): resta del saldo; error si no hay suficiente.
#   - transferir_dinero(otro_usuario, cantidad): pasa dinero del otro usuario
#     a este; error si el otro no tiene suficiente.
#   - agregar_dinero(cantidad): suma al saldo.
# Caso de uso: crear a Alicia (saldo 100) y a Bob (saldo 50), los dos con
# cuenta corriente; agregar 20 a Bob; transferir 80 de Bob a Alicia;
# retirar 50 de Alicia.
# -------------------------------------------------------------
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene cuenta corriente.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene saldo suficiente para retirar {cantidad} €.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene saldo suficiente para transferir {cantidad} €.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)                      # Bob pasa a tener 70
try:
    alicia.transferir_dinero(bob, 80)       # Bob solo tiene 70 -> error
except ValueError as error:
    print("Kata 36: error ->", error)
alicia.retirar_dinero(50)                   # Alicia pasa a tener 50

print(f"Kata 36: saldo de Alicia = {alicia.saldo} €, saldo de Bob = {bob.saldo} €")


# =============================================================
# KATAS 3
# =============================================================

# -------------------------------------------------------------
# Kata 37
# Crea las funciones contar_palabras(texto), reemplazar_palabras(texto,
# palabra_original, palabra_nueva) y eliminar_palabra(texto, palabra), y
# una función procesar_texto(texto, opcion, *args) que, según la opción
# ("contar", "reemplazar" o "eliminar"), llame a la función que toca.
# Comprueba que todo funciona.
# -------------------------------------------------------------
def contar_palabras(texto):
    conteo = {}
    for palabra in texto.split():
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    palabras = [palabra_nueva if p == palabra_original else p for p in texto.split()]
    return " ".join(palabras)

def eliminar_palabra(texto, palabra):
    return " ".join(p for p in texto.split() if p != palabra)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)
    else:
        raise ValueError("Opción no válida: usa 'contar', 'reemplazar' o 'eliminar'.")

frase = "el gato come y el perro duerme"
print("Kata 37 (contar):", procesar_texto(frase, "contar"))
print("Kata 37 (reemplazar):", procesar_texto(frase, "reemplazar", "gato", "conejo"))
print("Kata 37 (eliminar):", procesar_texto(frase, "eliminar", "el"))


# -------------------------------------------------------------
# Kata 38
# Escribe un programa que pida al usuario la hora y diga si es de día, de
# tarde o de noche.
# -------------------------------------------------------------
def momento_del_dia():
    try:
        hora = int(input("Kata 38 · ¿Qué hora es? (0-23): "))
    except ValueError:
        print("Kata 38: error, escribe un número entero.")
        return
    if hora < 0 or hora > 23:
        print("Kata 38: esa hora no existe.")
    elif 6 <= hora < 14:
        print("Kata 38: es de día.")
    elif 14 <= hora < 21:
        print("Kata 38: es de tarde.")
    else:
        print("Kata 38: es de noche.")

momento_del_dia()


# -------------------------------------------------------------
# Kata 39
# Escribe un programa que convierta una nota numérica en texto:
#   0-69 insuficiente · 70-79 bien · 80-89 muy bien · 90-100 excelente
# -------------------------------------------------------------
def calificacion_texto(nota):
    if nota < 0 or nota > 100:
        return "nota no válida"
    elif nota < 70:
        return "insuficiente"
    elif nota < 80:
        return "bien"
    elif nota < 90:
        return "muy bien"
    else:
        return "excelente"

print("Kata 39:", calificacion_texto(65), calificacion_texto(75),
      calificacion_texto(85), calificacion_texto(95))


# -------------------------------------------------------------
# Kata 40
# Escribe una función que reciba una figura ("rectangulo", "circulo" o
# "triangulo") y una tupla con los datos necesarios, y calcule su área.
# -------------------------------------------------------------
import math

def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return base * altura / 2
    else:
        return "figura no reconocida"

print("Kata 40:", calcular_area("rectangulo", (4, 5)),
      round(calcular_area("circulo", (3,)), 2),
      calcular_area("triangulo", (6, 4)))


# -------------------------------------------------------------
# Kata 41
# Escribe un programa que pida el precio original de un artículo, pregunte
# si tiene cupón de descuento (sí/no) y, si lo tiene, pida su valor. El
# descuento solo se aplica si el cupón es mayor que cero. Muestra el precio
# final. Usa if, elif y else.
# -------------------------------------------------------------
def precio_con_cupon():
    try:
        precio = float(input("Kata 41 · Precio original del artículo: "))
    except ValueError:
        print("Kata 41: error, escribe un número.")
        return
    tiene_cupon = input("Kata 41 · ¿Tienes cupón de descuento? (si/no): ").strip().lower()
    if tiene_cupon in ("si", "sí"):
        try:
            cupon = float(input("Kata 41 · Valor del cupón en €: "))
        except ValueError:
            print("Kata 41: error, escribe un número.")
            return
        if cupon > 0:
            precio_final = max(precio - cupon, 0)
            print(f"Kata 41: precio final con descuento = {precio_final:.2f} €")
        else:
            print(f"Kata 41: el cupón no es válido. Precio final = {precio:.2f} €")
    elif tiene_cupon == "no":
        print(f"Kata 41: precio final sin descuento = {precio:.2f} €")
    else:
        print("Kata 41: respuesta no válida, escribe 'si' o 'no'.")

precio_con_cupon()
