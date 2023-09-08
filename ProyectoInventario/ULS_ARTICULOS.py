import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk          ### Descargar a traves de la terminal de comandos (cmd) usando el codigo "pip install Pillow"


def ventana_agregar():
    window = tk.Toplevel()
    window.geometry("512x512")
    window.title("Agregar Producto")
    window.iconbitmap('icono1.ico')

    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    titulo = tk.Label(window, text="Agregar Productos", font=("Arial", 16))
    titulo.pack(pady=20)

    entryproducto = tk.StringVar()
    entryprecio = tk.StringVar()
    cantidad_var = tk.StringVar()  # Variable para almacenar la cantidad seleccionada
    cantidad_var.set("seleccionar")

    etiquetanombre = tk.Label(window, text="Ingrese Nombre del Producto:")
    etiquetanombre.pack()
    productotx = tk.Entry(window, textvariable=entryproducto)
    productotx.pack(pady=10)

    etiquetacantidad = tk.Label(window, text="Ingrese Cantidad del Producto:")
    etiquetacantidad.pack()
    
    # Crear el menú desplegable (select) con las opciones
    opciones_cantidad = ["Kg", "g", "Lts", "unid."]
    cantidad_menu = tk.OptionMenu(window, cantidad_var, *opciones_cantidad)
    cantidad_menu.pack(pady=7)
    cantidad_menu.config(width=10)
    cantidad_menu.place(x=335, y=155)

    preciotx = tk.Entry(window, textvariable=entryprecio)
    preciotx.pack(pady=10)

    def guarda():
        db = sqlite3.connect("articulos.s3db")
        c = db.cursor()
        nombre = entryproducto.get()
        precio = entryprecio.get()
        cantidad = cantidad_var.get()
        cantidadTotal = f"{precio} {cantidad}"
        c.execute("insert into articulos (nombre,precio) values ('"+nombre+"','"+cantidadTotal+"')")
        db.commit()
        c.close()
        messagebox.showinfo("MODIFICACIÓN", "ARTÍCULO INGRESADO")
        window.destroy()

    menu = tk.Button(window, text="MENU", fg="red", font=("Arial", 12), borderwidth=10, cursor="hand2", command=window.destroy)
    menu.pack()
    menu.place(x=218, y=275)

    btguardar = tk.Button(window, text="GUARDAR", fg="blue", font=("Arial", 12), borderwidth=10, cursor="hand2", relief="raised", command=guarda)
    btguardar.pack(pady=20)
    btguardar.bind("<Enter>", lambda event, button=btguardar: button.config(bg="lightblue"))
    btguardar.bind("<Leave>", lambda event, button=btguardar: button.config(bg="SystemButtonFace"))

def ventana_ver():
    #.withdraw()
    window=tk.Toplevel()
    window.geometry("512x512")
    window.iconbitmap('icono1.ico')

    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    e1=tk.Label(window, text="BUSCAR PRODUCTOS :", font=("Arial", 16)).place(x=50, y=45),
    e_codigo=tk.Label(window, text="CODIGO", font=("Arial", 12)).place(x=50, y=70)
    e_nombre=tk.Label(window, text="NOMBRE", font=("Arial", 12)).place(x=150, y=70)
    e_precio=tk.Label(window, text="CANTIDAD", font=("Arial", 12)).place(x=250, y=70)
    def mostrar():
##        codigo
        lista=tk.Listbox(window, width = 30, font=("arial", 12), height =15 )
        lista.pack()
        db = sqlite3.connect("articulos.s3db")
        c = db.cursor()
        c.execute("select * from articulos ORDER BY (codigo)DESC")
        for row in c:
            lista.insert(0,row[1]+"---------------"+ row[2])
        lista.place(x=150,y=90)
##        nombre
        lista_1=tk.Listbox(window, width = 10, font=("arial", 12), height =15 )
        lista_1.pack()
        db = sqlite3.connect("articulos.s3db")
        c = db.cursor()
        c.execute("select codigo from articulos ORDER BY (codigo)DESC")
        for row in c:
            lista_1.insert(0,row[0])
        lista_1.place(x=50,y=90)

  

    menu=tk.Button(window, text="MENU", fg="red", font=("Arial", 12), borderwidth=10, cursor="hand2",command = window.destroy)
    menu.pack()
    menu.place(x=50,y=392)

    bt_mostrar = tk.Button(window, text =  "MOSTRAR PRODUCTOS", fg="blue", font=("Arial", 12), borderwidth=10, cursor="hand2",command = mostrar)
    bt_mostrar.pack()
    bt_mostrar.place(x=270,y=390)
def ventana_eliminar():
    window = tk.Toplevel()
    window.geometry("512x512")
    window.title("Eliminar Producto")
    window.iconbitmap('icono1.ico')

    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1) 

    titulo = tk.Label(window, text="Eliminar Producto", font=("Arial", 16))
    titulo.pack(pady=20)

    entry_id = tk.StringVar()

    etiquetacodigo = tk.Label(window, text="Ingrese Código del Producto:")
    etiquetacodigo.pack()
    productotx = tk.Entry(window, textvariable=entry_id)
    productotx.pack(pady=10)

    def eliminar():
        db = sqlite3.connect("articulos.s3db")
        c = db.cursor()
        id_producto = entry_id.get()
        c.execute("DELETE FROM articulos WHERE codigo = ?", (id_producto,))
        db.commit()
        c.close()
        messagebox.showinfo("MODIFICACIÓN", "ARTÍCULO ELIMINADO")
        window.destroy()

    menu=tk.Button(window, text="MENU", fg="red", font=("Arial", 12), borderwidth=10, cursor="hand2",command = window.destroy)
    menu.pack()
    menu.place(x=218,y=220)

    bt_eliminar = tk.Button(window, text="ELIMINAR PRODUCTO", fg="blue", font=("Arial", 12), borderwidth=10, cursor="hand2", command=eliminar)
    bt_eliminar.pack(pady=20)
    bt_eliminar.bind("<Enter>", lambda event, button=bt_eliminar: button.config(bg="lightblue"))
    bt_eliminar.bind("<Leave>", lambda event, button=bt_eliminar: button.config(bg="SystemButtonFace"))

def ventana_modificar():
    window = tk.Toplevel()
    window.geometry("512x512")
    window.title("Modificar Producto")
    window.iconbitmap('icono1.ico')

    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1) 

    titulo = tk.Label(window, text="Modificar Producto", font=("Arial", 16))
    titulo.pack(pady=20)

    entry_id = tk.StringVar()
    entry_nuevo_precio = tk.StringVar()

    etiquetacodigo = tk.Label(window, text="Ingrese Código del Producto:")
    etiquetacodigo.pack()
    productotx = tk.Entry(window, textvariable=entry_id)
    productotx.pack(pady=10)

    etiquetanuevoprecio = tk.Label(window, text="Ingrese La nueva cantidad:")
    etiquetanuevoprecio.pack()
    nuevopreciotx = tk.Entry(window, textvariable=entry_nuevo_precio)
    nuevopreciotx.pack(pady=10)

    def modificar():
        db = sqlite3.connect("articulos.s3db")
        c = db.cursor()
        id_producto = entry_id.get()
        nuevo_precio = entry_nuevo_precio.get()
        c.execute("UPDATE articulos SET precio = ? WHERE codigo = ?", (nuevo_precio, id_producto))
        db.commit()
        c.close()
        messagebox.showinfo("MODIFICACIÓN", "ARTÍCULO MODIFICADO")
        window.destroy()

    menu=tk.Button(window, text="MENU", fg="red", font=("Arial", 12), borderwidth=10, cursor="hand2",command = window.destroy)
    menu.pack()
    menu.place(x=218,y=275)

    bt_modificar = tk.Button(window, text="MODIFICAR PRODUCTO", fg="blue", font=("Arial", 12), borderwidth=10, cursor="hand2", relief="raised", command=modificar)
    bt_modificar.pack(pady=20)
    bt_modificar.bind("<Enter>", lambda event, button=bt_modificar: button.config(bg="lightblue"))
    bt_modificar.bind("<Leave>", lambda event, button=bt_modificar: button.config(bg="SystemButtonFace"))

windows = tk.Tk()
windows.title("Inventario de Productos")
windows.geometry("700x500")
# Establecer el icono personalizado (reemplaza 'icono.ico' con la ruta de tu archivo .ico)
windows.iconbitmap('icono1.ico')

background_image = Image.open("backgroud2.pgm")
background_image = background_image.resize((700, 500), Image.LANCZOS)
background_image = ImageTk.PhotoImage(background_image)

background_label = tk.Label(windows, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1) 


# Utilizamos una fuente diferente, color y centrado para el título
titulo_principal = tk.Label(windows, text="Inventario de Productos", font=("Helvetica", 24, "bold"), fg="blue")
titulo_principal.pack(pady=20)

b1 = tk.Button(windows, text="Agregar Producto", fg="blue", font=("Arial", 14), borderwidth=10, cursor="hand2", relief="raised", command=ventana_agregar)
b1.pack()
b1.place(relx=0.5, rely=0.3, anchor='center')

b2 = tk.Button(windows, text="Buscar Producto", fg="blue", font=("Arial", 14), borderwidth=10, cursor="hand2", relief="raised", command=ventana_ver)
b2.pack()
b2.place(relx=0.5, rely=0.45, anchor='center')

b3 = tk.Button(windows, text="Eliminar Producto", fg="blue", font=("Arial", 14), borderwidth=10, cursor="hand2", relief="raised", command=ventana_eliminar)
b3.pack()
b3.place(relx=0.5, rely=0.6, anchor='center')

b4 = tk.Button(windows, text="Modificar Producto", fg="blue", font=("Arial", 14), borderwidth=10, cursor="hand2", relief="raised", command=ventana_modificar)
b4.pack()
b4.place(relx=0.5, rely=0.75, anchor='center')

windows.mainloop()
