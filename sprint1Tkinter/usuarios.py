import tkinter as tk
from tkinter import messagebox
from tkinter import Menu

# Función para añadir un usuario a la lista
def agregar_usuario():
    nombre = entry_nombre.get()
    edad = escala_edad.get()
    genero = genero_seleccionado.get()

    if not nombre:
        messagebox.showwarning("Error", "El nombre no puede estar vacío")
        return

    usuario = f"{nombre}, {edad} años, {genero}"
    lista_usuarios.insert(tk.END, usuario)

# Función para eliminar un usuario seleccionado de la lista
def eliminar_usuario():
    seleccion = lista_usuarios.curselection()
    if seleccion:
        lista_usuarios.delete(seleccion)
    else:
        messagebox.showwarning("Error", "Selecciona un usuario para eliminar")

# Función para salir de la aplicación
def salir_aplicacion():
    root.quit()

# Función para guardar la lista de usuarios (simulada con un messagebox)
def guardar_lista():
    messagebox.showinfo("Guardar Lista", "La lista de usuarios ha sido guardada")

# Función para cargar la lista de usuarios (simulada con un messagebox)
def cargar_lista():
    messagebox.showinfo("Cargar Lista", "La lista de usuarios ha sido cargada")

# Crear la ventana principal
root = tk.Tk()
root.title("Registro de Usuarios")
root.geometry("400x600")

# Nombre del usuario
tk.Label(root, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.pack(pady=5)

# Barra deslizante para la edad del usuario
tk.Label(root, text="Edad:").pack(pady=5)
escala_edad = tk.Scale(root, from_=0, to=100, orient='horizontal')
escala_edad.pack(pady=5)

# Género del usuario
tk.Label(root, text="Género:").pack(pady=5)
genero_seleccionado = tk.StringVar()
genero_seleccionado.set("Masculino")
tk.Radiobutton(root, text="Masculino", variable=genero_seleccionado, value="Masculino").pack()
tk.Radiobutton(root, text="Femenino", variable=genero_seleccionado, value="Femenino").pack()
tk.Radiobutton(root, text="Otro", variable=genero_seleccionado, value="Otro").pack()

# Botón para agregar usuario
tk.Button(root, text="Añadir Usuario", command=agregar_usuario).pack(pady=5)

# Lista de usuarios
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_usuarios = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, width=50, height=10)
lista_usuarios.pack()

scrollbar.config(command=lista_usuarios.yview)

# Botón para eliminar usuario seleccionado
tk.Button(root, text="Eliminar Usuario", command=eliminar_usuario).pack(pady=5)

# Botón para salir de la aplicación
tk.Button(root, text="Salir", command=salir_aplicacion).pack(pady=5)

# Menú desplegable
menu_bar = Menu(root)
root.config(menu=menu_bar)

menu_archivo = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Guardar Lista", command=guardar_lista)
menu_archivo.add_command(label="Cargar Lista", command=cargar_lista)

# Ejecutar la aplicación
root.mainloop()