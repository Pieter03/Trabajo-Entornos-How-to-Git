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
    
#Multiplicación
elif(opcion==3):
    resMultiplicacion= lambda x, y: x*y
    numero1=int(input("Introduce el primer número: "))
    numero2=int(input("Introduce el segundo número: "))
    resultado1=(numero1 * numero2)
    print(f"{numero1} * {numero2} = {resMultiplicacion(numero1, numero2)}")

#División
elif(opcion==4):
    resDivision= lambda x, y: x/y
    numero1=int(input("Introduce el primer número: "))
    numero2=int(input("Introduce el segundo número: "))
    if(numero2==0):
        print("No es posible dividir entre 0")
    else:
        resultado1=(numero1 / numero2)
        print(f"{numero1} / {numero2} = {resDivision(numero1, numero2)}")
        
#Cociente
elif(opcion==5):
    resCociente= lambda x, y: x//y
    numero1=int(input("Introduce el primer número: "))
    numero2=int(input("Introduce el segundo número: "))
    if(numero2==0):
        print("No es posible dividir entre 0")
    else:
        resultado1=(numero1 // numero2)
        print(f"Cociente de {numero1} // {numero2} = {resCociente(numero1, numero2)}")

#Resto   
elif(opcion==6):
    resResto= lambda x, y: x%y
    numero1=int(input("Introduce el primer número: "))
    numero2=int(input("Introduce el segundo número: "))
    if(numero2==0):
        print("No es posible dividir entre 0")
    else:
        resultado1=(numero1 % numero2)
        print(f"Resto de {numero1} % {numero2} = {resResto(numero1, numero2)}")

#Exponenciación
elif(opcion==7):
    resExponente= lambda x, y: pow(x, y)
    numero1=int(input("Introduce el primer número: "))
    numero2=int(input("Introduce el exponente: "))
    print(f"{numero1} elevado a {numero2} = {resExponente(numero1, numero2)}")
