import json 
import re

def cargar_json(path:str)->list:
    with open(path,"r") as file:
        buffer_dict = json.load(file)
    return buffer_dict["heroes"] 

def validar_numero(respuesta:str,patron:str)->int:
    if respuesta:
        if re.match(patron, respuesta):
            return(respuesta)
    return -1

def validar_lista(lista: list[dict], tamaño:int())->int:
    if lista:
        tamaño = int(tamaño)
        if tamaño>0 and tamaño < len(lista):
            print(f'tamaño correcto: {tamaño}')
            return tamaño
        print(f'Tamaño maximo superado, hay {len(lista)} heroes')
        return len(lista)   

def mostrar(lista:list, key:str):
    if lista:
        print('\n')
        for elemento in lista:
            mensaje = f'Nombre {elemento["nombre"]} | Identidad {elemento["identidad"]} | {key.capitalize()}:{elemento[key]}'
            print(mensaje)
        print('\n')

def buscar_minimo_maximo(lista:list, key:str, valor:str="maximo"):
    if lista and len(lista)>0:
        i_min=0
        i=0
        if valor=="maximo":
            for elemento in lista:
                if (int(elemento[key])>int(lista[i_min][key])):
                    i_min = i
                i+=1    
            return i_min        
        elif valor =="minimo":
            for elemento in lista:
                if (int(elemento[key])<int(lista[i_min][key])):
                    i_min = i
                i+=1    
            return i_min 

def ordenar_lista(lista:list, key:str, manera:str="asc")->list:
    if lista and len(lista)>0:
        lista_a_ordenar = lista.copy()
        lista_ordenada=[]
        if manera =="asc":
            while(len(lista_a_ordenar)>0):
                index_minimo = buscar_minimo_maximo(lista_a_ordenar, key, "minimo")
                elemento = lista_a_ordenar.pop(index_minimo)
                lista_ordenada.append(elemento)
        elif manera =="desc":
            while(len(lista_a_ordenar)>0):
                index_minimo = buscar_minimo_maximo(lista_a_ordenar, key, "maximo")
                elemento = lista_a_ordenar.pop(index_minimo)
                lista_ordenada.append(elemento)
        return lista_ordenada

lista_heroe = cargar_json("C:/Users/Lucas/Desktop/UTN/Programacion_I/PythonUTN/Ejercicios/SimulacroParcial/data_stark.json")
while(True):
        print('''
        1-Lista de los primeros N héroes. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)
        2-Ordenar videos por duracion (UP/DOWN)
        3-Ordenar videos por cantidad de views (UP/DOWN)
        4-Buscar videos por titulo
        5-Exportar lista de videos CVC
        6-Salir
        ''')
        respuesta = input()
        respuesta = int(validar_numero(respuesta, "^[1-7]{1}$"))
        if (respuesta==1):
            respuesta = input("Cantidad de heroes a mostrar: ")
            cantidad = int(validar_numero(respuesta, "^[1-9]{1,2}$"))
            cantidad = validar_lista(lista_heroe, cantidad)
            lista_para_archivo = lista_heroe[:cantidad].copy()
            mostrar(lista_para_archivo)
        if (respuesta==2):
            respuesta = input("Quiere ordenar de manera ascendiente o descenciante ? (asc, desc) \n")
            validar = re.search('asc|desc', respuesta, re.IGNORECASE)
            
            if validar == None:
                print("No ingreso ni asc o desc")      
            else:
                if respuesta =="asc":
                    lista_para_archivo = ordenar_lista(lista_heroe, "altura", "asc").copy()
                    mostrar(lista_para_archivo,"altura")
                elif respuesta =="desc":
                    lista_para_archivo = ordenar_lista(lista_heroe, "altura", "desc").copy()
                    mostrar(lista_para_archivo,"altura")        
        if (respuesta==3):
            respuesta = input("Quiere ordenar de manera ascendiente o descenciante ? (asc, desc) \n")
            validar = re.search('asc|desc', respuesta, re.IGNORECASE)
            if validar == None:
                print("No ingreso ni asc o desc")      
            else:
                if respuesta =="asc":
                    mostrar(ordenar_lista(lista_heroe, "fuerza", "asc"),"fuerza")
                elif respuesta =="desc":
                    mostrar(ordenar_lista(lista_heroe, "fuerza", "desc"),"fuerza")        
        if (respuesta==4):
            print("Buscar videos por titulo")
        if (respuesta==5):
            print("Exportar lista de videos CVC")    
        if (respuesta==6):
            print("Salir")
            break 
