""" 6. Realizá un programa que permita ingresar el monto total de las ventas 
realizadas por un vendedor durante el mes, de quien se sabe que gana un 
sueldo fijo de 44000 pesos más el 16 por ciento del monto total vendido.
 Con tales datos debes calcular y mostrar el importe a cobrar por el vendedor."""

monto_ventas=float(input("ingrese el monto total de la venta mensual => $"))

comision=(monto_ventas*16)/100
print(f"El importe a cobrar por el vendedor es: ${44000+comision} ")
