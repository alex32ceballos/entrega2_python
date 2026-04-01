rounds = [
    {'theme': 'Entrada',
    'scores': {
        'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
        'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
        'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
        'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
        'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
        }
    },

    {'theme': 'Plato principal',
    'scores': { 'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                }
    },

    {'theme': 'Postre',
     'scores': {'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                'Mateo':{'judge_1': 9, 'judge_2': 9,'judge_3': 8},
                'Camila':{'judge_1': 8, 'judge_2': 7,'judge_3': 9},
                'Santiago': {'judge_1': 7, 'judge_2': 7,'judge_3': 6},
                'Lucía':{'judge_1': 9, 'judge_2': 9,'judge_3': 9},
            }
    },

    {
    'theme': 'Cocina internacional',
    'scores': {
                'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},
                'Mateo':{'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},
                'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
            }
    },

    {
    'theme': 'Final libre',
    'scores': {
                'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},
                'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},
                'Camila':{'judge_1': 7, 'judge_2': 7, 'judge_3': 7},
                'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
                'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
            }
    }
]


def imprimirTablaRonda(ordenadoActual):
    print("cocinero      puntaje")
    for participante,datos in ordenadoActual:
        print(f'{participante:10} {datos["puntaje"]:8}')
    print("")


def mejorPuntajeRonda(puntaje,participante,mejorPuntaje,mejorCocinero):
    if (mejorCocinero == "") and (mejorPuntaje == -1):
        mejorCocinero = participante
        mejorPuntaje = puntaje
    else:
        if (puntaje > mejorPuntaje):
            mejorCocinero = participante
            mejorPuntaje = puntaje
    return mejorPuntaje,mejorCocinero

def imprimirTablaFinal(tablaPosicionesFinal):
    ordenado = sorted(tablaPosicionesFinal.items(), key=lambda x:x[1]["puntaje"], reverse=True)
    print("Tabla de posiciones final:")
    print("Cocinero      puntaje     rondas ganadas     mejor ronda      promedio")
    for participante,datos in ordenado:
        print(f'{participante:10} {datos["puntaje"]:8} {datos["rondas ganadas"]:13} {datos["mejor ronda"]:18} {datos["promedio"]:16}')


def inicializarTablaFinal(rounds,tablaPosicionesFinal):
    for ronda in rounds:
        participantes = ronda["scores"]
        for participante in participantes:
            tablaPosicionesFinal[participante] = {
                "puntaje":0,
                "rondas ganadas":0,
                "mejor ronda":0,
                "promedio":0
            }
            
def actualizarTablaFinal(tablaPosicionesFinal,participante,puntaje,posicion):
    tablaPosicionesFinal[participante]["puntaje"] += puntaje
    tablaPosicionesFinal[participante]["promedio"] = tablaPosicionesFinal[participante]["puntaje"] / posicion
    if (puntaje > tablaPosicionesFinal[participante]["mejor ronda"]):
        tablaPosicionesFinal[participante]["mejor ronda"] = puntaje
    
    
def competenciaCocinaRanking(rounds):
    tablaPosicionesFinal = {}
    inicializarTablaFinal(rounds,tablaPosicionesFinal)
    for i,ronda in enumerate(rounds):
        posicion = i + 1
        print(f'Ronda {posicion} - {ronda["theme"]}')
        
        participantes = ronda["scores"] #dicc de participantes
        mejorCocinero = ""
        mejorPuntaje = -1
        rondaActual = {}
        for participante in participantes: #participante es la clave(string) de participantes
            puntaje = sum(participantes[participante].values())
            
            rondaActual[participante] = {"puntaje":puntaje} #agrego en ronda actual
            
            mejorPuntaje,mejorCocinero = mejorPuntajeRonda(puntaje,participante,mejorPuntaje,mejorCocinero)
        
            actualizarTablaFinal(tablaPosicionesFinal,participante,puntaje,posicion)
                    
        tablaPosicionesFinal[mejorCocinero]["rondas ganadas"] += 1
        print(f"Ganador: {mejorCocinero} ({mejorPuntaje})")
        
        ordenadoActual = sorted(rondaActual.items(), key=lambda x:x[1]["puntaje"], reverse=True)
        
        imprimirTablaRonda(ordenadoActual)
        
    imprimirTablaFinal(tablaPosicionesFinal)
    
competenciaCocinaRanking(rounds)