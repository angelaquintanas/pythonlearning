#PYTHON
#Hecho por: Angela Quintana
#Fecha: 7 marzo 2017



def calcula_puntuacion (puntuacion):	
	if (puntuacion <= 1.0 and puntuacion >= 0.0):
		if (puntuacion >= 0.9): 
			print "Sobresaliente"
		if (puntuacion < 0.9 and puntuacion >= 0.8):
                        print "Notable"
		if (puntuacion < 0.8 and puntuacion >= 0.7):
                        print "Bien"
		if (puntuacion < 0.7 and puntuacion >= 0.6):
                        print "Suficiente"
		if (puntuacion < 0.6):
                        print "Insuficiente"
	else:
		print "Esa puntuacion no es valida. Debe estar entre 0.0 y 1.0. "
        return puntuacion

try:
        puntuacion_raw = raw_input("Por favor ingrese la puntuacion: ")
        puntuacion = float(puntuacion_raw)
	calcula_puntuacion (puntuacion)

except:
	print "Error. Por favor ingrese un valor numerico. Gracias."

