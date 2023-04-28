# ------------------------
# Desktop app No. 1
#-------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *

#-----------------------------
# funciones de la app
#-----------------------------

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

#Titulo de la ventana
ventana_principal.title("Bandera de Colombia")

#tamaño de la ventana
ventana_principal.geometry("500x500")

#desahabilitar boton de maximizar
ventana_principal.resizable(False, False)  

#color de fondo de la  ventana
ventana_principal.concfig(bg="skyblue")

#-----------------------------
# frame amarillo
#-----------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="yellow", width=500, height=150)
frame_amarillo.place(x=8, y=0)
 
#------------------
# frame azul
#------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=500, height=125)
frame_azul.place(x=0, y=250)

#------------------
# frame rojo
#------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=125)
frame_rojo.place(x=0, y=375)

#run
#se ejejcuta el metodo mainloop()de la clase Tk() a travez de la instancia ventana_principa.Este metodo despliega una ventana en pantalla y queda a la espera de lo que elusuario haga (click en un boton, escribir, etc).
