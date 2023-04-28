#------------------------------
# Bandera Noruega
#------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *


ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Bandera de Francia")

# tamaño de la ventana
ventana_principal.geometry("800x480")

# deshabilitar boton maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="red")

#------------------------------
# frame blanca
#------------------------------
frame_blanca= Frame(ventana_principal)
frame_blanca.config(bg="white", width=800, height=130)
frame_blanca.place(x=0, y=175)

#------------------------------
# frame blanco
#------------------------------
frame_blanco= Frame(ventana_principal)
frame_blanco.config(bg="white", width=126, height=480)
frame_blanco.place(x=190, y=0)

#------------------------------
# frame Azul
#------------------------------
frame_azul= Frame(ventana_principal)
frame_azul.config(bg="blue4", width=800, height=94)
frame_azul.place(x=0, y=193)

#------------------------------
# frame azul
#------------------------------
frame_azul= Frame(ventana_principal)
frame_azul.config(bg="blue4", width=95, height=480)
frame_azul.place(x=205, y=0)

# run
# se ejecuta el metodo mainlop() de la clase Tk () a través de la instancia ventana_principal. Este metodo despliega una ventana en la pantalla y queda a la espera de lo que el usuario haga (click en un botón, escrubir, etc). Cada acción del usuario se conoce como un evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()