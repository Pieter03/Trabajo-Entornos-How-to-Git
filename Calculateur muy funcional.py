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


#Área Cuadrado
elif(opcion==8):
    resAreaCuadrado= lambda x: pow(x, 2)
    lado=int(input("Introduce el lado del cuadrado: "))
    print(f"El área de un cuadrado de lado {lado} es {resAreaCuadrado(lado)} metros cuadrados")

#Área Rectángulo
elif(opcion==9):
    resMultiplicacion= lambda x, y: x*y
    base=int(input("Introduce la base del rectángulo: "))
    altura=int(input("Introduce la altura del rectángulo: "))
    print(f"El área de un rectángulo de base {base} y altura {altura} es {resMultiplicacion(base, altura)} metros cuadrados")

#Área Triángulo
elif(opcion==10):
    resAreaTriangulo= lambda x, y: x*y/2
    base=int(input("Introduce la base del triángulo: "))
    altura=int(input("Introduce la altura del triángulo: "))
    print(f"El área de un triángulo de base {base} y altura {altura} es {resAreaTriangulo(base, altura)} metros cuadrados")

#Área Círculo
elif(opcion==11):
    resAreaCirculo= lambda x: math.pi*x**2
    radio=int(input("Introduce el radio del círculo: "))
    print(f"El área de un círculo de radio {radio} es {round(resAreaCirculo(radio), 2)} metros cuadrados")
    
#Salir
elif(opcion==12):
    print("Cerrando la calculadora...")
    

