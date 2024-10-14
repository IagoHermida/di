import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Selecciona una fruta")

# Tamaño de la ventana
root.geometry("500x400")

# Función para mostrar la fruta seleccionada
def mostrar_fruta():
    # Obtener la selección actual del Listbox
    seleccion = listbox_frutas.curselection()
    if seleccion:  # Verificar si hay una selección
        fruta = listbox_frutas.get(seleccion)  # Obtener el valor seleccionado
        etiqueta_resultado.config(text=f"Fruta seleccionada: {fruta}")
    else:
        etiqueta_resultado.config(text="No has seleccionado ninguna fruta")

# Lista de frutas
frutas = ["Manzana", "Banana", "Naranja"]

# Crear el Listbox con las frutas
listbox_frutas = tk.Listbox(root)
for fruta in frutas:
    listbox_frutas.insert(tk.END, fruta)
listbox_frutas.pack(pady=10)

# Botón para mostrar la fruta seleccionada
boton_mostrar = tk.Button(root, text="Mostrar fruta", command=mostrar_fruta)
boton_mostrar.pack(pady=10)

# Etiqueta para mostrar el resultado de la selección
etiqueta_resultado = tk.Label(root, text="Fruta seleccionada: Ninguna")
etiqueta_resultado.pack(pady=20)

# Iniciar el bucle principal de la aplicación
root.mainloop()