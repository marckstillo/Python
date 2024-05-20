traductor = {"CASA":"HOUSE", "LAPIZ":"PEN"}
while True:
    palabra = input ("INGRESE LA PALABRA A TRADUCIR: ")
    if palabra in traductor :
        print(traductor[palabra])
    elif palabra == 0:
        break
    else:
        resp=input ("NO EXISTE LA TRADUCCIÓN BUSCADA. ¿DESEA AGREGARLO?: (SI/NO)")
        if resp == "SI":
            traducción=input(f"INGRESE LA TRADUCCIÓN {palabra}: ")
            traductor[palabra] = traducción
