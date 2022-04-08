""" 9. Realizá un programa que permita ingresar dos números que representan las medidas
en grados de dos ángulos interiores de cierto triángulo. A partir de los valoresde estos dos
ángulos el programa debe mostrar el valor en grados del ángulo restante.
Recordá que la suma de los ángulos interiores de todo triángulo es de 180º.  """


angulo_valido = False

while angulo_valido != True:
    print("Recuerde que la suma de los angulos de los triangulos no puede ser mayor de 180")
    print("*********")
    angulo_1_triangulo=int(input("Ingrese la medida del primer angulo => "))
    angulo_2_triangulo=int(input("Ingrese la medida del segundo angulo => "))
    suma_angulos = angulo_1_triangulo + angulo_2_triangulo
    if suma_angulos<180:
        print(f"El angulo restante para armar un riangulo es de {180-suma_angulos}° Grados ")
        angulo_valido = True
    else:
        print("Los angulos Ingresados son incorrectos")