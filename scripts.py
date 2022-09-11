def multiplicacion(x, y):

    try:
        a = float(x)
        b = float(y)
        resultado = a*b
        return resultado
    except ValueError:
        return "null"


def division(x, y):

    try:
        a = float(x)
        b = float(y)
        resultado = a/b
        return resultado
    except ValueError:
        return "null"


def resistencia_equivalente_serie(x, y, z):

    try:
        a = float(x)
        b = float(y)
        c = float(z)
        if a and b and c > 0:
            resultado = a + b + c
            return resultado
        else:
            return "null"
    except ValueError:
        return "null"


def resistencia_equivalente_paralelo(x, y, z):

    try:
        a = float(x)
        b = float(y)
        c = float(z)
        if a and b and c > 0:
            resultado = 1/((1/a)+(1/b)+(1/c))
            return resultado
        else:
            return "null"
    except ValueError:
        return "null"


def resistencia_equivalente_paralelo_jre(x, y):

    try:
        a = float(x)
        b = float(y)
        if a > 0 and b > 0:
            resultado = 1/((1/a)+(1/b))
            return resultado
        else:
            return "null"
    except ValueError:
        return "null"


def corriente_total(x, y):

    try:
        a = float(x)
        b = float(y)
        resultado = a/b
        return resultado
    except ValueError:
        return "null"


def potencia_total(x, y):

    try:
        a = float(x)
        b = float(y)
        resultado = a*b
        return resultado
    except ValueError:
        return "null"
