import tkinter as tk


# Función para dibujar el círculo y el rectángulo
def dibujar():
    # Limpiar el canvas
    canvas.delete("all")

    # Obtener las coordenadas del círculo
    x1_circulo = int(entry_x1_circulo.get())
    y1_circulo = int(entry_y1_circulo.get())
    x2_circulo = int(entry_x2_circulo.get())
    y2_circulo = int(entry_y2_circulo.get())

    # Obtener las coordenadas del rectángulo
    x1_rect = int(entry_x1_rect.get())
    y1_rect = int(entry_y1_rect.get())
    x2_rect = int(entry_x2_rect.get())
    y2_rect = int(entry_y2_rect.get())

    # Dibujar el círculo
    canvas.create_oval(x1_circulo, y1_circulo, x2_circulo, y2_circulo, outline="blue", width=2)

    # Dibujar el rectángulo
    canvas.create_rectangle(x1_rect, y1_rect, x2_rect, y2_rect, outline="red", width=2)


# Crear la ventana principal
root = tk.Tk()
root.title("Dibujo de Círculo y Rectángulo")

# Crear el Canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.grid(row=0, column=0, columnspan=4)

# Etiquetas y campos de entrada para las coordenadas del círculo
tk.Label(root, text="Círculo (x1, y1, x2, y2):").grid(row=1, column=0, padx=5, pady=5)
entry_x1_circulo = tk.Entry(root)
entry_y1_circulo = tk.Entry(root)
entry_x2_circulo = tk.Entry(root)
entry_y2_circulo = tk.Entry(root)
entry_x1_circulo.grid(row=1, column=1)
entry_y1_circulo.grid(row=1, column=2)
entry_x2_circulo.grid(row=1, column=3)
entry_y2_circulo.grid(row=1, column=4)

# Etiquetas y campos de entrada para las coordenadas del rectángulo
tk.Label(root, text="Rectángulo (x1, y1, x2, y2):").grid(row=2, column=0, padx=5, pady=5)
entry_x1_rect = tk.Entry(root)
entry_y1_rect = tk.Entry(root)
entry_x2_rect = tk.Entry(root)
entry_y2_rect = tk.Entry(root)
entry_x1_rect.grid(row=2, column=1)
entry_y1_rect.grid(row=2, column=2)
entry_x2_rect.grid(row=2, column=3)
entry_y2_rect.grid(row=2, column=4)

# Botón para dibujar las figuras
boton_dibujar = tk.Button(root, text="Dibujar", command=dibujar)
boton_dibujar.grid(row=3, column=0, columnspan=5, pady=10)

# Ejecutar la ventana
root.mainloop()