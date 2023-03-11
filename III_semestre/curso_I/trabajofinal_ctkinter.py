import customtkinter
import tkinter
import customtkinter

customtkinter.set_appearance_mode("Dark")   
customtkinter.set_default_color_theme("dark-blue")  

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("550x300")
        self.title("")
        self.minsize(550, 300)
        self.maxsize(550,300)
    
    # configure grid layout (4x4)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(1, weight=1)
        
        self.frame = customtkinter.CTkFrame(master=self, width=200, height=100)
        self.frame.grid(row=0, column=0, padx=(10,0), pady=10, sticky="nsew")

        self.frame2 = customtkinter.CTkFrame(master=self) #, width=300, height=100)
        self.frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.frame2.grid_rowconfigure(0,weight=1)
        # self.frame2.grid_rowconfigure(1,weight=1)
        self.frame2.grid_columnconfigure((0,1), weight=1)

        #
        # FRAME: 1
        #

        self.frame_title = customtkinter.CTkFrame(master=self.frame)
        self.frame_title.grid(row=0, column=0, padx=(10,10), pady=10, sticky="nsew")

        self.logo_label = customtkinter.CTkLabel(master=self.frame_title, text="FERROTEK SAC", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=10, pady=10)

        def fun_button_exit():
            print("SALIR")

        self.button_exit = customtkinter.CTkButton(master=self.frame, width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="SALIR",
                                 font=customtkinter.CTkFont(size=14),
                                 command=fun_button_exit)
        self.button_exit.grid(row=1, column=0, padx=20, pady=(160,20))


        #
        # FRAME: 2
        #

        # CONTENEDOR
        self.frame_div = customtkinter.CTkFrame(master=self.frame2,width=250,height=200)
        self.frame_div.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 0), sticky="nsew")

        self.frame_conte = customtkinter.CTkFrame(master=self.frame_div,width=250,height=200)
        self.frame_conte.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")


        # NOMBRE
        self.label_name = customtkinter.CTkLabel(master=self.frame_conte, text="Nombre        :")
        self.label_name.grid(row=0, column=0)

        self.entry = customtkinter.CTkEntry(master=self.frame_conte,placeholder_text="")
        self.entry.grid(row=0, column=1, columnspan=3)

        # CATEGORIA
        self.label_name = customtkinter.CTkLabel(master=self.frame_conte, text="Categoria     :")
        self.label_name.grid(row=1, column=0)

        def segmented_button_callback(value):
            print("Categoria:", value)

        segemented_button = customtkinter.CTkSegmentedButton(master=self.frame_conte,
                                                            values=["A", "B", "C"],
                                                            command=segmented_button_callback)
        segemented_button.grid(row=1, column=1)
        segemented_button.set("A")

        # NOMBRE
        self.label_name = customtkinter.CTkLabel(master=self.frame_conte, text="Horas Extra :")
        self.label_name.grid(row=2, column=0)

        self.entry = customtkinter.CTkEntry(master=self.frame_conte,placeholder_text="")
        self.entry.grid(row=2, column=1, padx=10)

        # NOMBRE
        self.label_name = customtkinter.CTkLabel(master=self.frame_conte, text="Tardanza     :")
        self.label_name.grid(row=3, column=0)

        self.entry = customtkinter.CTkEntry(master=self.frame_conte,placeholder_text="")
        self.entry.grid(row=3, column=1, padx=10)

        # BOTON LIMPIAR
        def fun_button_exit():
            print("SALIR")

        self.button_exit = customtkinter.CTkButton(master=self.frame2, width=100,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="LIMPIAR",
                                 command=fun_button_exit)
        self.button_exit.grid(row=1, column=0)
        #BOTON IMPRIMIR
        def fun_button_exit():
            print("SALIR")

        self.button_exit = customtkinter.CTkButton(master=self.frame2, width=80,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="IMPRIMIR",
                                 command=fun_button_exit)
        self.button_exit.grid(row=1, column=1)

        





if __name__ == "__main__":
    app = App()
    app.mainloop()