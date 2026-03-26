import random

def hayNombresRepetidos(nombres):
    hay = False
    nombresMinusculas = " ".join(nombres).lower()
    nombresMinusculas = nombresMinusculas.split()
    for nombre in nombresMinusculas:
        if (nombresMinusculas.count(nombre) > 1):
            hay = True
            break
    return hay

def imprimirInvalidez(repetidos,nombres):
    if ((repetidos == True) and (len(nombres) < 3)):
        print("Hay nombres repetidos y hay menos de 3 nombres, no se puede llevar a cabo el sorteo")
    elif (repetidos == True):
        print("Hay nombres repetidos, no se puede llevar a cabo el sorteo")
    else:
        print("hay menos de 3 nombres, el sorteo no puede llevarse a cabo")


def limpiarEspacios(nombres):
    for i,nombre in enumerate(nombres):
        nombre = nombre.strip()
        nombres[i] = nombre
        
def sorteoAmigoInvisible():
    nombres = input("ingrese los participantes (Separados por coma): ").split(",")
    limpiarEspacios(nombres)
    nombresMezclados = nombres.copy()
    repetidos = hayNombresRepetidos(nombres)
    if (repetidos == False) and (len(nombres) >= 3):
        while True:
            random.shuffle(nombresMezclados)
            seSuperponen = False
            for i in range(len(nombresMezclados)):
                if (nombres[i] == nombresMezclados[i]):
                    seSuperponen = True
                    break
            if seSuperponen == False:
                break
        
        print("sorteo de amigo invisible:")
        for i in range(len(nombres)):
            print(f"{nombres[i]} --> {nombresMezclados[i]}")
        
    else:
        imprimirInvalidez(repetidos,nombres)
sorteo()
    