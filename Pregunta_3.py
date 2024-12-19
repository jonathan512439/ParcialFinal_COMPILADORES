"""En Python escribe 3 ejemplos para:
a) Errores Lexicos

b) Errores Sintacticos

c) Errores Semanticos

"""
# a) Errores Lexicos:

# Ejemplo 1: Caracter invisible no permitido
va\u200br = 10  # Error: El espacio invisible rompe el nombre de la variable

# Ejemplo 2: Uso de comillas mixtas
mensaje = "Hola mundo'  # Error: Se mezclaron comillas dobles y simples sin cerrarlas correctamente

# Ejemplo 3: Identificador con caracteres de otro idioma

número = 42  # Error en sistemas que no aceptan caracteres fuera del ASCII


# b) Errores Sintacticos:

# Ejemplo 1: Combinación errónea de estructuras
if 5 > 3:
    print("Mayor")
else print("Menor")  # Error: Falta ':' después de 'else'

# Ejemplo 2: Falta de indentficación
def calcular():
valor = 10  # Error: Falta indentificación en el bloque de la función


# Ejemplo 3: Falta de una coma en listas o argumentos
lista = [1, 2, 3  4, 5]  # Error: Falta una coma entre '3' y '4'

# c) Errores Semanticos:

# Ejemplo 1: Comparación lógica incorrecta
x = 10
if x = 5:  # Error semántico disfrazado de sintáctico: '=' es asignación, no comparación
    print("Es igual a 5")


# Ejemplo 2: Reasignación de una variable que genera un error inesperado

resultado = [1, 2, 3]
resultado = resultado.append(4)  # Error semántico: append() modifica la lista y devuelve None


# Ejemplo 3: Manejo erróneo de rangos

for i in range(1, 10):  # La intención es incluir 10, pero el rango excluye el último valor
    if i == 10:
        print("Encontrado")  # Nunca se ejecutará


 