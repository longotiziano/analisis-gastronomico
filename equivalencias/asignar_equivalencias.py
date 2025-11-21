from typing import Any

def devolver_clave(valor_dado: Any, diccionario: dict) -> list:
    """
    Función que, dado el valor de alguna clave y diccionario de listas, devuelve las claves correspondientes encontradas
    en aquellas listas.
    """
    return [clave for clave, lista in diccionario.items() if valor_dado in lista]

