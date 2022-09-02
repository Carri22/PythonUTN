'''
1)Analizar detenidamente el set de datos
2)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
3)Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
4)Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
5)Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
6)Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
7)Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
8)Calcular e informar cual es el superhéroe más y menos pesado.
9)Ordenar el código implementando una función para cada uno de los valores informados.
Construir un menú que permita elegir qué dato obtener

EJEMPLO
 {
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  },
'''
from data_stark import lista_heroes
#2 y 3
for nombre in lista_heroes:
    print("Nombre: {0} | Altura: {1}".format(nombre["nombre"],nombre["altura"]))

#4
heroe_max = lista_heroes[0]
altura_max = float(heroe_max["altura"])
nombre_altura_max = heroe_max["nombre"]
for heroe in lista_heroes:
  altura2 = float(heroe["altura"])
  if altura_max<altura2:
    altura_max = altura2
    nombre_altura_max = heroe["nombre"]
print("{0} es el heroe mas alto con una altura de: {1}".format(nombre_altura_max,altura_max))  

#5
heroe_min = lista_heroes[0]
altura_min = float(heroe_min["altura"])
nombre_altura_min = heroe_min["nombre"]
for heroe_ej5 in lista_heroes:
  altura3 = float(heroe_ej5["altura"])
  if altura_min>altura3:
    nombre_altura_min
    altura_min = altura3
    nombre_altura_min = heroe_ej5["nombre"]
print("{0} es el heore mas bajo con una altura de: {1}".format(nombre_altura_min,altura_min))  




