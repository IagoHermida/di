import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Elige tu color favorito")

# Tamaño de la ventana
root.geometry("300x200")

# Variable para almacenar el color seleccionado
color_seleccionado = tk.StringVar(value="")

# Función para cambiar el color de fondo según la opción seleccionada
def cambiar_color():
    color = color_seleccionado.get()
    if color == "Rojo":
        root.config(bg="red")
    elif color == "Verde":
        root.config(bg="green")
    elif color == "Azul":
        root.config(bg="blue")

# Pedir al  usuario que seleccione color
etiqueta = tk.Label(root, text="Selecciona tu color favorito:")
etiqueta.pack(pady=10)

# Radiobutton para elegir el color favorito
radio_rojo = tk.Radiobutton(root, text="Rojo", variable=color_seleccionado, value="Rojo", command=cambiar_color)
radio_rojo.pack(pady=5)

radio_verde = tk.Radiobutton(root, text="Verde", variable=color_seleccionado, value="Verde", command=cambiar_color)
radio_verde.pack(pady=5)

radio_azul = tk.Radiobutton(root, text="Azul", variable=color_seleccionado, value="Azul", command=cambiar_color)
radio_azul.pack(pady=5)

# Iniciar el bucle principal de la aplicación
root.mainloop()