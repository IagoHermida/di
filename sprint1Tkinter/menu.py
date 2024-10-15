import tkinter as tk
from tkinter import messagebox

# Función para la opción de "Abrir"
def abrir_archivo():
    messagebox.showinfo("Abrir", "Aquí se debería abrir un archivo")
# Función para la opción de "Salir"
def salir():
    root.quit()

# Función para la opción "Acerca de"
def acerca_de():
    messagebox.showinfo("Acerca de", "Ejemplo mensaje informativo ejercicio 9")

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación con Menú")

# Crear la barra de menú
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

# Crear el menú "Archivo"
menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_separator()  # Separador
menu_archivo.add_command(label="Salir", command=salir)

# Crear el menú "Ayuda"
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)

# Ejecutar la ventana
root.mainloop()