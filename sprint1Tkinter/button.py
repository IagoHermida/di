import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana con botones")

# Tamaño de la ventana
root.geometry("300x200")

# Función que mostrará un mensaje en la etiqueta
def mostrar_mensaje():
    etiqueta.config(text="Mensaje tras pulsar")

# Crear una etiqueta vacía donde se mostrará el mensaje
etiqueta = tk.Label(root, text="")
etiqueta.pack(pady=10)

# Botón para mostrar el mensaje
boton_mensaje = tk.Button(root, text="Mostrar mensaje", command=mostrar_mensaje)
boton_mensaje.pack(pady=5)

# Botón para cerrar la ventana
boton_cerrar = tk.Button(root, text="Cerrar", command=root.quit)
boton_cerrar.pack(pady=5)

# Iniciar el bucle principal de la aplicación
root.mainloop()