'''
consigna
  1)Analizar detenidamente el set de datos
  2)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
  3)Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
  4)Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
  5)Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
  6)Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
  7)Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
  8)Calcular e informar cual es el superhéroe más y menos pesado.
  9)Ordenar el código implementando una función para cada uno de los valores informados.
  Construir un menú que permita elegir qué dato obtener:
  
MENU
  2)nombre de cada superhéroe
  3)nombre de cada superhéroe junto a la altura del mismo
  4)superhéroe más alto (MÁXIMO)
  5)superhéroe más bajo (MÍNIMO)
  6)altura promedio de los  superhéroes (PROMEDIO)
  7)Nombre (Identidad) del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
  8)superhéroe más y menos pesado.
  9)SALIR

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
#CARRIZO LUCAS 1H
from data_stark import lista_heroes

def PuntoDos():
  for nombre in lista_heroes:
      print("Nombre: {0}".format(nombre["nombre"]))

def PuntoTres():
  for nombre in lista_heroes:
    print("Nombre: {0} | Altura: {1}".format(nombre["nombre"],nombre["altura"]))

def PuntoCuatro():
  heroe_max = lista_heroes[0]
  for heroe in lista_heroes:
    if float(heroe_max["altura"])<float(heroe["altura"]):
      heroe_max = heroe
  print("{0} es el heroe mas alto con una altura de: {1}".format(heroe_max["nombre"],heroe_max["altura"]))  

def PuntoCinco():
  heroe_min = lista_heroes[0]
  for heroe_ej5 in lista_heroes:
    if float(heroe_min["altura"])>float(heroe_ej5["altura"]):
      heroe_min = heroe_ej5
  print("{0} es el heore mas bajo con una altura de: {1}".format(heroe_min["nombre"],heroe_min["altura"]))  

def PuntoSeis():
  promedio_altura = 0
  for heroe_promedio in lista_heroes:
    promedio_altura+=float(heroe_promedio["altura"])
  promedio = promedio_altura / len(lista_heroes)
  print("El promedio de altura de todos los heroes es {0} cm".format(promedio))

def PuntoSiete():
  heroe_min = lista_heroes[0]
  heroe_max = lista_heroes[0]
  for heroe_siete in lista_heroes:
    if float(heroe_min["altura"])>float(heroe_siete["altura"]):
      heroe_min = heroe_siete
    elif float(heroe_max["altura"])<float(heroe_siete["altura"]):
      heroe_max = heroe_siete  
  print("La identidad del heroe mas bajo es {0} y la del heroe mas alto es {1}".format(heroe_min["identidad"], heroe_max["identidad"]))

def PuntoOcho():
  heroe_peso_max = lista_heroes[0]
  heroe_peso_min = lista_heroes[0]
  for heroe_8 in lista_heroes:
    if float(heroe_peso_max["peso"])<float(heroe_8["peso"]):
      heroe_peso_max = heroe_8
    elif float(heroe_peso_min["peso"])>float(heroe_8["peso"]):
      heroe_peso_min = heroe_8
  print("{0} es el heroe mas pesado con un peso de: {1}".format(heroe_peso_max["nombre"],heroe_peso_max["peso"]))
  print("{0} es el heore menos pesado con un peso de: {1}".format(heroe_peso_min["nombre"],heroe_peso_min["peso"]))  


while True:
  
  respuesta = input("\n-2)nombre de cada superhéro\n-3)nombre de cada superhéroe junto a la altura del mismo\n-4)superhéroe más alto (MÁXIMO)\n-5)superhéroe más bajo (MÍNIMO)\n-6)altura promedio de los  superhéroes (PROMEDIO)\n-7)Nombre (Identidad) del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)\n-8)superhéroe más y menos pesado.\n-9)SALIR\n\n>")
  if respuesta == "2":
    PuntoDos()
  elif respuesta=="3":
    PuntoTres()
  elif respuesta=="4":
    PuntoCuatro()
  elif respuesta=="5":
    PuntoCinco()  
  elif respuesta=="6":
    PuntoSeis()
  elif respuesta=="7":
    PuntoSiete()
  elif respuesta=="8":
    PuntoOcho()
  elif respuesta=="9":
    break 


