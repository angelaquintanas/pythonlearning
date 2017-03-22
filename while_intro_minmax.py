#Python
#Hecho por Angela QUintana
#Fecha:22 marzo 2017

numero= None
contador= 0
suma= 0
minimo= None
maximo= None

while numero!= 'fin':
    numero= raw_input ('Introduzca un numero: ')
    try:
        contador= contador + 1
        suma= suma + int(numero)
	if minimo == None or numero < minimo:
		minimo= numero
	if maximo==None or numero > maximo:
		maximo= numero
    except ValueError:
	if numero != 'fin':
	    print "Entrada invalida"

print "Suma: ",suma, "Contador: ",contador, "Minimo: ", minimo, "Maximo: ",maximo
