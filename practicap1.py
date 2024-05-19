notas = []
#j
for x in range (3):
    #validar si la nota esta entre el 1 y 5 
    nota = 0
    while nota < 1 or nota > 5:
        nota = int (input(f"INGRESE LA NOTA {x+1}: "))
    notas.append(nota)
total = 0
for x in range (3):
    total += notas[x]
#calculo del promedio
promedio = total /3
print ("EL PROMEDIO DE LAS 3 NOTAS ES: %.2f"% promedio)
#VERIFICAR SI ESTÁ REPROBADO O APROBADO
print ("ESTADO:")
if (promedio > 1.7):
    print("APROBADO")
else:
    print("REPROBADO")
