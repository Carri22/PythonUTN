# Ejercicio Integrador 02

# La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para la cocina de Industrias Wayne.
# Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
# preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
# 1) PESO: (entre 10 y 100 kilos)
# 2) PRECIO POR KILO: (mayor a 0 [cero]).
# 3) TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
# Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto. o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
# A) El importe total a pagar, BRUTO sin descuento.
# B) El importe total a pagar con descuento (Solo si corresponde).
# C) Informar el tipo de alimento más caro.
# D) El promedio de precio por kilo en total.

respuesta = "si"
peso = 0
presio_kilo = 0
tipo = ''
importe_total = 0
importe_descuento = 0
peso_total = 0
importe_todal_vuelta = 0
alimento_caro = 0
tipo_caro = ''
promedio = 0
mensaje = 'No le corresponte importe a pagar con descuento'

while(respuesta == "si"):

    peso = int(input("ingrese el peso "))
    if peso >= 10 and peso <= 100:
        break

    presio_kilo = int(input("ingrese el precio por kilo "))
    if presio_kilo >0:
        break

    tipo = input("ingrese tipo de alimento (v, a, m),(vegetal, animal, mezcla) ")
    while(tipo != "v" and tipo != "a" and tipo != "m"):
        tipo = input(
            "Error: vuelva a ingresar el tipo de alimento correcto ")

    importe_todal_vuelta = peso * presio_kilo
    importe_total += importe_todal_vuelta 
    peso_total += peso

    if  alimento_caro < importe_todal_vuelta:
        alimento_caro = importe_todal_vuelta
        tipo_caro = tipo

    respuesta = ("quiere continuar con la operacion? (si, no)")
    while(respuesta != "si" and respuesta != "no"):
        respuesta = input(
            "Error: vuelva a ingresar su respusta, quiere continuar con la operacion? (si, no) ")

if peso_total > 100:
    if peso_total > 300:
        importe_descuento = importe_total * 0.75
        mensaje = "El importe a pagar con despuesto es de: ", importe_descuento
    else:
        importe_descuento = importe_total * 0.85
        mensaje = "El importe a pagar con despuesto es de: ", importe_descuento

promedio = importe_total/peso_total

print("El importe total a pagar, BRUTO sin descuento es: ", importe_total ,)
print(mensaje)
print("El alimento mas caro es: ",tipo_caro)
print("El precio promedio por kilo es: ",promedio)


                           