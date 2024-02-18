"""calcul factorial"""
def factorial(e):
    """
    funcio per al factorial
    
    entra: 
        int: num
    ixida:
        int: torna el factorial del num donat
    
    """
    if not isinstance(e,int):
        raise TypeError("Error, no has ficat un numero")
    if e==1:
        return 1
    if e<0:
        raise ValueError("Error numero negatiu")
    return e * factorial(e-1)