#ESCRIBA UN PROGRAMA PARA VALIDAR SI LOS DATOS DE ACCESO SON CORRECTOS
"""(USUARIO Y COTRASEÑA) SE ENCUENTRAN EN EL DICCIONARIO"""
# DAR VALIDEZ DE SOLO 3 INTENTOS ERRONEOS DE CONTRASEÑA UTILIZANDO CICLO WHILE 
usuarios = {"admin": "124554", "PEPE":"BURBUJA", "CAMILA":"CAMI"}
intentos = 0
user = input("INGRESE EL USUARIO: ")
password = input("INGRESE LA CONTRASEÑA: ")
#VALIDAR LOS DATOS DEL USUARIO
if user in usuarios:
    intentos += 1
    while intentos <=3:
        if usuarios[user] == password:
            print ("ACCESO CORRECTO")
            break
        elif intentos == 3:
            print ("Su cuenta se ha bloqueado por seguridad")
            break
        else: 
            intentos += 1
            print ("ACCESO DENEGADO")
            password=input(f"INTENTO {intentos} DE 3. INGRESE SU CONTRASEÑA: ")
else:
    print("EL USUARIO NO EXISTE")