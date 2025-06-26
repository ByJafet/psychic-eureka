import customtkinter as ctk
import json, os



    
class FormularioIngreso(ctk.CTkFrame):
    

    
    def __init__(self, master):
        self.registros = []
        super().__init__(master)
        self.crear_widgets()
        self.pack_propagate(False)
        self.cargar_desde_json()

    

    def crear_widgets(self):
        # Titulo
        titulo = ctk.CTkLabel(self, text="Formulario de ingreso", font=ctk.CTkFont(size=25, weight="bold"))
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
        self.entry_Guardar.grid(row=8, column=1, columnspan=2, pady=20)
        
        #a
        #self.frame_botones = ctk.CTkFrame(self)
        #self.frame_botones.grid(row=0, column=0, columnspan=2, sticky="s", padx=10, pady=(10,0))
        
        
        
        
        
        
        #Boton de registro

        self.boton_mostrar = ctk.CTkButton(self, text="Mostrar Registros", command=self.abrir_ventana_registros)
        self.boton_mostrar.place(relx=0.03, rely=0.878 )

    
    
    def mostrar_registros(self):
        print("\m--- Lista de registros ---")
        for i, registro in enumerate(self.registros, start=1):
            print(f"Registro #{i}:")
            for clave, valor in registro.items():
                print(f"  {clave}: {valor}")
            print("---------------------------")
            
    
    def cargar_desde_json(self):
        if os.path.exists("datos.json"):
            with open("datos.json", "r", encoding="utf-8") as archivo:
                self.registros = json.load(archivo)


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
        
        self.registros.append(datos)

        print("Registro guardado correctamente")
        print(f"Total  registros: {len(self.registros)}")
        print("Ultimo registro:", datos)

        self.guardar_en_archivo_json()

    
   
   
    def abrir_ventana_registros(self):
        registro_seleccionado = {"registro": None}
        ventana = ctk.CTkToplevel(self)
        ventana.title("Registros")
        ventana.geometry("600x400")
        
        
        frame_edicion = ctk.CTkFrame(ventana)
        frame_edicion.pack(fill="x", padx=10, pady=10)

        campo_busqueda = ctk.CTkEntry(ventana, placeholder_text="Buscar")
        campo_busqueda.pack(padx=10, pady=(10, 5), fill="x")

       

        

        boton_buscar = ctk.CTkButton(ventana, text="Buscar", command=lambda: filtrar_registros(campo_busqueda.get()))
        boton_buscar.pack(padx=10, pady=(0, 10))

        frame_resultados = ctk.CTkScrollableFrame(ventana)
        frame_resultados.pack(fill="both", expand=True, padx=10, pady=(50, 10))

        def editar_registro_en_mismo_frame():
            registro = registro_seleccionado["registro"]
            if not registro:
                print("Fail")
                return
            for widget in frame_edicion.winfo_children():
                widget.destroy()

            entradas = {}
            fila = 0

            
            for clave, valor in registro.items():
                label = ctk.CTkLabel(frame_edicion, text=clave + ":")
                label.grid(row=fila, column=0, padx=10, pady=5, sticky="e")

                entry = ctk.CTkEntry(frame_edicion)
                entry.insert(0, valor)
                entry.grid(row=fila, column=1, padx=10, pady=5, sticky="w")
                entradas[clave] = entry
                fila += 1
            
            def guardar_cambios():
                for clave in entradas:
                    registro[clave] = entradas[clave].get()
                
                self.guardar_en_archivo_json()
                filtrar_registros("")
                
                boton_guardar = ctk.CTkButton(frame_edicion, text="Guardar Cambios", command=guardar_cambios)
                boton_guardar.grid(row=fila + 1, column=0, columnspan=2, pady=10)

        boton_editar = ctk.CTkButton(
            ventana,
            text="Editar Registro",
            command=editar_registro_en_mismo_frame
        )
        boton_editar.pack(padx=10, pady=(0, 10))
            
        
       
        def filtrar_registros(texto):

            def seleccionar_registro(r):
                return lambda e: registro_seleccionado.update({"registro": r})
            
            for widget in frame_resultados.winfo_children():
                widget.destroy()
        
            texto = texto.lower()

            resultados = [
                r for r in self.registros
                if texto in r["nombre_de_cliente"].lower()
                or texto in r["Marca"].lower()
                or texto in r["Año"].lower()
                or texto in r["numero_cliente"].lower
                or texto in r["Dia_Entrada"].lower()
            ]

            for i, registro in enumerate(resultados, start=1):
             texto_registro = f"{i}. Cliente: {registro['nombre_de_cliente']} | Marca: {registro['Marca']} | Numero: {registro['numero_cliente']} | Año: {registro['Año']} | Entrada: {registro['Dia_Entrada']}"
            
             
             
             etiqueta = ctk.CTkLabel(frame_resultados, text=texto_registro, anchor="w")
             etiqueta.pack(fill="x", padx=5, pady=2)
             etiqueta.bind("<Button-1>", seleccionar_registro(registro))
    
        
        

        
       

        
        
        
        
        filtrar_registros("")





    def guardar_en_archivo_json(self):
        with open("datos.json", "w", encoding="utf-8") as archivo:
            json.dump(self.registros, archivo, indent=4, ensure_ascii=False)