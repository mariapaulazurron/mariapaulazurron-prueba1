Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:34:34) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def pedirnumero():
	a=int(input("ingrese el valor de a:"))
	b=int(input("ingrese el valor de b:"))
	return a,b

>>> def suma(a,b):
	return a+b

>>> def resta(a,b):
	return a-b

>>> def multiplica (a,b):
	return a*b

>>> def menu(a,b):
	while True:
		print(f"que tipode operacion matematica desea realizar{a}y{b}1sumar,2restar,3multiplicar x salir")
		opcion=input()
		if opcion=="1":
			print(f"resultadoes:{suma(a,b)}")
			if opcion=="2"
			
SyntaxError: invalid syntax
>>> def menu(a,b):
	while True:
		print(f"que tipode operacion matematica desea realizar{a}y{b}1sumar,2restar,3multiplicar x salir")
		opcion=input()
		if opcion=="1":
			print(f"resultado es:{suma(a,b)}")
			if opcion=="2":
				print(f"resultado es;{resta(a,b)}")
				if opcion=="3":
					print(f"resultado es:{multiplicar(a,b)}")
					break
				input("presione cualquier tecla")