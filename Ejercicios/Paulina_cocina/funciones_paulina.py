'''
cargar un json a una lista o variable dependa que tenga el json (en este caso una lista)
path(ruta del json)
'''

import json #necesito un archivo json que no tengo
def cargar_json(path:str)->list:
    with open(path,"r") as file:
        buffer_dict = json.load(file)
    return buffer_dict["paulina"] 

def mostrar(lista:list):
    for elemento in lista:
        print(elemento)

def buscar_minimo(lista:list,key:str):
    '''
    busca un minimo en una lista de elementos dict con clave "key"
    recibe una lista con elementos dict con clave "key"
    retorna el indice del elemento minimo o -1 en caso de error 
    '''
    i_min=-1
    if(len(lista)>0):
        i_min = 0
        for i in range(len(lista)):
            if (lista[i]["key"]<lista[i_min]["key"]):
                i_min = i
    return i_min

def ordenar_lista(lista:list):
    lista_a_ordenar = lista.copy()
    lista_ordenada = []
    while(len(lista_a_ordenar>0)):
        index_minimo = buscar_minimo(lista_a_ordenar, "views")
        elemento = lista_a_ordenar.por(index_minimo)
        lista_ordenada.append(elemento)
    return lista_ordenada
    