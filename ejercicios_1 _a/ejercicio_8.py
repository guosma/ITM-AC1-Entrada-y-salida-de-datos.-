""" 8. Realizá un programa que permita ingresar dos números naturales.
Debes mostrar los resultados para las 4 operaciones matemáticas básicas con los números ingresados. 
[EC] """

numero_1=int(input("ingrese un numer => "))
numero_2=int(input("ingrese otro numer => "))

print(
    f"""Los numeros ingresados son : {numero_1} y {numero_2}
    La multiplicacion de estos numeros da : {numero_1*numero_2}
    La Divivion de los mismos es: {numero_1/numero_2} y {numero_2/numero_1}
    La suma es: {numero_1+numero_2}
    Y la resta de los mismos es: {numero_1-numero_2} y {numero_2-numero_1}
     """
)