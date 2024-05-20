calificaciones = [1,2,3,4,5]
nombres = ["MOISES","CAMILA","FERNANDA","PABLO","TANIA"]
lista_variada = [True, 10.5, "abc", [0,1,1]]
print("ESTUDIANTE: ", nombres[2])
print("CALIFICACIÓN: ", calificaciones[-2])
print("lista dentro de otra ", lista_variada[3][0])
print("imprimir un rango o slices ", nombres[1:2])
print(lista_variada)
#agregar elementos a una lista 
nombres.append("ANIBAL")
print(nombres)
#remover elementos de una lista
nombres.remove("PABLO")
print(nombres)