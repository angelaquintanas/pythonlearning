#Python
#Hecho por Angela QUintana
#Fecha:14 marzo 2017

numero= None
contador= 0
suma= 0
media= 0

while numero!= 'fin':
    numero= raw_input ('Introduzca un numero: ')
    try:
        contador= contador + 1
        suma= suma + int(numero)
    except ValueError:
	if numero != 'fin':
	    print "Entrada invalida"

media= suma/contador
print suma, contador, media

