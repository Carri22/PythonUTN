# CARRIZO LUCAS 1H

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
flag = True
item_mas_unidades = 0
item_fabricante = ''
cont_jabon = 0

for i in range(3):

    tipo_producto = input("ingrese tipo de producto (jabon, barbijo, alcohol) ")
    while(tipo_producto != "barbijo" and tipo_producto != "jabon" and tipo_producto != "alcohol"):
        tipo_producto = input(
            "Error: vuelva a ingresar el tipo de producto correcto ")

    while(True):
        precio = int(input("ingrese precio "))
        if precio >= 100 and precio <= 300:
            break

    while(True):
        cantidad=int(input("ingrese la cantidad "))
        if cantidad > 0 and cantidad < 1001:
            break

    marca = input("ingrese marca ")
    fabricante = input("ingrese el fabricante ")    

    if tipo_producto == "barbijo":
        if precio > precio_barbijo_caro:
            precio_barbijo_caro = precio
            cantidad_barbijo_caro = cantidad
            fabricante_barbijo_caro = fabricante

    if item_mas_unidades < cantidad:
        item_mas_unidades = cantidad
        item_fabricante = fabricante

    if tipo_producto == "jabon":
        cont_jabon+=1

print("La cantidad del barbijo mas caro es: ", cantidad_barbijo_caro ," y el fabricante es: " ,fabricante_barbijo_caro)
print("Del ítem con más unidades, el fabricante es: ", item_fabricante)
print("Hay ", cont_jabon ," jabones en total")