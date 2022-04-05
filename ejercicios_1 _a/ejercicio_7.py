""" 7. Realizá un programa que permita ingresar el ancho y el largo de un terreno en metros 
y el valor del metro cuadrado de tierra. Debe mostrarse el valor total del 
terreno y la cantidad de metros de alambre para cercarlo completamente a tres alturas distintas.  """

ancho_terreno=float(input("ingrese el ancho del terreno en metros => "))
largo_terreno=float(input("ingrese el largo del terreno en metros => "))
valor_metro_cuadrado=float(input("ingrese el valor del metro cuadrado => $"))

area=ancho_terreno*largo_terreno
perimetro= 2*(ancho_terreno+largo_terreno)

# entindo por "a 3 alturas distintas" que irian 3 hilos de alabre a toda la vuelta
print(f"""El valor del terreno es: {area*valor_metro_cuadrado}
Va a necesitar {perimetro*3} Mts de alambre para cercar el terreno 

"""
)