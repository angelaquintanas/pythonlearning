#Python
#Hecho por: Angela Quintana
#Fecha: 7 marzo 2017

horas=raw_input("Introduzca las horas: ")
tarifa=raw_input("Introduzca la tarifa: ")

try:
	if horas>40:
		salario= (40 * float(tarifa)) + ((1.5) * (float(horas)-40) * float(tarifa))
	else:
		salario= float(horas) * float(tarifa)
	
	print "Salario: " + str(salario)

except:
	print "ERROR. Por favor escribir un valor numerico. Gracias."


