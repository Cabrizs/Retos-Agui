identificador_unico = int(input("Hola Elfo! Digita el identificador numérico de tu regalo y te diremos a qué tipo de persona corresponde:\n"))
def clasificar_regalo(identificador_unico):
    if identificador_unico < 100 or identificador_unico > 999:
        return "Identificador no válido. Debe ser un número entre 100 y 999."
    elif identificador_unico % 2 == 0:
        if str(identificador_unico) == str(identificador_unico)[::-1]:
            return "El regalo es para un Niño."
        else:
            return "El regalo es para un Hombre."
    else:
        if str(identificador_unico) == str(identificador_unico)[::-1]:
            return "El regalo es para una Niña."
        else:
            return "El regalo es para una Mujer."
print(clasificar_regalo(identificador_unico))