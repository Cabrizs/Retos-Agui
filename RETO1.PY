identificador_unico = int(input("Hola Elfo! digita el identificador numérico de tu regalo y te diremos a que tipo de persona corresponde:\n"))
if identificador_unico < 100 or identificador_unico > 999:
    print("Identificador no válido. Debe ser un número entre 100 y 999.")
elif identificador_unico % 2 == 0:
    if str(identificador_unico)[0] == str(identificador_unico)[1] == str(identificador_unico)[2]:
        print("El regalo es para un Niño.")
    else:
        
        print("El regalo es para un Hombre.")
else:
    if str(identificador_unico)[0] == str(identificador_unico)[1] == str(identificador_unico)[2]:
        
        print("EL regalo es para una Niña.")
    else:
       
        print("El regalo es para una Mujer.")
