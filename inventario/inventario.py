import json
import tkinter as tk
from tkinter import messagebox

def cargar_productos():
    try:
        with open('inventario.json') as archivo:
            productos = json.load(archivo)
    except FileNotFoundError:
        productos = []
    
    return productos

def guardar_productos(productos):
    with open('inventario.json', 'w') as archivo:
        json.dump(productos, archivo, indent=4)

def agregar_producto():
    nombre = entry_nombre.get()
    precio = float(entry_precio.get())
    cantidad = int(entry_cantidad.get())

    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }

    productos = cargar_productos()
    productos.append(producto)
    guardar_productos(productos)

    messagebox.showinfo("Éxito", "Producto agregado con éxito.")

def eliminar_producto():
    indice = int(entry_indice.get())

    productos = cargar_productos()

    if indice < 0 or indice >= len(productos):
        messagebox.showerror("Error", "Índice inválido.")
        return

    del productos[indice]
    guardar_productos(productos)

    messagebox.showinfo("Éxito", "Producto eliminado con éxito.")

def mostrar_inventario():
    productos = cargar_productos()

    if len(productos) == 0:
        messagebox.showinfo("Inventario", "El inventario está vacío.")
        return

    inventario_text.delete('1.0', tk.END)

    inventario_text.insert(tk.END, "=== Inventario ===\n")
    for indice, producto in enumerate(productos):
        inventario_text.insert(tk.END, f"Índice: {indice}\n")
        inventario_text.insert(tk.END, f"Nombre: {producto['nombre']}\n")
        inventario_text.insert(tk.END, f"Precio: {producto['precio']}\n")
        inventario_text.insert(tk.END, f"Cantidad: {producto['cantidad']}\n")
        inventario_text.insert(tk.END, "------------------\n")

def buscar_producto():
    nombre_buscar = entry_buscar.get()

    productos = cargar_productos()

    encontrados = []
    for producto in productos:
        if producto['nombre'].lower() == nombre_buscar.lower():
            encontrados.append(producto)

    if len(encontrados) == 0:
        messagebox.showinfo("Búsqueda", "No se encontraron productos con ese nombre.")
        return

    inventario_text.delete('1.0', tk.END)

    inventario_text.insert(tk.END, "=== Resultados de búsqueda ===\n")
    for producto in encontrados:
        inventario_text.insert(tk.END, f"Nombre: {producto['nombre']}\n")
        inventario_text.insert(tk.END, f"Precio: {producto['precio']}\n")
        inventario_text.insert(tk.END, f"Cantidad: {producto['cantidad']}\n")
        inventario_text.insert(tk.END, "------------------\n")

window = tk.Tk()
window.title("Inventario")

label_nombre = tk.Label(window, text="Nombre:")
label_nombre.grid(row=0, column=0)
entry_nombre = tk.Entry(window)
entry_nombre.grid(row=0, column=1)

label_precio = tk.Label(window, text="Precio:")
label_precio.grid(row=1, column=0)
entry_precio = tk.Entry(window)
entry_precio.grid(row=1, column=1)

label_cantidad = tk.Label(window, text="Cantidad:")
label_cantidad.grid(row=2, column=0)
entry_cantidad = tk.Entry(window)
entry_cantidad.grid(row=2, column=1)

label_indice = tk.Label(window, text="Índice:")
label_indice.grid(row=3, column=0)
entry_indice = tk.Entry(window)
entry_indice.grid(row=3, column=1)

label_buscar = tk.Label(window, text="Buscar por nombre:")
label_buscar.grid(row=4, column=0)
entry_buscar = tk.Entry(window)
entry_buscar.grid(row=4, column=1)

button_agregar = tk.Button(window, text="Agregar", command=agregar_producto)
button_agregar.grid(row=5, column=0)

button_eliminar = tk.Button(window, text="Eliminar", command=eliminar_producto)
button_eliminar.grid(row=5, column=1)

button_mostrar = tk.Button(window, text="Mostrar inventario", command=mostrar_inventario)
button_mostrar.grid(row=6, column=0)

button_buscar = tk.Button(window, text="Buscar", command=buscar_producto)
button_buscar.grid(row=6, column=1)

inventario_text = tk.Text(window, width=40, height=10)
inventario_text.grid(row=7, columnspan=2)

window.mainloop()
