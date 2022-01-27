import math

"""Calculadora"""
print("Calculdora de dos números")
print("                         ")
print("1. Suma")
print("2. Resta")
print("3. Multiplifación")
print("4. División")
print("5. Cociente")
print("6. Resto")
print("7. Exponenciación")
print("8. Área Cuadrado")
print("9. Área Rectángulo")
print("10. Área Triángulo")
print("11. Área Círculo")
print("12. Salir")

opcion=int(input("Seleccione el tipo de operación según su número asignado: "))

while opcion<1 or opcion>12: #Con este controlamos que este en el rango correcto
    opcion=int(input("Introduce le numero valido"))
#Suma
if(opcion==1):
    resSuma= lambda x, y: x+y
    numero1=int(input("Introduce el primer número: "))
    numero2=int(input("Introduce el segundo número: "))
    print(f"{numero1} + {numero2} = {resSuma(numero1, numero2)}")


#Resta    
elif(opcion==2):
    resResta= lambda x, y: x-y
    numero1=int(input("Introduce el primer número: "))
    numero2=int(input("Introduce el segundo número: "))
    resultado1=(numero1 - numero2)
    print(f"{numero1} - {numero2} = {resResta(numero1, numero2)}")