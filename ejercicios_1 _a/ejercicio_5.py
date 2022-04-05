"""5. Realizá un programa que permita ingresar valores del mismo tipo
para las variables num1 y num2. Una vez cargadas, mostrar ambas variables por pantalla,
ntercambiá sus valores (que lo cargado en num1 quede en num2,
y viceversa) y volvé a mostrarlas actualizadas. [EC] """

num1 = int(input("ingrese un numero => "))
num2 = int(input("ingrese otro numero => "))

print(f"Los numeros ingrsados son {num1} y {num2} ")
print("Los cambiamos de lugar")
contenedor = num1
num1 = num2
num2 = contenedor
print(f"Ahora los numeros son {num1} y {num2}")