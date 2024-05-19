import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="traductor_es_in_marcos"
)
cursor = mydb.cursor()
palabra = input("INGRESE LA PALABRA A TRADUCIR: ")
sentencia = f"select ingles from traductor where espanol like '{palabra}'"
cursor.execute(sentencia)

resultado = cursor.fetchall()

for x in resultado:
    print(x)
while True:
    palabra = input ("INGRESE LA PALABRA A TRADUCIR: ")
    if palabra in x:
        print(x [palabra])
    elif palabra == 0:
        break
    else:
        resp=input ("NO EXISTE LA TRADUCCIÓN BUSCADA. ¿DESEA AGREGARLO?: (SI/NO)")
        if resp == "SI":
            traducción=input(f"INGRESE LA TRADUCCIÓN {palabra}: ")
            mydb [palabra] = traducción
