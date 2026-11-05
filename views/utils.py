# Funcion para centrar una ventana en Tkinter
def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    coordenada_x = (pantalla_ancho // 2) - (ancho // 2)
    coordenada_y = (pantalla_alto // 2) - (alto // 2)

    return f"{ancho}x{alto}+{coordenada_x}+{coordenada_y}"