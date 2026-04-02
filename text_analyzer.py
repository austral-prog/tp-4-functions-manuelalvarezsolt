# ---- Funciones provistas (NO modificar) ----

def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

# ---- Funciones a implementar ----

def total_letters(text):
    """
    Retorna la cantidad total de letras en el texto.
    Debe USAR las funciones count_vowels y count_consonants.
    """
    letras = count_vowels(text) + count_consonants(text)
    return(letras)

def vowel_percentage(text):
    """
    Retorna el porcentaje de vocales sobre el total de letras, redondeado a 1 decimal.
    Si no hay letras, retorna 0.0.
    Debe USAR las funciones count_vowels y total_letters.

    Ejemplo: "hola" tiene 2 vocales de 4 letras → 50.0
    """
    if count_consonants(text) + count_vowels(text) != 0:
        porcentaje = (count_vowels(text) / total_letters(text)) * 100
        rond = round(porcentaje, 1)
        return(rond)
    else:
        return(0.0)

def analyze_text(text):
    """
    Retorna un string con el análisis completo del texto usando el siguiente formato:
    "V:{vowels} C:{consonants} T:{total} P:{percentage}%"

"""
    return(f"V:{count_vowels(text)} C:{count_consonants(text)} T:{total_letters(text)} P:{vowel_percentage(text)}%")

