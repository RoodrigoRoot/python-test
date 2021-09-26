

def suma(num1:int, num2: int) -> int:
    """
    Esta función hace la suma de dos números.
    >>> suma(4, 5)
    9

    Ingresar cades, provocaría una exceción
    >>> suma("1", 2)
    Traceback (most recent call last):
        ...
    TypeError: No se aceptan cadenas
    """
    if type(num1) != int or type(num2) != int:
        raise TypeError("No se aceptan cadenas")
    return num1 + num2

if __name__ == "__main__":
    import doctest
    doctest.testmod()