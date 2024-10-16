import tkinter as tk

# Función que actualiza el valor de la etiqueta
def actualizar_valor(valor):
    etiqueta.config(text=f"Valor seleccionado: {valor}")

# Crear la ventana principal
root = tk.Tk()
root.title("Barra Deslizante")

# Tamaño de la ventana
root.geometry("300x200")

# Crear una barra deslizante (Scale)
barra_deslizante = tk.Scale(root, from_=0, to=100, orient='horizontal', command=actualizar_valor)
barra_deslizante.pack(pady=20)

# Crear una etiqueta para mostrar el valor seleccionado
etiqueta = tk.Label(root, text="Valor seleccionado: 0")
etiqueta.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()