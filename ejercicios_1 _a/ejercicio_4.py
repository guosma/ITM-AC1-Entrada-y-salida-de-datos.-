"""4. Realizá un programa que permita ingresar el valor monetario de 
una hora de trabajo y la cantidad de horas trabajadas por día por un trabajador.
Debes mostrar el valor del salario semanal, sabiendo que trabaja todos los días
 hábiles y la mitad de las horas del día hábil los sábados. (Todas las horas valen lo mismo.)"""

valor_hora = int(input("Ingrese el valor monetario de una hora de trabajo => "))
jornada_lavoral = int(input("Ingrese la cantidad de horas de 1 jornada laboral => "))
salario = (jornada_lavoral*valor_hora*5)+((jornada_lavoral/2)*valor_hora)
print(f"El valor del salario semanal para {jornada_lavoral} hs diarias es : ${salario}")