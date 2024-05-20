#cargar e imprimir una lista con funciones 
#definimos una lista vacia 
lista = []
#definimos la función que permitirá cargar una lista 
def cargar_lista(dato):
    lista.append(dato)
#recibir una cantidad indeterminado de argumentos 
def cargar_lista(*args):
    for arg in args:
        lista.append(arg)
def imprimir_lista():
    for item in lista:
        print(item, end=' | ')
#ejecutamos las funciones
cargar_lista(25)
cargar_lista(53)
cargar_lista(75)
cargar_lista(100)
#impimimos la lista 
imprimir_lista()
cargar_lista('A','B','C',[125,852,963])
imprimir_lista()