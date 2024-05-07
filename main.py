# # print('Hello World')
# variable = "Hello"
# print(variable)  # Hello
# variable = "World"
# print(variable)  # World
# # Operaciones simples
# a = 5
# b = 6
# c = 5 + 6
# d = 6 - 5
# e = 5 * 6
# print(c, d, e)  # 11 1 30
# print(id(c))  # Posición de memoria que almacena la variable
# print(id(d))
# # --Ejercicio2--
# nombre =  "Dan"
# numero = 12345678
# correo = "dorozco0@gmail.com"
# print("Prueba2")
# print("\n", "Yo me llamo: " + nombre, "\n", numero, "\n", correo)
# # Tipos de variables
# print(type(nombre))
# print(type(numero))
# f = "1"
# g = "2"
# h = False
# print("Concatenar: ", f + g)
# print("Sumar: ", int(f) + int(g))
# h = 3 < 5
# print(h)
# if h:
#     print("hola")
# else:
#     print("bye")
# # Nombre = int(input("Ingresa un numero: "))
# # Apellido = int(input("Ingresa otro numero: "))
# # resul = Nombre + Apellido
# # print("La suma da:", resul)
# # calif = int(input("Como estuvo tu día (1-10): "))
# # print("Mi día estuvo de:", calif)
# Titulo = input("Dime el titulo del libro: ")
# Autor = input("Y su autor es...: ")
# print(Titulo, "fue escrito por", Autor)
# a = 3
# b = 2
# suma = a + b
# resta = a - b
# mult = a * b
# div = a / b
# divS = a // b
# mod = a % b
# exp = a ** b
# print(f'El resultado de suma es: {suma}')  # Interpolacion
# print(f'El resultado de resta es: {resta}')
# print(f'El resultado de multiplicacion es: {mult}')
# print(f'El resultado de division es: {div}')
# print(f'El resultado de division sin decimal es: {divS}')
# print(f'El resultado de modulo es: {divS}')
# print(f'El resultado de modulo es: {exp}')
# al = int(input("Dime el alto del rectangulo: "))
# an = int(input("Dime el ancho del rectangulo: "))
# ar = al * an
# per = (al + an) * 2
# print(f'El perimetro del rectangulo es {per} y el area es {ar}')
# var = 10
# print(var)
# var += 1  # Se le suma 1 a la variable
# print(var)
# var += 1
# var += 1
# print(var)
# var *= 3
# print(var)
# var /= 4
# print(var)
# res = (a != b)  # a es diferente que b?
# print(res)
# res = (a == b)  # a es igual que b?
# print(res)
# res = (a < b)
# print(res)
# res = (a > b)
# print(res)
# res = (a <= b)
# print(res)
# res = (a >= b)
# print(res)
# par = int(input("Ingresa un numero: "))
# res = par % 2
# # print(res)
# if res == 0:
#     print(f"El numero {par} es par")
# else:
#     print(f"El numero {par} es impar")
# edad = int(input("Ingresa tu edad: "))
# print("Eres mayor de edad " if edad >= 18 else "Eres menor de edad")
# a = True
# b = True
# res = a and b  # Ambos true
# print(res)
# res = a or b  # Alguno true
# print(res)
# res = not b  # Es falso este valor? Devuelve true
# print(res)
# res = not a  # Es falso este valor? Devuelve true
# print(res)
# numeroo = int(input("Dame un numero: "))
# a = numeroo >= 0
# b = numeroo <= 5
# print(f"El numero {numeroo} se encuentra en el rango 0 - 5" if a and b else
#       f"El numero {numeroo} no se encuentra en el rango 0 - 5")
# dia = input("Tienes vacaciones? ")
# dai = False
# res = False
# if dia.lower() == "si":
#     res = True
# else:
#     res = False
# print(res)
# dai = input("Tienes dia de descanso? ")
# if dai.lower() == "si":
#     res2 = True
# else:
#     res2 = False
# print(dai.lower())  # lower() convierte all a minuscula
# print(res2)
# print("No puedes visitar a tu hijo" if not (res or res2) else "Puedes visitar al chamaco")
# age = int(input("Dime tu edad: "))
# # v = age >= 20 and age < 30
# # t = age >= 30 and age < 40
# # print(v)
# # print(t)
# # if (age >= 20 and age < 30) or (age >= 30 and age < 40):
# if (20 <= age < 30) or (30 <= age < 40):
#     # print("En el rango de 20's o 30's")
#     if 20 <= age < 30:
#         print(f"Tienes {age} jovenzuelo")
#     elif 30 <= age < 40:
#         print(f"Tienes {age} viejito")
#     # else:
#     #     print("Fuera de rango")
# else:
#     print("Fuera de rango")
# # print(f"Tienes {age} jovencito" if v or t else f"Ni entre 20's ni 30's")
# mM = int(input("Dame un numero: "))
# Mm = int(input("Dame otro numero: "))
# print(f"El numero mayor es {mM}" if mM > Mm else f"El numero mayor es {Mm}")
# print("Dame los siguientes datos de un libro: ")
# Name = input("Nombre del libro: ")
# Id = int(input("Id del libro: "))
# Price = float(input("Precio con decimales: "))
# EnvioG = input("True o False: ")
# EnvioG = EnvioG.lower()
# if EnvioG == "true":
#     EnvioG = True
# elif EnvioG == "false":
#     EnvioG = False
# else:
#     EnvioG = False
# print(f'''
#     Nombre: {Name}
#     ID: {Id}
#     Precio: {Price}
#     ¿Envio gratuito?: {EnvioG}
# ''')
# print("Nombre:", Name, "\nID:", Id, "\nPrecio:", Price, "\nEnvio gratis:", EnvioG)
#  Sentencias IF/ELSE
# numeroo = int(input('Dame tu calif: '))
# NumT = None
# if 9 <= numeroo <= 10:
#     NumT = 'A'
# elif 8 <= numeroo < 9:
#     NumT = 'B'
# elif 7 <= numeroo < 8:
#     NumT = 'C'
# elif 6 <= numeroo < 7:
#     NumT = 'D'
# elif 0 <= numeroo < 6:
#     NumT = 'F'
# else:
#     NumT = '?'
# print(f'Tu calificacion es {numeroo}, sacaste una {NumT} ')
# -----------Ciclos------------------
# cont = 0
# Max = 5
# while cont <= Max:
#     print(cont)
#     cont += 1
# else:
#     print('Fin ciclo')
#
# cont2 = 5
# Min = 1
# while cont2 >= Min:
#     print(cont2)
#     cont2 -= 1
# else:
#     print('Fin ciclo')
#
# # -------- FOR -------------
# cad = 'Hola'
#
# for letra in cad:
#     print(letra)
# else:
#     print('En ciclo')
# cont = 1
# for letra in "Holanda":
#     if letra == 'a':
#         print(f'Letra encontrada {letra} un total de {cont} vez')
#         cont += 1
#         break
# else:
# #     print('Fin ciclo')
# for i in range(6):
#     if i % 2 == 0:
#         print(f'El valor es {i}')
# for n in range(6):
#     if n % 2 != 0:
#         continue
#     print(f'El valor es {n}')
# nombres = ["Juan", "Carlos", "Karla"]
# print(nombres[0:3])
# for nombre in nombres:
#     print(nombre)
# else:
#     print('No hay mas nombres')
#
# print(len(nombres))
# nombres.append("Juan2")  # Append añadir
# print(nombres)
# nombres.insert(1, "Pepe")
# print(nombres)
# nombres.remove("Juan2")
# print(nombres)
# nombres.pop()
# print(nombres)
# del nombres[0]
# print(nombres)
# for i in range(11):
#     if i % 3 == 0:
#         print(f'El valor es {i}')
# for i in range(2, 7):
#     print(f'El valor es {i}')
# for i in range(3, 11, 2):
#     print(f'El valor es22 {i}')
# # ----------- Tuplas ------------
# frutas = ('Naranja', 'Platano', 'Manzana')
# for fruta in frutas:
#     print(fruta, end=' ')
# flist = list(frutas)
# flist.append("Hola")
# frutas = tuple(flist)
# print(frutas)
# Modificar tupla ---------------------------
# tupla = (13, 1, 8, 3, 2, 5, 8)
# ft = list(tupla)
# ll = []
# for f in ft:
#     if f < 5:
#         ll.append(f)
# ft = ll
# print(ft)
# Set ----------------------------
