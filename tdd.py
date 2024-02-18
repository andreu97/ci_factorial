def factorial(e):
    if not isinstance(e,int):
        raise TypeError("Error, no has ficat un numero")
    if e==1:
        return 1
    if e<0:
        raise ValueError("Error numero negatiu")
    else:
        return e * factorial(e-1)
    
    