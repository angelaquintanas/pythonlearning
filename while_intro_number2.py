#Python
#Hecho por Angela QUintana
#Fecha:14 marzo 2017

numero= None
contador= 0
suma= 0
media= 0

while True:
    numero= raw_input ('Introduzca un numero: ')
    if numero == "fin": break
    try:
        contador= contador + 1
        suma= suma + int(numero)
    except ValueError:
	print "Entrada invalida"

media= suma/contador
print suma, contador, media

