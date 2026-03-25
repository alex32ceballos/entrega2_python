import string
import textwrap #biblioteca para formatear el texto de salida



def filtroSpoilers(): #no tengo en cuenta los saltos de linea
    review = """La película sigue a un grupo de astronautas que
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo
a través
de tormentas solares y fallos en el sistema de navegación. Al
llegar
a Marte descubren que la base está abandonada y los
suministros
destruidos. Torres decide sacrificar la nave nodriza para
salvar
al equipo y logran volver a la Tierra en una cápsula de
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje
secreto."""
    palabras = input("Ingrese las palabras spoiler (separadas por coma): ").replace(" ","").split(",")
    reviewLista = review.split()
    for i,palabraReview in enumerate(reviewLista): #recorro la lista de palabras de review con indice i
        for palabra in palabras:
            palabraReviewSinCarRaros = palabraReview.strip(string.punctuation)
            if palabra.lower() == palabraReviewSinCarRaros.lower():
                reviewLista[i] = reviewLista[i].replace(palabraReviewSinCarRaros,"*"*len(palabraReviewSinCarRaros))
                break
    reviewLista = " ".join(reviewLista)
    
    print(textwrap.fill(reviewLista, width=62)) #organiza el string en maximo 62 caracteres por linea



