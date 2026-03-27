students = [
{"name": " Ana García ", "grade": "8", "status":"aprobado"},
{"name": "pedro lópez", "grade": "4", "status":"DESAPROBADO"},
{"name": "MARÍA FERNÁNDEZ", "grade": "10", "status":"Aprobado"},
{"name": "ana garcía", "grade": "9", "status":"aprobado"},
{"name": None, "grade": "7", "status": "aprobado"},
{"name": "Luis Martínez ", "grade": None, "status":"aprobado"},
{"name": " carlos RUIZ", "grade": "6", "status":"aprobado"},
{"name": "PEDRO LÓPEZ ", "grade": "3", "status":"desaprobado"},
{"name": " ", "grade": "5", "status": "aprobado"},
{"name": "María Fernández", "grade": "7", "status":"APROBADO"},
{"name": "Sofía Torres", "grade": "9", "status":"Aprobado"},
{"name": " sofía torres ", "grade": "8", "status":"aprobado"},
{"name": "Carlos Ruiz", "grade": "6", "status":"APROBADO"},
{"name": "Roberto Díaz", "grade": "absent", "status":"ausente"},
{"name": "roberto díaz", "grade": "", "status":"Ausente"},
{"name": None, "grade": None, "status": None},
{"name": "Laura Méndez", "grade": "7", "status":"aprobado"},
{"name": " laura méndez", "grade": "8", "status":"Aprobado"},
{"name": "GABRIELA RÍOS", "grade": "5", "status":"aprobado"},
{"name": "gabriela ríos ", "grade": "4", "status":"Desaprobado"},
]

def eliminarRegistroNombreBasura(nombre):
    if (nombre == None):
        return True 
    nombre = nombre.strip()
    if (nombre == ""):
        return True
    return False
    
def eliminarRegistroNotaBasura(nota):
    if (nota == None):
        return True 
    nota = nota.strip()
    if (nota == ""):
        return True
    try:
        nota = float(nota)
        return False
    except ValueError:
        return True
    

def normalizarNombre(nombre):
    return nombre.strip().title()

def normalizarEstado(estado):
    return estado.strip().title()


def imprimir(mejores):
    print("Registros limpios de alumnos: ")
    print("-----------------------------------------------------")
    print(f"Nombre                   Nota               Estado")
    print("")
    for diccionario in mejores:
        print(f'{diccionario["name"]:<25} {diccionario["grade"]:<17} {diccionario["status"]}')
    print(f"Total de alumnos válidos: {len(mejores)}")

def normalizarRegistrosAlumnos(students):
    mejores = {} #un diccionario con clave "name" y valor el diccionario datos. Almacena las mejores notas y datos de los estudiantes sin repetir
    for estudiante in students:
        
        if eliminarRegistroNombreBasura(estudiante["name"]):
            continue
        if eliminarRegistroNotaBasura(estudiante["grade"]):
            continue

        datos = {
            "name":normalizarNombre(estudiante["name"]),
            "grade":float(estudiante["grade"]),
            "status":normalizarEstado(estudiante["status"])
        }
        
        #chequeo si datos esta, o si esta veo si la nota es mayor o menor asi reemplazo
        if (datos["name"] not in mejores) or (datos["grade"] > mejores[datos["name"]]["grade"]):
            mejores[datos["name"]] = datos
            
    mejores = list(mejores.values())
    mejores.sort(key=lambda x:x["name"]) #ordeno la nueva lista
    imprimir(mejores)
    
        
normalizarRegistrosAlumnos(students)