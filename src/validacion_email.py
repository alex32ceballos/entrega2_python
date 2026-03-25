def validacionEmail():
    valido = False
    email = input("Ingrese un email: ")
    if (email.count("@") == 1): #un solo arroba
        partesEmail = email.split("@") #divido el email a partir del arroba
        if (len(partesEmail[0]) >= 1): #tiene al menos un car antes del @
            if(partesEmail[1].count(".") >= 1): #tiene al menos un punto despuesd del @
                if (not email.startswith(("@","."))) and (not (email.endswith(("@",".")))): #no empieza ni termina con "@" y/o "."
                    if (len(partesEmail[1].split(".")[-1]) >= 2): # La parte después del último punto tiene al menos 2 caracteres 
                        valido = True
    if (valido):
        print("El email es válido")
    else:
        print("El email no es válido")
