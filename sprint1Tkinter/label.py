import tkinter as tk

def cambiar_texto():
    etiqueta3.config(text="¡Texto cambiado!")

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana de Ejemplo")

# Crear las etiquetas
etiqueta1 = tk.Label(root, text="Bienvenido a la aplicación")
etiqueta1.pack(pady=10)

etiqueta2 = tk.Label(root, text="Iago Hermida")
etiqueta2.pack(pady=10)

etiqueta3 = tk.Label(root, text="Texto original")
etiqueta3.pack(pady=10)

# Crear el botón
boton = tk.Button(root, text="Cambiar texto", command=cambiar_texto)
boton.pack(pady=20)

# Iniciar el bucle de la ventana
root.mainloop()