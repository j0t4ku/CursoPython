# Documentacion y pruebas 



def areaTriangulo(base,altura):
    """
    Funcion que calcula el area del triangulo
    Resive dos parametros (base y altura)
    >>> areaTriangulo(3,6)
    'El area del triangulo es 9.0'
    >>> areaTriangulo(4,5)
    'El area del triangulo es 10.0'
    >>> areaTriangulo(3,9)
    'El area del triangulo es 13.5'
    """
    return "El area del triangulo es "+ str((base*altura)/2)



def verificarEmail(email):
    """
        Funcion comprueba si el email recibido es correcto
        Busca la posicion del @ 
        >>> verificarEmail('joel@gmail.com')
        True
        >>> verificarEmail('joel@gmail.com@')
        False
    """
    arroba=email.count('@')
    if(arroba != 1 or email.rfind('@')==(len(email)-1) or email.find('@')==0):
        return False
    else:
        return True 






import doctest

doctest.testmod()
