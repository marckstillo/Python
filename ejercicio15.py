#calculadora
#FUNCIONES MATEMATICAS

def suma(a,b,m,n): 
    return a + b + m + n

def resta(a,b):
    return a - b

def multiplicación(a,b):
    return a*b

def división(a, b): 
    if (b == 0):
        return "NO SE PUEDE DIVIDIR POR CERO"
    else: 
        return a/b

def raiz(a,b = 2):
    return a ** (1/b)

#cuando ejecutamos el script, __name__ pasa a ser igual al string '__main__'
if __name__ == '__main__':
    print("LA SUMA ES DE: ", suma(3,4,2,1))
    print("LA RESTA ES DE: ", resta(3,4))
    print("LA MULTIPLICACIÓN ES DE: ", multiplicación(3,4))
    print("LA DIVISIÓN ES: ", división(3,0))
    print("LA RAIZ ES IGUAL A: ", raiz(25))