#condicionales.py
num_1 = int(input("INGRESE EL PRIMER NUMERO: "))
num_2 = int(input("INGRESE EL SEGUNDO NUMERO: "))
if(num_1 > num_2):
    print("{} es mayor a {}".format(num_1,num_2))
    if(num_1 % 2 == 0): 
        print("EL NUMERO ES PAR")
    else: 
        print("EL NUMERO ES IMPAR")
elif(num_1 < num_2): 
    print("{} es mayor a {}".format(num_2,num_1))
    if(num_2 % 2 == 0):
        print("EL NUMERO ES PAR")
    else:
        print("EL NUMERO ES IMPAR")
else:
    print("LOS NUMEROS INGRESADOS SON IGUALES")

print("----------------------------------------------------")
usuario = input("ingrese un usuario: ")
password = input("ingrese su contraseña: ")
if(usuario == "admin" and password == "12345"):
    print("ACCESO CORRECTO")
else: 
    print("ACCESO DENEGADO")