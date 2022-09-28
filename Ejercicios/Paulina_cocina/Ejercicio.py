'''
1-Lista TOP numeros videos
2-Ordenar videos por duracion (UP/DOWN)
3-Ordenar videos por cantidad de views (UP/DOWN)
4-Buscar videos por titulo
5-Exportar lista de videos CVC
6-Salir
'''
#from DesafioStark import data_stark
import funciones_paulina
def paulina_app():
    lista_videos = funciones_pualina.cargar_json(path)
    while(True):
        print('''
        1-Lista TOP numeros videos
        2-Ordenar videos por duracion (UP/DOWN)
        3-Ordenar videos por cantidad de views (UP/DOWN)
        4-Buscar videos por titulo
        5-Exportar lista de videos CVC
        6-Salir
        ''')
        respuesta = input()
        if (respuesta=="1"):
            #Valida que el input es un int, la siguiente linea no lo esta haciendo, es algo que tenes que hacer Lucas
            top = int(input("cuantos?"))
            funciones_pualina.mostrar(lista_videos[:top])
        if (respuesta=="2"):
            print("Ordenar videos por duracion (UP/DOWN)")    
        if (respuesta=="3"):
            print("Ordenar videos por cantidad de views (UP/DOWN)")    
        if (respuesta=="4"):
            print("Buscar videos por titulo")
        if (respuesta=="5"):
            print("Exportar lista de videos CVC")    
        if (respuesta=="6"):
            print("Salir")
            break1

    