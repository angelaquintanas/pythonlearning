#Python
#Hecho por Angela QUintana
#Fecha:14 marzo 2017

def calculo_salario (horas, tarifa):
    salario= float(horas) * float(tarifa)
    return salario


horas= raw_input('Introduzca Horas: ')
tarifa= raw_input('Introduzca Tarifa: ')
print str('Salario: ') + str(calculo_salario (horas, tarifa))
