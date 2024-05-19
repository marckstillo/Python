from pygame import mixer 
class Reproductor:
    #atributos
    archivo = None
    #constructor
    def __init__ (self, archivo):
        self.archivo =archivo
        mixer.init()
        mixer.music.load(archivo)
    def play (self):
        mixer.music.play()
        return"REPRODUCIENDO MÚSICA"
    def pause (self):
        mixer.music.pause()
        return"LA MÚSICA SE HA PAUSADO"
    def stop (self):
        mixer.music.stop()
        return"LA MÚSICA SE DETUVO"
    def volumen (self, v):
        mixer.music.set_volume(v)
        return "DEFINIENDO EL VOLUMEN A {}".format(v)