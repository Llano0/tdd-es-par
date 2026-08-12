def es_par(n:int) -> bool:
    """
    Devuelve True si 'n' es un numero par; en caso contrario, False.
    Un entero es par cuando el residuo de dividirlo entre 2 es 0
    """
    return n%2 == 0

def es_multiplo(n:int, m:int) -> bool:
    """
    Devuelve True si 'n' es un numero multiplo de 'm'; en caso contrario, False.
    Un entero no es multiplo de otro cuando el residuo de la división entre ellos no es 0
    """
    return n%m == 0
