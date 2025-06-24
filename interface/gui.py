import customtkinter as ctk

class FormularioIngreso(ctk.CTkFrame):

    
    def __init__(self, master):
        super().__init__(master)
        self.crear_widgets()
        self.pack_propagate(False)

    def crear_widgets(self):
        # Titulo
        titulo = ctk.CTkLabel(self, text="Formulario de ingreso", font=ctk.CTkFont(size=20, weight="bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # Dia de entrada
        self.label_dia_entrada = ctk.CTkLabel(self, text="Dia de entrada:")
        self.label_dia_entrada.grid(row=1, column=0, sticky="e", padx=10, pady=5)

        self.entry_dia_entrada = ctk.CTkEntry(self)
        self.entry_dia_entrada.grid(row=1, column=1, sticky="w", padx=10, pady=5)    

        #Numero de cliente
        self.label_numero_de_cliente = ctk.CTkLabel(self, text="Numero de cliente:")
        self.label_numero_de_cliente.grid(row=2, column=0, sticky="e", padx=10, pady=5)

        self.entry_numero_de_cliente = ctk.CTkEntry(self)
        self.entry_numero_de_cliente.grid(row=2, column=1, sticky="w", padx=10, pady=5) 

        #Nombre del cliente
        
        self.label_nombre_de_cliente = ctk.CTkLabel(self, text="Nombre de cliente:")
        self.label_nombre_de_cliente.grid(row=3, column=0, sticky="e", padx=10, pady=5)

        self.entry_nombre_de_cliente = ctk.CTkEntry(self)
        self.entry_nombre_de_cliente.grid(row=3, column=1, sticky="w", padx=10, pady=5)

        
        #año

        self.label_año = ctk.CTkLabel(self, text="Introduzca año del vehiculo:")
        self.label_año.grid(row=4, column=0, sticky="e", padx=10, pady=5)
        
        self.entry_año = ctk.CTkEntry(self)
        self.entry_año.grid(row=4, column=1, sticky="w", padx=10, pady=5) 

        #Modelo

        self.label_marca = ctk.CTkLabel(self, text="Introduzca Marca del vehiculo:")
        self.label_marca.grid(row=5, column=0, sticky="e", padx=10, pady=5)

        self.entry_marca = ctk.CTkEntry(self)
        self.entry_marca.grid(row=5, column=1, sticky="w", padx=10, pady=5) 

        #VIN

        self.label_vin = ctk.CTkLabel(self, text="Introduzca VIN:")
        self.label_vin.grid(row=6, column=0, sticky="e", padx=10, pady=5)

        self.entry_vin = ctk.CTkEntry(self)
        self.entry_vin.grid(row=6, column=1, sticky="w", padx=10, pady=5)

        #Causa

        self.label_causa = ctk.CTkLabel(self, text="Posible Causa:")
        self.label_causa.grid(row=7, column=0, sticky="e", padx=10, pady=5)
        
        self.entry_causa = ctk.CTkEntry(self)
        self.entry_causa.grid(row=7, column=1, sticky="w", padx=10, pady=5)

        #Guardar

        self.entry_Guardar = ctk.CTkButton(self, text="Guardar Datos", command=self.guardar_datos)
        self.entry_Guardar.grid(row=12, column=0, columnspan=2, pady=20)
        
    def guardar_datos(self): #guardar datos 
        
        datos = {
            "Dia_Entrada": self.entry_dia_entrada.get(),
            "numero_cliente": self.entry_numero_de_cliente.get(),
            "nombre_de_cliente": self.entry_nombre_de_cliente.get(),
            "Año": self.entry_año.get(),
            "Marca": self.entry_marca.get(),
            "Vin": self.entry_vin.get(),
            "Causa": self.entry_causa.get(),

        }
        print("Datos Guardados")
        print(datos)
        pass
    