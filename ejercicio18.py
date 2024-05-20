agenda = {} # global para todas las funciones
def cargar_agenda(nombre, telefono):
    agenda[nombre] = telefono
def ver_agenda():
    print(agenda)
def ver_agenda_detalles():
    print("LISTA DE CONTACTOS")
    for nombre,tel in agenda.items():
        print(f"{nombre} : {tel}")
if __name__ == "__main__":
    cargar_agenda("Moises", "0987654321")
    cargar_agenda("Martha", "0986543725")
    cargar_agenda("Carlos", "0987456321")
    cargar_agenda("Salma", "0987626521")
    ver_agenda()
    ver_agenda_detalles()