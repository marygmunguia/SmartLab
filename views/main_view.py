import customtkinter as ctk
from views.utils import centrar_ventana

class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SmartLab - Sistema para laboratorio médico")
        posicion_ventana = centrar_ventana(self, 1080, 720)
        self.geometry(posicion_ventana)

        boton = ctk.CTkButton(self, text="Haz click", command=self.haz_click).pack(pady=20)

    def haz_click(self):
        print("Estas haciendo click.")