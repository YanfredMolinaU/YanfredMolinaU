def multiplicarRecusivo(num, factor):
    if isinstance(num, int):
        if (factor == 0):
            return 0
        elif (factor == 1):
            return num
        elif (factor < 0):
            return - multiplicarRecusivo(num, -factor)
        else:
            return num + multiplicarRecusivo(num, factor -1)
    else:
        return print('Error tipo de dato')

def divisionRecusivo(dividendo, divisor):
    if (divisor == 0):
        return print('Error: No se puede dividir entre 0')
    elif (dividendo < divisor):
        return 0
    elif (divisor == dividendo):
        return 1
    else:
        return 1 + divisionRecusivo(dividendo - divisor, divisor)

def divisores(num):
    if isinstance(num, int):
        indice = 1, num + 1
        if (num > 0):
            return divisores(num % indice == 0)
        else:
            return print('Error: debe ser un numero positivo')
    else:
        return print('Error: debe ser un numero entero')


    

    
