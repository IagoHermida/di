import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Texto con Barra de Desplazamiento")

# Crear un Frame para contener el Text y la Scrollbar
frame_texto = tk.Frame(root)
frame_texto.pack(padx=10, pady=10)

# Crear el widget Text
texto = tk.Text(frame_texto, wrap="word", height=15, width=50)
texto.pack(side="left", fill="both", expand=True)

# Crear la barra de desplazamiento vertical
scrollbar = tk.Scrollbar(frame_texto, orient="vertical", command=texto.yview)
scrollbar.pack(side="right", fill="y")

# Configurar el Text para que se sincronice con la Scrollbar
texto.config(yscrollcommand=scrollbar.set)

# Añadir contenido largo al widget Text
contenido_largo = """Ejemplo de texto largo

Linea 1

Linea 2

Linea 3

Linea 4

Linea 5

Linea 6

Linea 7

Linea 8

Linea 9

Linea 10

Linea 11"""

# Insertar el contenido largo en el widget Text
texto.insert("1.0", contenido_largo)

# Ejecutar la ventana
root.mainloop()