import tkinter as tk

# Función para mostrar el contenido del Entry en la etiqueta
def mostrar_texto():
    texto = entry.get()
    etiqueta_mostrar.config(text=texto)

# Función para borrar el contenido del Entry
def borrar_texto():
    entry.delete(0, tk.END)
    etiqueta_mostrar.config(text="")

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz con Frames")

# Tamaño de la ventana
root.geometry("300x200")

# Crear el Frame superior
frame_superior = tk.Frame(root)
frame_superior.pack(pady=10)

# Etiquetas y campo de entrada en el Frame superior
etiqueta1 = tk.Label(frame_superior, text="Etiqueta 1:")
etiqueta1.grid(row=0, column=0, padx=5, pady=5)

etiqueta2 = tk.Label(frame_superior, text="Etiqueta 2:")
etiqueta2.grid(row=1, column=0, padx=5, pady=5)

entry = tk.Entry(frame_superior)
entry.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta para mostrar el contenido del Entry
etiqueta_mostrar = tk.Label(frame_superior, text="", fg="blue")
etiqueta_mostrar.grid(row=1, column=1, padx=5, pady=5)

# Crear el Frame inferior
frame_inferior = tk.Frame(root)
frame_inferior.pack(pady=10)

# Botón para mostrar el contenido del Entry
boton_mostrar = tk.Button(frame_inferior, text="Mostrar", command=mostrar_texto)
boton_mostrar.grid(row=0, column=0, padx=10, pady=10)

# Botón para borrar el contenido del Entry
boton_borrar = tk.Button(frame_inferior, text="Borrar", command=borrar_texto)
boton_borrar.grid(row=0, column=1, padx=10, pady=10)

# Ejecutar la ventana
root.mainloop()