#Python
#Hecho por Angela QUintana
#Fecha:14 marzo 2017


try:
    contador=0
    numero= raw_input ('Introduzca un numero: ')
    contador= contador + 1
    for valor in [numero]:
        if numero== 'fin':
            print sum(numero), contador, sum(numero)/contador
            break

except:
    print 'ERROR'
