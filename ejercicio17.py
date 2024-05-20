import os
#menu principal
respuesta = 1
while(respuesta != 0):
    print("ELIJA UNA OPCIÓN")
    print("1.CALCULADORA")
    print("2.VER MI IP")
    print("3.ADMINIDTRADOR DE TAREAS")
    print("4.APAGAR EL EQUIPO EN 5 MINUTOS")
    print("5.CANCELAR APAGADO")
    print("0.SALIR")
    respuesta = int(input(" |"))
    if(respuesta == 1):
        os.system('calc')
    elif(respuesta == 2):
        os.system('ipconfig')
    elif(respuesta == 3):
        os.system('taskmgr')
    elif(respuesta == 4):
        os.system('shutdown -s -t 300 ')
    elif(respuesta == 5):
        #ver como cancelar el apagado
        os.system('')
    else:
        "NO SE HA SELECCIONADO NADA "