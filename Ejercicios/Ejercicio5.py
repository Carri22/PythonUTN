'''
Ejercicio Integrador 05

En la base de datos de la división de armamento de industrias Wayne se tiene una información la cual están con la necesidad de cambiar el formato la lista de habilidades con sus respectivos puntos de combate, actualmente cada una de ellas está presente como un diccionario pero para su nuevo sistema requieren que el tipo de dato sea una tupla la cual albergue solamente el nombre de la habilidad y su poder al estilo ("rayo laser", 99). A su vez, todas y cada una de las habilidades deben estar dentro de una lista de habilidades, la cual debe ser el valor de una key que conforme un diccionario, como key par albergarlas usaremos “habilidades_UTN”.
Formato de resultado esperado:

{
 "habilidades_UTN": [("habilidad_alfa", número), ("habilidad_beta", número)] etc.
}

Ordenar la lista de "habilidades_UTN" según el número de cada tupla, de manera ascendente. 
Una vez hecho esto, deberá recorrer dicha lista imprimiendo sus valores,  conjuntamente con la key que integra dicha estructura de datos.

EJEMPLO

habilidades_UTN:
Habilidad 1: habilidad_alfa | Poder: numero
Habilidad 2: habilidad_beta | Poder: numero
Etcétera.

'''
habilidades_UTN = tuple([("Habilidad_1", 64), 
                         ("Habilidad_2", 32),
                         ("Habilidad_3", 256), 
                         ("Habilidad_4", 1024), 
                         ("Habilidad_5", 128), 
                         ("Habilidad_6", 512)])

habilidades = ["Vision-X","Vuelo","Inteligencia","Metamorfosis","Super Velocidad","Magia",]                         

habilidades = [ 
    {
        "Habilidad_1": "Vision-X",
        "Poder": 64
    },
    {
        "Habilidad_2": "Vuelo",
        "Poder": 32
    },
    {
        "Habilidad_3": "Inteligencia",
        "Poder": 256
    },
    {
        "Habilidad_4": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Habilidad_5": "Super Velocidad",
        "Poder": 128
    },
    {
        "Habilidad_6": "Magia",
        "Poder": 512
    }
]

for habilidad in habilidades_UTN:
    print(habilidades_UTN)