hastaUnKG = (500,1000,2000)
entreUnoYcincoKG = (1000, 2500, 4500)
masCincoKG = (2000, 5000, 8000)
zonasValidas = ("local","regional","nacional")

def buscarZonaSegunPeso(zona, zonasValidas):
    posicion = 0
    for i in zonasValidas:
        if zona == zonasValidas[posicion]:
            break
        posicion += 1
    return posicion

def buscarCostoEnvio(peso,posicion):
    match peso:
        case _ if (peso > 0 and peso <= 1):
            costoEnvio = hastaUnKG[posicion]
        case _ if (peso > 1 and peso <= 5):
            costoEnvio = entreUnoYcincoKG[posicion]
        case _ if (peso >5):
            costoEnvio = masCincoKG[posicion]
    return costoEnvio
        
def calcular():
    peso = input("Ingrese peso del paquete: ")
    try:
        peso = float(peso)
        if (float(peso) > 0):
            peso = float(peso)
            zona = input("Ingrese la zona de destino (local/regional/nacional): ").lower()
            if (zona in zonasValidas):
                posicion = buscarZonaSegunPeso(zona,zonasValidas)
                costoEnvio = buscarCostoEnvio(peso,posicion)
                print("Costo de envio: ", costoEnvio)
            else:
                print("Zona no válida. Las zonas disponibles son: local, regional, nacional.")
        else:
            print("el peso es erroneo")
    except:
        print("el peso es erroneo")
    
calcular()