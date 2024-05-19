from tkinter import *
from tkinter.ttk import *
from Reproductor import *
musica = Reproductor ('musica/.mp3')
def play_musica():
    musica.volumen(0.8)
    musica.play()
def pause_musica():
    musica.volumen(0.8)
    musica.pause()
master = Tk()
master.geometry("200x200")
label=Label(master, text= "REPRODUCTOR DE MÚSICA")
label.pack(pady = 10)
btn_play=Button(master, text ="REPRODUCIR", command = play_musica)
btn_play.pack(pady = 10)
btn_pause=Button(master, text ="PAUSA", command = pause_musica)
btn_pause.pack(pady = 10)
mainloop()
