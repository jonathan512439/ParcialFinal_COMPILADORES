def automata(input_string):
    """
   Pregunta 1. Inciso d)
   
    param input_string: Cadena de entrada para evaluar.
    return: True si la cadena es aceptada, False en caso contrario.
    """
    # Estado inicial
    state = "q0"
    for char in input_string:
        if state == "q0":
            if char == "m":
                state = "q1"
            elif char == "h":
                state = "q2"
            else:
                return False
        elif state == "q1":
            if char == "a":
                state = "q2"
            elif char == "h":
                state = "q3"
            else:
                return False
        elif state == "q2":
            if char == "m":
                state = "q1"
            else:
                return False
        elif state == "q3":
            if char == "a":
                state = "q3"
            else:
                return False
    return state in {"q2", "q3"}

# Empleo del codigo en casos de uso:
if __name__ == "__main__":
    test_cases = ["m", "mh", "mma", "ma", "hmmh", "hma", "mmmaa", "h", "a", "hamah", "maham", "hmamamamha"]
    print("Resultados de las cadenas de prueba:")
    for case in test_cases:
        print(f"Cadena: '{case}' -> {'Aceptada' if automata(case) else 'Rechazada'}")