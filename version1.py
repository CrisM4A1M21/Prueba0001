def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

def potencia(num1, num2):
    return num1 ** num2 


num1 = int(input("Ingrese el valor 1: "))
num2 = int(input("Ingrese el valor 2: "))

print("1. Sumar: ")
print("2. Resta: ")
print("3. Multiplicar: ")
print("4. Dividir: ")
print("5. Potencia: ")

opcion = int(input("Elija una opcion: "))

if(opcion == 1):
    print(suma(num1, num2))
if(opcion == 2):
    print(resta(num1, num2))
if(opcion == 3):
    print(multiplicar(num1, num2))
if(opcion == 4):
    print(dividir(num1, num2))
if(opcion == 5):
    print(potencia(num1, num2))