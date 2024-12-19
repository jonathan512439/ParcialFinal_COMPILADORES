import re

def es_valido(file):
    """
    Verifica si una cadena cumple con ka gramatica:
    
    <file>::=<path> "." <extension>|<path>
    <path>::=<path>"/"<dir>|<dir>
    <dir>::="home" |  "var" | "user" | "Documents" | "compi"...
    <extension>::= "txt" | "docx" | "etc" |...
    
    :param input_string: Cadena a verificar
    :return: True si la cadena cumple con la gramática, False en caso contrario
    
    """
    # Paso 1: Separar la cadena en el camino (path) y la extensión (si existe)
    if "." in file:
        path, extension = file.rsplit(".", 1)
    else:
        path = file
        extension = None

    # Paso 2: Verificar si la extensión es válida
    valid_extensions = {"txt", "docx", "etc"}
    if extension and extension not in valid_extensions:
        return False

    # Paso 3: Verificar si el camino es válido
    valid_dirs = {"home", "var", "user", "Documents", "compi", "other"}
    path_parts = path.split("/")

    for part in path_parts:
        if part not in valid_dirs:
            return False

    return True

# Ejemplos de prueba
if __name__ == "__main__":
    test_cases = [
        "home/var/Documents/compi.txt", #Pregunta 3 d), deberia de ser válido
        "home/user/Documents/file.txt", #Invalido
        "var/log/system.log",         #Invalido
        "home/user/file",         #Invalido
    ]
    print("verificacion de ruta segun la implementacion:")
    for case in test_cases:
        print(f"Cadena: '{case}' -> La Ruta es: { 'Valida' if es_valido(case) else 'Invalida'}")
