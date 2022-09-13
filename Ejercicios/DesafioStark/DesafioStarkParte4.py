#Desafío #04
'''
IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista, un string, etc y que contendrá) y que es lo que retorna la función!

1.1)
Crear la función ‘extraer_iniciales’ que recibirá como parámetro: 
*nombre_heroe: un string con el nombre del personaje
La función deberá devolver a partir del parámetro recibido un nuevo string con las iniciales del nombre del personaje seguidos por un punto (.)
*En el caso que el nombre del personaje contenga el artículo ‘the’ se deberá omitir de las iniciales
*Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso que lo tenga se deberá reemplazar por un espacio en blanco
La función deberá validar:
*Que el string recibido no se encuentre vacío
Devolver ‘N/A’ en caso de no cumplirse la validación
Ejemplo de la salida de la función para Howard the Duck:
H.D.

1.2)Crear la función ‘definir_iniciales_nombre’ la cual recibirá como parámetro:
heroe: un diccionario con los datos del personaje
La función deberá agregar una nueva clave al diccionario recibido como parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de llamar a la función ‘extraer_iniciales’
La función deberá validar:
Que el dato recibido sea del tipo diccionario
Que el  diccionario contengan la clave ‘nombre’  
En caso de encontrar algún error retornar False, caso contrario retornar True

1.3)
Crear la función ‘agregar_iniciales_nombre’ la cual recibirá como parámetro:
lista_heroes: lista de personajes
Se deberá validar:
Que lista_heroes sea del tipo lista
Que la lista contenga al menos un elemento
La función deberá iterar la lista_heroes pasándole cada héroe a la función definir_iniciales_nombre.
En caso que la función definir_iniciales_nombre() retorne False entonces se deberá detener la iteración e informar por pantalla el siguiente mensaje:
 ‘El origen de datos no contiene el formato correcto’ 
La función deberá devolver True en caso de haber finalizado con éxito o False en caso de que haya ocurrido un error

1.4)
Crear la función ‘stark_imprimir_nombres_con_iniciales’  la cual recibirá como parámetro:
lista_heroes: la lista de personajes
La función deberá utilizar la función agregar_iniciales_nombre’ para añadirle las iniciales a los diccionarios contenidos en la lista_heroes
Luego deberá imprimir la lista completa de los nombres de los personajes seguido de las iniciales encerradas entre paréntesis () 
Se deberá validar:
Que lista_heroes sea del tipo lista
Que la lista contenga al menos un elemento
Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de viñeta) seguido de un espacio.
Ejemplo de salida:
* Howard the Duck (H.D.)
* Rocket Raccoon (R.R.)
…
La función no retorna nada

2.1)
Crear la función ‘generar_codigo_heroe’ la cual recibirá como parámetros:
id_heroe: un entero que representa el identificador del héroe
genero_heroe: un string que representa el género del héroe ( puede tomar los valores ‘M’,  ‘F’ o ‘NB’)
La función deberá generar un string con el siguiente formato:
GENERO-000…000ID
Es decir, el género recibido por parámetro seguido de un ‘-’ (guión) y por último el identificador recibido.  Todos los códigos generados deben tener como máximo 10 caracteres (contando todos los caracteres, inclusive el guión). Se deberá completar con ceros para que todos queden del mismo largo
Algunos ejemplos:
F-00000001
M-00000002
NB-0000010
La función deberá validar:
El identificador del héroe sea numérico. 
El género no se encuentre vacío y este dentro de los valores esperados (‘M’,  ‘F’ o ‘NB’)
En caso de no pasar las validaciones retornar ‘N/A’. En caso de verificarse correctamente retornar el código generado

2.3)
Crear la función ‘stark_generar_codigos_heroes’  la cual recibirá como parámetro:
lista_heroes: la lista de personajes
La función deberá iterar la lista de personajes y agregarle el código a cada uno de los personajes.
El código del héroe (id_heore) surge de la posición del mismo dentro de la lista_heroes (comenzando por el 1).
Reutilizar la función agregar_codigo_heroe pasándole como argumentos el héroe que se está iterando y el id_heroe
Una vez finalizado imprimir por pantalla un mensaje como el siguiente:
(## representa la cantidad de códigos generados):
Se asignaron ## códigos 
*   El código del primer héroe es: 		M-00000001
* El código del del último héroe es: 	M-00001224
La función deberá validar::
La lista contenga al menos un elemento
Todos los elementos de la lista sean del tipo diccionario
Todos los elementos contengan la clave ‘genero’
En caso de encontrar algún error, informar por pantalla: ‘El origen de datos no contiene el formato correcto’
La función no retorna ningún valor.

3.1)
Crear la función ‘sanitizar_entero’ la cual recibirá como parámetro:
numero_str: un string que representa un posible número entero
La función deberá analizar el string recibido y determinar si es un número entero positivo.  La función debe devolver distintos valores según el problema encontrado:
Si contiene carácteres no numéricos retornar -1
Si el número es negativo se deberá retornar un -2
Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3
También deberá quitar los espacios en blanco de atras y adelante del string en caso que los tuviese
En caso que se verifique que el texto contenido en el string es un número entero positivo, retornarlo convertido en entero

3.2)
Crear la función ‘sanitizar_flotante’ la cual recibirá como parámetro:
numero_str: un string que representa un posible número decimal
La función deberá analizar el string recibido y determinar si es un número flotante positivo.  La función debe devolver distintos valores según el problema encontrado:
Si contiene carácteres no numéricos retornar -1
Si el número es negativo se deberá retornar un -2
Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3
También deberá quitar los espacios en blanco de atras y adelante del string en caso que los tuviese
En caso que se verifique que el texto contenido en el string es un número flotante positivo, retornarlo convertido en flotante

3.3)
Crear la función ‘sanitizar_string’’ la cual recibirá como parámetro
valor_str: un string que representa el texto a validar
valor_por_defecto: un string que representa un valor por defecto (parámetro opcional, inicializarlo con ‘-’)
La función deberá analizar el string recibido y determinar si es solo texto (sin números). En caso de encontrarse números retornar “N/A”
En el caso que valor_str contenga una barra ‘/’ deberá ser reemplazada por un espacio
El espacio es un caracter válido 
En caso que se verifique que el parámetro recibido es solo texto, se deberá retornar el mismo convertido todo a minúsculas
En el caso que el texto a validar se encuentre vacío y que nos hayan pasado un valor por defecto, entonces retornar el valor por defecto convertido a minúsculas
Quitar los espacios en blanco de atras y adelante de ambos parámetros en caso que los tuviese

3.4)
Crear la función ‘sanitizar_dato’ la cual recibirá como parámetros:
heroe: un diccionario con los datos del personaje
clave: un string que representa el dato a sanitizar (la clave del diccionario). Por ejemplo altura
tipo_dato: un string que representa el tipo de dato a sanitizar. Puede tomar los valores: ‘string’, ‘entero’ y ‘flotante’
La función deberá sanitizar el valor del diccionario correspondiente a la clave y al tipo de dato recibido
Para sanitizar los valores se deberán utilizar las funciones creadas en los puntos 2.1, 2.2, 2.3 y 2.4

Se deberá validar:
Que tipo_dato se encuentre entre los valores esperados (‘string, ‘entero, ‘flotante)’ la validación debe soportar que nos lleguen mayúsculas o minúsculas. En caso de encontrarse un valor no válido informar por pantalla: ‘Tipo de dato no reconocido’

Que clave exista como clave dentro del diccionario heroe. En caso de no encontrarse, informar	 por pantalla: ‘La clave especificada no existe en el héroe’. (en este caso la validación es sensible a mayúsculas o minúsculas) 
Ejemplo de llamada a la función válida:
sanitizar_dato(dict_personaje, “altura”, “Flotante”)
La función deberá devolver True en caso de haber sanitizado algún dato y False en caso contrario.

3.5)
Crear la función 'stark_normalizar_datos’ la cual recibirá como parámetros:
lista_heroes: la listas personajes
La función deberá recorrer la lista de héroes y sanitizar los valores solo de las siguientes claves: ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e ‘inteligencia’
Un vez finalizado el proceso mostrar el mensaje ‘Datos normalizados’, 
Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
La función no retorna nada
Reutilizar la función sanitizar_dato

4.1)
Crear la función ‘generar_indice_nombres’ la cual recibirá como parámetro:
lista_heroes: la lista de personajes
La función deberá iterar la lista de personajes y generar una lista donde cada elemento es cada palabra que componen el nombre de los personajes.
Por ejemplo la lista que se deberá retornar tiene la siguiente forma:
[‘Howard’,  ‘the’, ‘Duck’, ‘Rocket’, ‘Raccoon’, ‘Wolverine’, … ]

4.2)
Crear la función ‘stark_imprimir_indice_nombre’ la cual recibirá como parámetro:
lista_heroes: la lista de personajes

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
def extraer_iniciales(nombre_heroe:str):
    '''
    1.1)
    Crear la función ‘extraer_iniciales’ que recibirá como parámetro: 
    *nombre_heroe: un string con el nombre del personaje
    La función deberá devolver a partir del parámetro recibido un nuevo string con las iniciales del nombre del personaje seguidos por un punto (.)
    *En el caso que el nombre del personaje contenga el artículo ‘the’ se deberá omitir de las iniciales
    *Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso que lo tenga se deberá reemplazar por un espacio en blanco
    La función deberá validar:
    *Que el string recibido no se encuentre vacío
    Devolver ‘N/A’ en caso de no cumplirse la validación
    Ejemplo de la salida de la función para Howard the Duck:
    H.D.
    '''
    mensaje=""
    punto="."

    if not nombre_heroe:
        mensaje = "N/A"
    else:
        nombre_2=nombre_heroe.replace("-", " ")
        # nombre_2=nombre_2.replace("the", " ")
        nombre=nombre_2.split(" ")
        for i in nombre:
            if i == "the":
                nombre.remove(i)     
        punto=punto.join(nombre)
        punto=punto.upper()
        index=punto.index(".")
        inicial1=punto[0:1]
        inicial2=punto[index:index+2]
        mensaje=inicial1+inicial2

    return mensaje

print(extraer_iniciales("el the duck"))