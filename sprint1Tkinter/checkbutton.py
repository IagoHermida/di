import tkinter as tk

#Crear la ventana principal
root = tk.Tk()
root.title("Selecciona tus Aficiones")

#Tamaño de la ventana
root.geometry("300x250")

#Variables asociadas a las casillas de verificación
aficion_leer = tk.BooleanVar()
aficion_deporte = tk.BooleanVar()
aficion_musica = tk.BooleanVar()


#Función para actualizar el estado de las aficiones seleccionadas
def actualizar_aficiones():
    seleccionadas = []

    if aficion_leer.get():
        seleccionadas.append("Leer")
    if aficion_deporte.get():
        seleccionadas.append("Deporte")
    if aficion_musica.get():
        seleccionadas.append("Música")

    texto_aficiones = ", ".join(seleccionadas) if seleccionadas else "Ninguna"
    etiqueta_aficiones.config(text=f"Aficiones seleccionadas: {texto_aficiones}")


#Checkbutton para las aficiones
check_leer = tk.Checkbutton(root, text="Leer", variable=aficion_leer, command=actualizar_aficiones)
check_leer.pack(pady=5)

check_deporte = tk.Checkbutton(root, text="Deporte", variable=aficion_deporte, command=actualizar_aficiones)
check_deporte.pack(pady=5)

check_musica = tk.Checkbutton(root, text="Música", variable=aficion_musica, command=actualizar_aficiones)
check_musica.pack(pady=5)

#Etiqueta para mostrar las aficiones seleccionadas
etiqueta_aficiones = tk.Label(root, text="Aficiones seleccionadas: Ninguna")
etiqueta_aficiones.pack(pady=20)

#Iniciar el bucle principal de la aplicación
root.mainloop()