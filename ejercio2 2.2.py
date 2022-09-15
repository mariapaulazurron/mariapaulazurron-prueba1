Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:34:34) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>def main():
        n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce otro número: ") )
opcion = 0
           
print("¿Qué quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números")
opcion = int(input("Introduce un número: ") )     

if opcion == 1:
    print("La suma de",n1,"+",n2,"es",n1+n2)
elif opcion == 2:
    print("La resta de",n1,"-",n2,"es",n1-n2)
elif opcion == 3:
    print("El producto de",n1,"*",n2,"es",n1*n2)
else:
    print("Opción incorrecta")
