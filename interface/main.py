from gui import FormularioIngreso
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Taller App")
app.geometry("450x450")


form = FormularioIngreso(master=app)
form.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")


app.mainloop()