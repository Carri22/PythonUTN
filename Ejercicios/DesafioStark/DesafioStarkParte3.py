from data_stark import lista_heroes
'''
CONSIGNA
    Desafío #02: (con biblioteca propia: stark_biblioteca)
    En base a lo resuelto en el desafío #00, deberás mejorar la calidad de tus funciones. Es por ello que te proponemos lo siguiente:
    IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista, un string, etc y que contendrá) y que es lo que retorna la función!
    Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista de héroes. La función deberá:
    Recorrer la lista y convertir al tipo de dato correcto las keys (solo con las keys que representan datos numéricos)
    Validar primero que el tipo de dato no sea del tipo al cual será casteado. Por ejemplo si una key debería ser entero (ejemplo edad) verificar antes que no se encuentre ya en ese tipo de dato.
    Si al menos un dato fue modificado, la función deberá imprimir como mensaje ‘Datos normalizados’, caso contrario no imprimirá nada.
    Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”

    Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el cual representara a un héroe y devolverá un string el cual contenga su nombre formateado de la siguiente manera: 
    Nombre: Howard the Duck

    Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y deberá imprimirlo en la consola. La función no tendrá retorno.

    Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por parámetro la lista de héroes y deberá imprimirla en la consola. Reutilizar las funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
    Con este se resuelve el Ej 1 del desafío #00

    Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario el cual representara a un héroe y una key (string) la cual representará el dato que se desea obtener. 
    La función deberá devolver un string el cual contenga el nombre y dato (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.

    El string resultante debe estar formateado de la siguiente manera: (suponiendo que la key es fuerza)
    Nombre: Venom | fuerza: 500

    Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por parámetro la lista de héroes, la cual deberá iterar e imprimir su nombre y altura USANDO la función creada en el punto 2. Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
    Con este se resuelve el Ej 2 del desafío #00

    Crear la función 'calcular_max' la cual recibirá por parámetro la lista de héroes y una key (string) la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe que tenga el dato más alto.
    Ejemplo de llamada:
        calcular_max(lista, 'edad')

    Crear la función 'calcular_min' la cual recibirá por parámetro la lista de héroes y una key (string) la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el mínimo de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe que tenga el dato más bajo. 
    Ejemplo de llamada:
        calcular_min(lista, 'edad')

    Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:
    La lista de héroes
    El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
    Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
    La función deberá retornar el héroe que cumpla con la condición pedida. Reutilizar las funciones hechas en los puntos 4.1 y 4.2
    Ejemplo de llamada:
    calcular_max_min_dato(lista, "maximo", "edad")

    Crear la función 'stark_calcular_imprimir_heroe' la cual recibirá tres parámetros: 
    La lista de héroes
    El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
    Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
    Con este se resuelve el Ej 3, Ej 4, Ej 6 y Ej 7 del desafío #00
    La función deberá obtener el héroe que cumpla dichas condiciones, imprimir su nombre y el valor calculado. Reutilizar las funciones de los puntos:
    punto 1.2, punto: 2, punto 4.1, punto 4.2 y punto 4.3 
    Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
    Ejemplo de llamada:
        stark_calcular_imprimir_heroe (lista, "maximo", "edad")
                Ejemplo de salida:
        Mayor altura: Nombre: Howard the Duck | altura: 79.34

    Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de héroes y un string que representara el dato/key de los héroes que se requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes de hacer la suma. La función deberá retorna la suma de todos los datos según la key pasada por parámetro

    Crear la función  ‘dividir’ la cual recibirá como parámetro dos números (dividendo y divisor). Se debe verificar si el divisor es 0,  en caso de serlo, retornar 0, caso contrario realizar la división entre los parámetros y retornar el resultado

    Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de héroes y un string que representa el dato del héroe que se requiere calcular el promedio. La función debe retornar el promedio del dato pasado por parámetro

    IMPORTANTE: hacer uso de las las funciones creadas en los puntos 5.1 y 5.2

    Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá una lista de héroes y utilizando la función del punto 5.3 calcula y mostrará la altura promedio. Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
    IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y 5.3
    Con este se resuelve el Ej 5 del desafío #00
    Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla, el cual permite utilizar toda la funcionalidad ya programada. Se deberá reutilizar la función antes creada encargada de imprimir un string (1.2)
    Crear la función “validar_entero” la cual recibirá por parámetro un string de número el cual deberá verificar que sea sea un string conformado únicamente por dígitos. Retornara True en caso de serlo, False caso contrario

    Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú de opciones y le pedirá al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las funciones del ejercicio 6.1 y 6.2

    Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes y se encargará de la ejecución principal de nuestro programa. 
    Utilizar if/elif o match según prefiera (match solo para los que cuentan con python 3.10+). Debe informar por consola en caso de seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.

'''
lista_vacia=[]

def stark_normalizar_datos(lista:list):
  '''
  convertir al tipo de dato correcto las keys de una lista (solo con las keys que representan datos numéricos)

  recive una lista en la cual tratara de convertir los datos de las keys necesarias 

  retorna un mensaje que comunica que se normalizo por lo menos un dato de la lista o un mensaje que comunica que no se ingrso una lista o que esta esta vacia

  '''
  flag=False
  if type(lista)==type([]) and len(lista)>0:
    for heroe in lista:
      if type(heroe["altura"])==type(""):
        heroe["altura"]=float(heroe["altura"])
        flag=True
      if type(heroe["peso"])==type(""): 
        heroe["peso"]=float(heroe["peso"])
        flag=True
      if type(heroe["fuerza"])==type(""): 
        heroe["fuerza"]=float(heroe["fuerza"])
        flag=True
    if flag==True:
      mensaje="Datos normalizados"
  else:
    mensaje="Error: no se ingreso una lista o esta lista de heroe esta vacia "
  return mensaje

def obtener_nombre(heroe:dict):
  '''
  obtiene el nombre del heroe

  recive un diccionario con los datos del heroe

  retorna un mensaje, este mensaje puede devolver :el nombre del heroe/que no exista la key con el nombre "heroe"/
                                                   que no se ingreso un diccionario o que el que ingreso esta vacio
  '''
  if type(heroe)==type({}) and heroe:
    if heroe["nombre"]:
      nombre = "Nombre: {0}".format(heroe["nombre"])
    else:
      nombre = "No existe la key nombre en el diccionario del heroe"  
  else:
    nombre = "No ingreso un diccionario o el diccionario ingresado esta vacio"
  return nombre  

def imprimir_dato(texto:str):
  '''
  imprime por consola un texto

  recive un parametro de tipo string

  No tiene retorno, imprime directamente en consola el el texto dentro del string ingresado o 
  un mensaje comunicando que el parametro ingresado no es de tipo string
  '''
  if type(texto) == str:
    print(texto)
  else:
    print("no ingreso un parametro de tipo strig")  

def stark_imprimir_nombres_heroes(lista:list):
    if type(lista)==type([]): 
        for heroe in lista:
            imprimir_dato(obtener_nombre(heroe))


def obtener_nombre_y_dato(heroe:dict, key:str):
    if type(heroe)==type({}) and heroe:
        nombre = obtener_nombre(heroe)
        if heroe[key]:
            nombre = "{0} | {1}:{2}".format(nombre,key,heroe[key])
        else:
            nombre = "No existe la key ingresada en el diccionario del heroe"  
    else:
        nombre = "No ingreso un diccionario o el diccionario ingresado esta vacio"
      
    return imprimir_dato(nombre)   

def stark_imprimir_nombres_alturas(heroe:dict):
    obtener_nombre_y_dato(heroe, "altura")   
    return obtener_nombre_y_dato  

def calcular_max(lista:list, key:str):
  stark_normalizar_datos(lista)
  flag = True
  for heroe in lista:
    for dato in heroe:
      if type(dato)==type(key) and dato==key:
        if flag == True:
          maximo = heroe[dato]
          nombre=heroe["nombre"]
          flag = False
        elif maximo<=heroe[dato]:
          maximo=heroe[dato]
          nombre=heroe["nombre"]
  return nombre

while True:
  
  respuesta = input("\n-2)nombre de cada superhéro\n-3)nombre de cada superhéroe junto a la altura del mismo\n-4)superhéroe más alto (MÁXIMO)\n-5)superhéroe más bajo (MÍNIMO)\n-6)altura promedio de los  superhéroes (PROMEDIO)\n-7)Nombre (Identidad) del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)\n-8)superhéroe más y menos pesado.\n-9)SALIR\n\n>")
  if respuesta == "2":
    stark_imprimir_nombres_heroes(lista_heroes)
  elif respuesta=="3":
    stark_imprimir_nombres_alturas(lista_heroes[0])
  elif respuesta=="4":
    print(calcular_max(lista_heroes,"altura"))
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
