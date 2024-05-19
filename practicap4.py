def ordenar_lista(lista, orden):
    contador = 0
    for x in range(len(lista)-1):
        for y in range(len(lista)-1):
            if lista[y] > lista [y+1]:
                aux=lista[y]
                lista[y]=lista[y+1]
                lista[y+1]=aux
            contador+=1
    print("CONTADOR: ", contador)
    return lista
lista_original=[2,3,45,87,25,64,8,6,26,45]
print("LISTA ORIGINAL: ", lista_original)
lista_ordenada=ordenar_lista(lista_original, "asc")
print("LISTA ORDENADA ASCENDENTEMENTE: ", lista_ordenada)
def ordenar_lista(lista, orden):
    contador = 0
    for x in range(len(lista)-1):
        for y in range(len(lista)-1):
            if lista[y] < lista [y+1]:
                aux=lista[y]
                lista[y]=lista[y+1]
                lista[y+1]=aux
            contador+=1
    print("CONTADOR: ", contador)
    return lista
lista_original=[2,3,48,87,25,64,8,6,26,45]
print("LISTA ORIGINAL: ", lista_original)
lista_ordenada=ordenar_lista(lista_original, "asc")
print("LISTA ORDENADA DESCENDENTEMENTE: ", lista_ordenada)