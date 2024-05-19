class Persona:
    nombre = None
    edad = None

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar(self):
        return f"(self.nombre), EDAD: (self.edad)"

class Empleado(Persona):
    sueldo_bruto = None
    
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo
    def mostrar(self):
        return super().mostrar() + f" SN: {self.calcular_salario_neto()}"
    def calcular_salario_neto(self):
        return self.sueldo_bruto * 0.9

class Directivo(Empleado):
    categoria = None

    def __init__(self, categoria):
        self.categoria = categoria
    def mostrar(self):
        return 

class Cliente(Persona):
    telefono_de_contacto = None

    def __init__(self, nombre, edad, telefono_de_contacto ):
        super().__init__(nombre, edad)
        self.telefono_de_contacto = telefono_de_contacto
    
if __name__ == '__main__':
   