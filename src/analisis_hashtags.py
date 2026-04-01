posts = [
"Arrancando el lunes con energía #Motivación #NuevaSemana",
"Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi", "No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
"Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
"Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
"Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
"Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
"Finde de lluvia, maratón de series #SerieAdicta #Relax", "Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
]

def crearDicHashtagsUnicos(todosLosHashtags,hashtagsUnicos):
    for hashtag in todosLosHashtags:
        if hashtag not in hashtagsUnicos:
            hashtagsUnicos[hashtag] = 1
        else:
            hashtagsUnicos[hashtag] += 1

def analisisHashtags(posts):
    listaPalabras = []
    todosLosHashtags = []
    hashtagsUnicos = {}
    for linea in posts:
        listaPalabras += linea.split()
    for palabra in listaPalabras:
        if (palabra.startswith("#")):
            todosLosHashtags.append(palabra)
    crearDicHashtagsUnicos(todosLosHashtags,hashtagsUnicos)
    hashtagsUnicos = sorted(hashtagsUnicos.items(), key=lambda elemento: elemento[1], reverse=True)
    
    print("Hashtags trending (más de una aparición): ")
    for clave, valor in hashtagsUnicos:
        if (valor > 1):
            print(f"{clave}: {valor}")
    print("Total de hashtags únicos: ",len(hashtagsUnicos))
analisisHashtags()