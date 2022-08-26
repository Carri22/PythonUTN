# Ejercicio Integrador 01

# La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
# 1 El tipo (validar "barbijo", "jabón" o "alcohol")
# 2 El precio: (validar entre 100 y 300)
# 3 La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
# 4 La marca y el Fabricante.

# Se debe informar lo siguiente:
# A Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B Del ítem con más unidades, el fabricante.
# Cuántas unidades de jabones hay en total.

tipo_producto = ''
precio = 0
cantidad = 0
marca = ''
fabricante = ''
precio_barbijo_caro = -1

for i in range(5):

    tipo_producto = input("ingrese tipo de producto (jabon, barbijo, alcohol")
    while(tipo_producto != "barbijo" and tipo_producto == "jabon" and tipo_producto == "alcohol"):
        tipo_producto = input(
            "Error: vuelva a ingresar el tipo de producto correcto")

    while(True):
        precio = int(input("ingrese precio"))
        if precio >= 100 and precio <= 300:
            break

    if tipo_producto == "barbijo":
        if precio > precio_barbijo_caro:
            precio_barbijo_caro = precio
            cantidad_barbijo_caro = cantidad
            fabricante_barbijo_caro = fabricante
