playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]

def convertirMinSeg(datos):
    minYseg = datos.split(":")
    minutos = int(minYseg[0])
    segundos = int(minYseg[1])
    return minutos, segundos
    
def sumarDuracion(minTotal,segTotal, minutos, segundos):
    segTotal = segTotal + segundos
    minTotal = minTotal + minutos
    if segTotal >= 60:
        segTotal -= 60
        minTotal += 1

    return minTotal, segTotal
        
def cancionEsLaMasLarga(minMasLargo,segMasLargo,minutos,segundos,):
    totalSegundos = minutos * 60 + segundos
    totalMasLargosSegundos = minMasLargo * 60 + segMasLargo
    return totalSegundos > totalMasLargosSegundos

def cancionEsLaMasCorta(minMasCorto,segMasCorto,minutos,segundos):
    totalSegundos = minutos * 60 + segundos
    totalMasCortosSegundos = minMasCorto * 60 + segMasCorto
    return totalSegundos < totalMasCortosSegundos

def duracionesPlaylist(playlist):
    minTotal = 0
    segTotal = 0
    minMasLargo = 0
    segMasLargo = 0
    cancionMasLarga = {}
    minMasCorto = 9999
    segMasCorto = 9999
    cancionMasCorta = {}
    for cancion in playlist:
        minutos,segundos = convertirMinSeg(cancion["duration"])
        minTotal, segTotal = sumarDuracion(minTotal, segTotal, minutos, segundos)
        if (cancionEsLaMasLarga(minMasLargo,segMasLargo,minutos,segundos)):
            minMasLargo = minutos
            segMasLargo = segundos
            cancionMasLarga = cancion.copy()
        if (cancionEsLaMasCorta(minMasCorto,segMasCorto,minutos,segundos)):
            minMasCorto = minutos
            segMasCorto = segundos
            cancionMasCorta = cancion.copy()
    print(f"Duracion total: {minTotal}m {segTotal}s")
    print(f"Cancion mas larga: '{cancionMasLarga['title']}' ({minMasLargo}:{segMasLargo:02d})") #minimo 2 enteros
    print(f"Cancion mas corta: '{cancionMasCorta['title']}' ({minMasCorto}:{segMasCorto:02d})")
