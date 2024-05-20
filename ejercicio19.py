nombres=[]
notas=[]
for x in range(3):
    nom=input("Ingrese el nombre del alumno: ")
    nombres.append(nom)

for x in range(3):
    nota=input("NOTA: ")
    notas.append(nota)

def cargar_nombres(*args):
    for arg in args:
        nom.append(arg)
def imprimir_nombres():
    for item in nombres:
        print(item, end=' | ')

def cargar_notas(*args):
    for arg in args:
        notas.append(arg)
def imprimir_notas():
    for item in notas:
        print(item, end=' | ')
cargar_nombres()
imprimir_nombres()
cargar_notas()
imprimir_notas()