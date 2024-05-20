#operadores aritméticos
#imprimir la suma de 3+4
print("La sauma de 10 + 4 es: ", 10 + 4)

#resolver todas las operaciones : 10+4, 10*4, 10/4, 10%4, 10//4, 10**4
print("la suma es: ", 10 + 3)
print("la multiplicación es: ", 10 * 4)
print("la divisióm es: ", 10 / 4)
print("el resultado es: ", 10 % 4)
print("el coeficiente es: ", 10 // 4)
print("la potencia es: ", 10 ** 4)

#resolver la ecuación cuadratica: 2x²-7x+3=0
a= 2
b= -7
c= 3
x1 = (-b+(b**2-4*a*c)**0.5)/(2*a);
x2 = (-b-(b**2-4*a*c)**0.5)/(2*a);
print("el resultado de x1 es: ", x1)
print("el resultado de x2 es: ", x2)

#operaciones con cadenas de textos 
print("SNPP " + "CTFPPJ " + "PROGRAMACIÓN PYTHON")
#PRINT("AULA" + 2102 ) AQUI TENDREMOS UN ERROR , 2102 NO ES UNA CADENA DE TEXTO, USA STR()

#OPERACIONES MIXTAS 
print ("Tun chi " * 5)
print ("JA " * (2**3))

#operadores de comparación 
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

#operaciones con cadenas de textos 
print("python" > "PYTHON")
print("aaaa" >= "abaa") #orientación alfábetica por ASCII
print(len("aaaa") >= len("abaa")) #cuenta caracteres

print("python" != "PYTHON")

###operdores lógicos 
print(10 > 4 and "Z" > "A")
print(10 > 4 or "Z" > "A")
print(not(10 > 4 )and "Z" >"A")