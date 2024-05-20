class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def avanza(self):
        print('ANDO CAMINANDO')
class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    def avanza(self):
        print('ANDO MOVIEND0ME EN MI BICICLETA')
if __name__ == '__main__':
    persona = Persona('PEPE')
    persona.avanza()

    ciclista = Ciclista('JUANCA')
    ciclista.avanza()