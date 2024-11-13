
def redondear(numero):
    # Verificar si tiene decimales
    if numero == int(numero):
        # Si no tiene decimales, devolver el número tal cual
        return numero

    # Convertir el número a string para analizar los decimales
    str_numero = str(numero)

    # Extraer la parte decimal como string
    parte_decimal = str_numero.split(".")[1]

    # Si el primer decimal es 5, redondear al entero más cercano
    if parte_decimal[0] == '5':
        return round(numero)  # Redondear al entero más cercano si el primer decimal es 5

    # Si no, también redondear al número entero
    return round(numero)

def buscar(li, ls, datos):
    counter = 0
    for i in datos:
        if(i>=li and i<ls):
            counter = counter + 1
    return counter