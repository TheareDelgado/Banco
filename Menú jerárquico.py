from pathlib import WindowsPath
import tkinter 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox

#crea ventana
root = Tk()
root.title("Menú Jerárquico Banco")
root.geometry("450x300")
root.resizable(width=False, height=False)



#crea treeview
arbol = ttk.Treeview(root)
arbol.heading("#0", text="Banco", anchor="nw")

#opciones
arbol.insert("", END, text="Operaciones", iid=0, open=False)
arbol.insert("", END, text="Clientes", iid=1, open=False)
arbol.insert("", END, text="Funcionario", iid=2, open=False)

#sub-opciones
arbol.insert("", END, text="Depositar", iid=3, open=False)
arbol.insert("", END, text="Retirar", iid=4, open=False)
arbol.insert("", END, text="Transferir", iid=5, open=False)
arbol.insert("", END, text="Préstamo", iid=6, open=False)

arbol.move(3,0,0)  #iid 3 (hijo) se asocia al iid 0 (padre) en la posición 0
arbol.move(4,0,1)
arbol.move(5,0,2)
arbol.move(6,0,3)



#posición
arbol.place(x=0,y=0)

def itemSeleccionado(event):
    for selected_item in arbol.selection():
        item = arbol.item(selected_item)

        valor = item["values"]
        nombreOpcion = item["text"]
        img = item["image"]
        abierto = item["open"]
        if nombreOpcion=="Depositar" or nombreOpcion=="Retirar" or nombreOpcion=="Transferir" or nombreOpcion=="Préstamo":
            messagebox.showinfo("Opción seleccionada", nombreOpcion+" es hijo de Operaciones")

arbol.bind("<<TreeviewSelect>>", itemSeleccionado)


root.mainloop()