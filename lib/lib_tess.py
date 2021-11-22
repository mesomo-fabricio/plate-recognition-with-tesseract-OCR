def diminuir(str):
    max = 7 # Numero Maximo de caracteres Permitidos.
    if len(str) > max:
        return str[:max]
    else:
        return str