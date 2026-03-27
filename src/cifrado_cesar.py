
def cifrar(desplazamiento,mensaje):
    cifrado=""
    for caracter in mensaje:
        if (caracter >= 'a' and caracter <= 'z'): #es min
            caracter = chr((ord(caracter) - 97 + desplazamiento) % 26 + 97)
            cifrado+=caracter
        elif (caracter >= 'A' and caracter <= 'Z'): #es mayus
            caracter = chr((ord(caracter) - 65 + desplazamiento) % 26 + 65)
            cifrado+=caracter
        else:
            cifrado+=caracter
    return cifrado
 
                
def cifradoCesar():
    mensaje = input("Ingrese un mensaje: ")
    try:
        desplazamiento = int(input("Ingrese el desplazamiento: "))
        
    except ValueError:
        print("no se puede llevar a cabo el cifrado cesar, no ingreso un numero entero")
        return

    cifrado = cifrar(desplazamiento,mensaje)
    descifrado = cifrar(-desplazamiento,cifrado)
    print("Mensaje cifrado: ",cifrado)
    print("Mensaje descifrado: ", descifrado)
    
