'''
A)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
B)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
C)Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
D)Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
E)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
F)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
G)Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
H)Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
I)Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a G)
J)Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K)Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L)Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
M)Listar todos los superhéroes agrupados por color de ojos.
N)Listar todos los superhéroes agrupados por color de pelo.
O)Listar todos los superhéroes agrupados por tipo de inteligencia

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

def nombres_heroes_masculinos():
    for heroe in lista_heroes:
        if heroe["genero"]=="M":
            print("Nombre: {0}".format(heroe["nombre"]))
        else:
            pass    

def nombres_heroes_femeninos():
    for heroe in lista_heroes:
        if heroe["genero"]=="F":
            print("Nombre: {0}".format(heroe["nombre"]))
        else:
            pass 

def heroe_masculino_mas_alto():
    flag = True
    for heroe in lista_heroes:
        if heroe["genero"]=="M" and flag == True:
            altura = float(heroe["altura"])
            flag = False
        if heroe["genero"]=="M":
            if altura<=float(heroe["altura"]):
                altura=float(heroe["altura"])
                nombre=heroe["nombre"]
    print("{0} es el heroe masculino mas alto con una altura de: {1}".format(nombre,altura))

def heroe_femenino_mas_alto():
    flag = True
    for heroe in lista_heroes:
        if heroe["genero"]=="F" and flag == True:
            altura = float(heroe["altura"])
            flag = False
        if heroe["genero"]=="F":
            if altura<=float(heroe["altura"]):
                altura=float(heroe["altura"])
                nombre=heroe["nombre"]
    print("{0} es la heroina mas alta con una altura de: {1}".format(nombre,altura)) 

def heroe_masculino_mas_bajo():
    flag = True
    for heroe in lista_heroes:
        if heroe["genero"]=="M" and flag == True:
            altura = float(heroe["altura"])
            flag = False
        if heroe["genero"]=="M":
            if altura>=float(heroe["altura"]):
                altura=float(heroe["altura"])
                nombre=heroe["nombre"]
    print("{0} es el heroe masculino mas bajo con una altura de: {1}".format(nombre,altura))

def heroe_femenina_mas_baja():
    flag = True
    for heroe in lista_heroes:
        if heroe["genero"]=="F" and flag == True:
            altura = float(heroe["altura"])
            flag = False
        if heroe["genero"]=="F":
            if altura>=float(heroe["altura"]):
                altura=float(heroe["altura"])
                nombre=heroe["nombre"]
    print("{0} es la heroina mas baja con una altura de: {1}".format(nombre,altura))   

def altura_promedia_masculina():
    cont = 0
    altura_total = 0
    for heroe in lista_heroes:
        if heroe["genero"]=="M":
            altura_total+=float(heroe["altura"])
            cont+=1
    print("La altura promedio de los heroes masculinos es: {0}".format(altura_total/cont))

def altura_promedia_femenina():
    cont = 0
    altura_total = 0
    for heroe in lista_heroes:
        if heroe["genero"]=="F":
            altura_total+=float(heroe["altura"])
            cont+=1
    print("La altura promedio de las heroinas es: {0}".format(altura_total/cont))

def identidades_heroes_mas_altos():
    flag_M = True
    flag_F = True
    for heroe in lista_heroes:
        if heroe["genero"]=="M" and flag_M == True:

            altura_M = float(heroe["altura"])
            flag_M = False
        elif heroe["genero"]=="M":
            if altura_M<=float(heroe["altura"]):
                altura_M=float(heroe["altura"])
                nombre_M=heroe["identidad"]
                    
        elif heroe["genero"]=="F" and flag_F == True:
            altura_F = float(heroe["altura"])
            flag_F = False    
        elif heroe["genero"]=="F":
            if altura_F<=float(heroe["altura"]):
                altura_F=float(heroe["altura"])
                nombre_F=heroe["identidad"]

    print("La identidad del heroe masculino mas alto es: {0}".format(nombre_M))
    print("La identidad de la heroina mas alta es: {0}\n".format(nombre_F))

def cantidad_heroes_por_color_de_ojos():
    lista_color= []
    for heroe in lista_heroes:
        lista_color.append(heroe["color_ojos"])
    lista_color=set(lista_color)
    for color in lista_color:
        cont_color = 0
        for heroe in lista_heroes:
            if heroe["color_ojos"]==color:
                cont_color+=1
        print("Cantidad de heroes: {0}, color: {1}".format(cont_color,color))       

def cantidad_heroes_por_color_de_pelo():
    lista_color= []
    for heroe in lista_heroes:
        lista_color.append(heroe["color_pelo"])
    lista_color=set(lista_color)
    for color in lista_color:
        cont_color = 0
        for heroe in lista_heroes:
            if heroe["color_pelo"]==color:
                if color == '':
                    color = "No tiene"
                cont_color+=1
        print("Cantidad de heroes: {0}, color: {1}".format(cont_color,color)) 

def cantidad_heroes_por_inteligencia():
    lista_inteligencia= []
    for heroe in lista_heroes:
        lista_inteligencia.append(heroe["inteligencia"])
    lista_inteligencia=set(lista_inteligencia)
    for inteligencia in lista_inteligencia:
        cont_inteligencia = 0
        for heroe in lista_heroes:
            if heroe["inteligencia"]==inteligencia:
                if inteligencia == '':
                    inteligencia = "No tiene"
                cont_inteligencia+=1
        print("Cantidad de heroes: {0}, Inteligencia: {1}".format(cont_inteligencia,inteligencia)) 

def heroes_agrupados_por_color_ojos():
    lista_color= []
    for heroe in lista_heroes:
        lista_color.append(heroe["color_ojos"])
    lista_color=set(lista_color)
    for color in lista_color:
        for heroe in lista_heroes:
            if heroe["color_ojos"]==color:
                print("Nombre: {0}, color: {1}".format(heroe["nombre"],color))    

def heroes_agrupados_por_color_pelo():
    lista_color= []
    for heroe in lista_heroes:
        lista_color.append(heroe["color_pelo"])
    lista_color=set(lista_color)
    for color in lista_color:
        for heroe in lista_heroes:
            if heroe["color_pelo"]==color:
                if color == '':
                    color = "No tiene"
                print("Nombre: {0}, color: {1}".format(heroe["nombre"],color))  

def heroes_agrupados_por_inteligencia():
    lista_inteligencia= []
    for heroe in lista_heroes:
        lista_inteligencia.append(heroe["inteligencia"])
    lista_inteligencia=set(lista_inteligencia)
    for inteligencia in lista_inteligencia:
        for heroe in lista_heroes:
            if heroe["inteligencia"]==inteligencia:
                if inteligencia == '':
                    inteligencia = "No tiene"
                print("Nombre: {0}, inteligencia: {1}".format(heroe["nombre"],inteligencia))  
while True:
  
  respuesta = input("\n-A)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M\n-B)Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F\n-C)Recorrer la lista y determinar cuál es el superhéroe más alto de género M \n-D)Recorrer la lista y determinar cuál es el superhéroe más alto de género F \n-E)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M \n-F)Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F \n-G)Recorrer la lista y determinar la altura promedio de los  superhéroes de género M \n-H)Recorrer la lista y determinar la altura promedio de los  superhéroes de género F \n-I)Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a G) \n-J)Determinar cuántos superhéroes tienen cada tipo de color de ojos. \n-K)Determinar cuántos superhéroes tienen cada tipo de color de pelo. \n-L)Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). \n-M)Listar todos los superhéroes agrupados por color de ojos. \n-N)Listar todos los superhéroes agrupados por color de pelo. \n-O)Listar todos los superhéroes agrupados por tipo de inteligencia\n-Z)SALIR\n>")
  if respuesta == "A":
    nombres_heroes_masculinos()
  elif respuesta=="B":
    nombres_heroes_femeninos()
  elif respuesta=="C":
    heroe_masculino_mas_alto()
  elif respuesta=="D":
    heroe_femenino_mas_alto() 
  elif respuesta=="E":
    heroe_masculino_mas_bajo()
  elif respuesta=="F":
    heroe_femenina_mas_baja()
  elif respuesta=="G":
    altura_promedia_masculina()
  elif respuesta=="H":
    altura_promedia_femenina()
  elif respuesta=="I":
    identidades_heroes_mas_altos()
  elif respuesta=="J":
    cantidad_heroes_por_color_de_ojos()
  elif respuesta=="K":
    cantidad_heroes_por_color_de_pelo()  
  elif respuesta=="L":
    cantidad_heroes_por_inteligencia()
  elif respuesta=="M":
    heroes_agrupados_por_color_ojos()
  elif respuesta=="N":
    heroes_agrupados_por_color_pelo()
  elif respuesta=="O":
    heroes_agrupados_por_inteligencia()
  elif respuesta=="Z":
    break 
