""" 10.Realizá un programa que permita resolver el siguiente problema: 
Tres personas aportan diferente capital a una sociedad y desean saber
 el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje). 
 Solicitar la carga por teclado del nombre de cada socio, su capital aportado y 
 a partir de esto calcular e informar lo requerido previamente.
 """

nombre_socio_1 = input("ingrese el nombre del primer socio ")
aporte_socio_1 = int(input("ingrese el monto aportado por el prmer socio => "))

nombre_socio_2 = input("ingrese el nombre del primer socio ")
aporte_socio_2 = int(input("ingrese el monto aportado por el prmer socio => "))

nombre_socio_3 = input("ingrese el nombre del primer socio ")
aporte_socio_3 = int(input("ingrese el monto aportado por el prmer socio => "))

capital_total = aporte_socio_1 + aporte_socio_2 + aporte_socio_3
porcentage_socio_1 = (aporte_socio_1 * 100)/capital_total
porcentage_socio_2 = (aporte_socio_2 * 100)/capital_total
porcentage_socio_3 = (aporte_socio_3 * 100)/capital_total