


def cantTotalLineas(text):
    lineas = len(text.split(".\n"))
    return lineas

def cantTotalPalabras(text):
    palabrasCant = len(text.split())
    return palabrasCant
    
def promedioPalabrasPorLinea(text):
    promedio = cantTotalPalabras(text) / cantTotalLineas(text)
    return round(promedio,2)
    
def lineasArribaPromedio(text):
    lineas = text.split(".\n")
    promedio = promedioPalabrasPorLinea(text)
    print("Líneas por encima del promedio (7.21 palabras)")
    for palabra in lineas:
        if (len(palabra.split()) > promedio):
            print(f'- "{palabra}." ({len(palabra.split())} palabras)')

def estadisticasTexto():
    text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way
to do it.
Although that way may not be obvious at first unless you're
Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good
idea.
Namespaces are one honking great idea -- let's do more of
those!"""
    print("Total de lineas: ",cantTotalLineas(text))
    print("Total de palabras: ",cantTotalPalabras(text))
    print("Promedio de palabras por línea: ",promedioPalabrasPorLinea(text))
    print(lineasArribaPromedio(text))
    
estadisticasTexto()