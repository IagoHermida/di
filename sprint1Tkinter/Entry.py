import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Saludo Personalizado")

# Tamaño de la ventana
root.geometry("300x200")

# Función para mostrar el saludo
def mostrar_saludo():
    nombre = entrada_nombre.get()  # Obtener el texto del campo de entrada
    saludo = f"Hola, {nombre}"  # Crear el saludo
    etiqueta_saludo.config(text=saludo)  # Actualizar la etiqueta con el saludo

# Etiqueta para pedir al usuario que introduzca su nombre
etiqueta_instruccion = tk.Label(root, text="Escribe tu nombre:")
etiqueta_instruccion.pack(pady=10)

# Campo de entrada para el nombre
entrada_nombre = tk.Entry(root, width=30)
entrada_nombre.pack(pady=5)

# Botón para generar el saludo
boton_saludar = tk.Button(root, text="Saludar", command=mostrar_saludo)
boton_saludar.pack(pady=10)

# Etiqueta donde se mostrará el saludo personalizado
etiqueta_saludo = tk.Label(root, text="")
etiqueta_saludo.pack(pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()