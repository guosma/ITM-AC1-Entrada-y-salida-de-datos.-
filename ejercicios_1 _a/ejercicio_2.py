"""2. Realizá un programa que permita ingresar 3 notas pertenecientes a tres
 trimestres distintos para cierto alumno de nivel secundario.
 Debe calcularse y mostrarse la nota promedio. [EC]"""

"""nota1= int(input("ingrese la primera nota => "))
nota2= int(input("ingrese la segunda nota => "))
nota3= int(input("ingrese la tercera nota => "))

print((nota1+nota2+nota3)/3)"""

#esta es una funcion que permite ingrsar 3 notas y te calcula el promedio
def promedio(nota1,nota2,nota3):
    return (nota1+nota2+nota3)/3
notas=[] #creo una lista para guardar las notas 
for i in range(3):
    #Le pido que me pase las tres notas con un indice mostrando la nota
    notas.append(int(input(f"ingrese la nota {i+1} =>"))) 

print(promedio(*notas)) #imprimo la funcion con la lista como parametro