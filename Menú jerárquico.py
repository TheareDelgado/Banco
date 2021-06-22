from pathlib import WindowsPath
import tkinter 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox

#crea ventana
root = Tk()
root.title("Menú Jerárquico Banco")
root.geometry("450x400")
root.resizable(width=False, height=False)



#crea treeview
arbol = ttk.Treeview(root)
arbol.heading("#0", text="Banco", anchor="nw")

#opciones
arbol.insert("", END, text="Operaciones", iid=0, open=False)
arbol.insert("", END, text="Clientes", iid=1, open=False)
arbol.insert("", END, text="Funcionarios", iid=2, open=False)

#sub-opciones operaciones
arbol.insert("", END, text="Depositar", iid=3, open=False)
arbol.insert("", END, text="Retirar", iid=4, open=False)
arbol.insert("", END, text="Transferir", iid=5, open=False)
arbol.insert("", END, text="Préstamo", iid=6, open=False)

arbol.move(3,0,0)  #iid 3 (hijo) se asocia al iid 0 (padre) en la posición 0
arbol.move(4,0,1)
arbol.move(5,0,2)
arbol.move(6,0,3)

#sub opciones depositar
arbol.insert("", END, text="Cliente 1", iid=15, open=False)
arbol.insert("", END, text="Cliente 2", iid=16, open=False)
arbol.insert("", END, text="Cliente 3", iid=17, open=False)
arbol.insert("", END, text="Cliente 4", iid=18, open=False)

arbol.move(15,3,0)
arbol.move(16,3,1)
arbol.move(17,3,2)
arbol.move(18,3,3)

#sub opciones retirar
arbol.insert("", END, text="Cliente 1", iid=19, open=False)
arbol.insert("", END, text="Cliente 2", iid=20, open=False)
arbol.insert("", END, text="Cliente 3", iid=21, open=False)
arbol.insert("", END, text="Cliente 4", iid=22, open=False)

arbol.move(19,4,0)
arbol.move(20,4,1)
arbol.move(21,4,2)
arbol.move(22,4,3)

#sub opciones transferir
arbol.insert("", END, text="Cliente 1", iid=23, open=False)
arbol.insert("", END, text="Cliente 2", iid=24, open=False)
arbol.insert("", END, text="Cliente 3", iid=25, open=False)
arbol.insert("", END, text="Cliente 4", iid=26, open=False)

arbol.move(23,5,0)
arbol.move(24,5,1)
arbol.move(25,5,2)
arbol.move(26,5,3)

#sub opciones prestamo
arbol.insert("", END, text="Cliente 1", iid=27, open=False)
arbol.insert("", END, text="Cliente 2", iid=28, open=False)
arbol.insert("", END, text="Cliente 3", iid=29, open=False)
arbol.insert("", END, text="Cliente 4", iid=30, open=False)

arbol.move(27,6,0)
arbol.move(28,6,1)
arbol.move(29,6,2)
arbol.move(30,6,3)


#sub-opciones clientes
arbol.insert("", END, text="Cliente 1", iid=7, open=False)
arbol.insert("", END, text="Cliente 2", iid=8, open=False)
arbol.insert("", END, text="Cliente 3", iid=9, open=False)
arbol.insert("", END, text="Cliente 4", iid=10, open=False)
arbol.insert("", END, text="Cliente 5", iid=31, open=False)
arbol.insert("", END, text="Cliente 6", iid=32, open=False)
arbol.insert("", END, text="Cliente 7", iid=33, open=False)
arbol.insert("", END, text="Cliente 8", iid=34, open=False)
arbol.insert("", END, text="Cliente 9", iid=35, open=False)
arbol.insert("", END, text="Cliente 10", iid=36, open=False)
arbol.insert("", END, text="Cliente 11", iid=37, open=False)
arbol.insert("", END, text="Cliente 12", iid=38, open=False)
arbol.insert("", END, text="Cliente 13", iid=39, open=False)
arbol.insert("", END, text="Cliente 14", iid=40, open=False)
arbol.insert("", END, text="Cliente 15", iid=41, open=False)
arbol.insert("", END, text="Cliente 16", iid=42, open=False)

arbol.move(7,1,0)  
arbol.move(8,1,1)
arbol.move(9,1,2)
arbol.move(10,1,3)
arbol.move(31,1,4)  
arbol.move(32,1,5)
arbol.move(33,1,6)
arbol.move(34,1,7)
arbol.move(35,1,8)  
arbol.move(36,1,9)
arbol.move(37,1,10)
arbol.move(38,1,11)
arbol.move(39,1,12)  
arbol.move(40,1,13)
arbol.move(41,1,14)
arbol.move(42,1,15)

#sub-opciones funcionarios
arbol.insert("", END, text="Funcionario 1", iid=11, open=False)
arbol.insert("", END, text="Funcionario 2", iid=12, open=False)
arbol.insert("", END, text="Funcionario 3", iid=13, open=False)

arbol.move(11,2,0)  
arbol.move(12,2,1)
arbol.move(13,2,2)

#posición
arbol.place(x=0,y=0)

def itemSeleccionado(event):
    for selected_item in arbol.selection():
        item = arbol.item(selected_item)

        valor = item["values"]
        nombreOpcion = item["text"]
        img = item["image"]
        abierto = item["open"]
        #if nombreOpcion=="Depositar" or nombreOpcion=="Retirar" or nombreOpcion=="Transferir" or nombreOpcion=="Préstamo":
            #messagebox.showinfo("Opción seleccionada", nombreOpcion+" es hijo de Operaciones")

arbol.bind("<<TreeviewSelect>>", itemSeleccionado)


root.mainloop()