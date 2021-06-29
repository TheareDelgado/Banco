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

imagenBanco = Image.open("./banco.png")
imagenBanco =imagenBanco.resize((24,27),Image.ANTIALIAS)
imagenBanco = ImageTk.PhotoImage(imagenBanco)


#crea treeview
arbol = ttk.Treeview(root)
arbol.heading("#0", text="Banco", anchor="nw", image=imagenBanco)

#opciones                       
arbol.insert("", END, text="Operaciones", iid=0, open=False)
arbol.insert("", END, text="Clientes", iid=1, open=False)
arbol.insert("", END, text="Funcionarios", iid=2, open=False)

#sub-opciones operaciones
imagenCliente = Image.open("./man.png")
imagenCliente =imagenCliente.resize((18,21),Image.ANTIALIAS)
imagenCliente = ImageTk.PhotoImage(imagenCliente)

imagenFuncionario = Image.open("./profile.png")
imagenFuncionario =imagenFuncionario.resize((18,21),Image.ANTIALIAS)
imagenFuncionario = ImageTk.PhotoImage(imagenFuncionario)


imagenDepositar = Image.open("./depositar.png")
imagenDepositar =imagenDepositar.resize((18,21),Image.ANTIALIAS)
imagenDepositar = ImageTk.PhotoImage(imagenDepositar)

imagenRetirar = Image.open("./retirar.png")
imagenRetirar = imagenRetirar.resize((18,21),Image.ANTIALIAS)
imagenRetirar = ImageTk.PhotoImage(imagenRetirar)


imagenPrestamo = Image.open("./prestamo.png")
imagenPrestamo = imagenPrestamo.resize((18,21),Image.ANTIALIAS)
imagenPrestamo = ImageTk.PhotoImage(imagenPrestamo)

imagenTransferir = Image.open("./transferir.png")
imagenTransferir = imagenTransferir.resize((18,21),Image.ANTIALIAS)
imagenTransferir = ImageTk.PhotoImage(imagenTransferir)


arbol.insert("", END, text="Depositar", iid=3, open=False, image=imagenDepositar)
arbol.insert("", END, text="Retirar", iid=4, open=False, image=imagenRetirar)
arbol.insert("", END, text="Transferir", iid=5, open=False, image=imagenTransferir)
arbol.insert("", END, text="Préstamo", iid=6, open=False, image=imagenPrestamo)

arbol.move(3,0,0)  #iid 3 (hijo) se asocia al iid 0 (padre) en la posición 0
arbol.move(4,0,1)
arbol.move(5,0,2)
arbol.move(6,0,3)

#sub opciones depositar
                                                                    #NOMBRE     RUT  MONTO
arbol.insert("", END, text="Cliente n°1", iid=15, open=False, values=("Nicolas Rubio","13.078.680-4","$120.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente n°2", iid=16, open=False, values=("Martin Galvez","11.027.247-2","$300.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente n°3", iid=17, open=False, values=("Eduardo Molina","26.680.492-K","$550.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente n°4", iid=18, open=False, values=("Susana Gomez","10.433.522-5","$1.000.000"), image=imagenCliente)

arbol.move(15,3,0)
arbol.move(16,3,1)
arbol.move(17,3,2)
arbol.move(18,3,3)

#sub opciones retirar
                                                                    #NOMBRE     RUT  MONTO
arbol.insert("", END, text="Cliente n°1", iid=19, open=False, values=("Alejandro Perez","18.769.066-8","$700.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente n°2", iid=20, open=False, values=("Marcela Valenzuela","9.675.192-3","$950.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente n°3", iid=21, open=False, values=("Moises Cruz","13.005.382-3","$200.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente n°4", iid=22, open=False, values=("Angela Vera","18.351.461-K","$100.000"), image=imagenCliente)

arbol.move(19,4,0)
arbol.move(20,4,1)
arbol.move(21,4,2)
arbol.move(22,4,3)

#sub opciones transferir
                                                                 #DE: NOMBRE     RUT  MONTO----->NOMBRE
arbol.insert("", END, text="Cliente n°1", iid=23, open=False, values=("Antonio Alvarez","21.480.890-0","$150.000","Angela Vera"), image=imagenCliente)
arbol.insert("", END, text="Cliente n°2", iid=24, open=False, values=("Manuel Estrada","16.002.895-5","$250.000","Moises Cruz"), image=imagenCliente)
arbol.insert("", END, text="Cliente n°3", iid=25, open=False, values=("Mauro Hernandez","18.329.054-1","$400.000","Martin Galvez"), image=imagenCliente)
arbol.insert("", END, text="Cliente n°4", iid=26, open=False, values=("Leticia Mora","11.777.803-7","$550.000","Susana Gomez"), image=imagenCliente)

arbol.move(23,5,0)
arbol.move(24,5,1)
arbol.move(25,5,2)
arbol.move(26,5,3)

#sub opciones prestamo
                                                                    #NOMBRE  MONTO CUOTAS
arbol.insert("", END, text="Cliente n°1", iid=27, open=False, values=(" Alan Cortes"," $1.000.000"," 12"), image=imagenCliente)
arbol.insert("", END, text="Cliente n°2", iid=28, open=False, values=(" Daniela Muñoz"," $500.000"," 6"), image=imagenCliente)
arbol.insert("", END, text="Cliente n°3", iid=29, open=False, values=(" Felipe Ortiz"," $300.000"," 3"), image=imagenCliente)
arbol.insert("", END, text="Cliente n°4", iid=30, open=False, values=(" Bryan Carrasco"," $700.000"," 9"), image=imagenCliente)

arbol.move(27,6,0)
arbol.move(28,6,1)
arbol.move(29,6,2)
arbol.move(30,6,3)


#sub-opciones clientes
arbol.insert("", END, text="Cliente 1", iid=7, open=False, values=("Nicolas", "Rubio","13.078.680-4","$80.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 2", iid=8, open=False, values=("Martin", "Galvez","11.027.247-2","$150.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 3", iid=9, open=False, values=("Eduardo", "Molina","26.680.492-K","$340.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 4", iid=10, open=False, values=("Susana", "Gomez","10.433.522-5","$200.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 5", iid=31, open=False, values=("Alejandro", "Perez","18.769.066-8","$1.000.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 6", iid=32, open=False, values=("Marcela", "Valenzuela","9.675.192-3","$1.250.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 7", iid=33, open=False, values=("Moises", "Cruz","13.005.382-3","$500.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 8", iid=34, open=False, values=("Angela", "Vera","18.351.461-K","$230.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 9", iid=35, open=False, values=("Antonio", "Alvarez","21.480.890-0","$750.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 10", iid=36, open=False, values=("Manuel", "Estrada","16.002.895-5","$400.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 11", iid=37, open=False, values=("Mauro", "Hernandez","18.329.054-1","$800.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 12", iid=38, open=False, values=("Leticia", "Mora","11.777.803-7","$980.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 13", iid=39, open=False, values=("Alan", "Cortes","15.376.718-1","$320.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 14", iid=40, open=False, values=("Daniela", "Muñoz","21.705.714-0","$175.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 15", iid=41, open=False, values=("Felipe", "Ortiz","24.163.364-0","$250.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 16", iid=42, open=False, values=("Bryan", "Carrasco","19.834.112-6","$435.000"), image=imagenCliente)

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
arbol.insert("", END, text="Funcionario 1", iid=11, open=False, values=("Cesar ","Mora ", "20377093-6"), image=imagenFuncionario)
arbol.insert("", END, text="Funcionario 2", iid=12, open=False, values=("Theare ","Delgado ", "20225477-2"), image=imagenFuncionario)
arbol.insert("", END, text="Funcionario 3", iid=13, open=False, values=("Diego ","Gonzalez ", "20297405-8"), image=imagenFuncionario)

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

        iid=arbol.focus()
        
        #IF para los Clientes de DEPOSITAR
        if iid=="15":
             messagebox.showinfo("Datos Deposito n°1", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="16":
             messagebox.showinfo("Datos Deposito n°2", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="17":
             messagebox.showinfo("Datos Deposito n°3", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="18":
             messagebox.showinfo("Datos Deposito n°4", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))

        #IF para los Clientes de RETIRAR
        if iid=="19":
             messagebox.showinfo("Datos Deposito n°1", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="20":
             messagebox.showinfo("Datos Deposito n°2", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="21":
             messagebox.showinfo("Datos Deposito n°3", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="22":
             messagebox.showinfo("Datos Deposito n°4", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))

        #IF para los Clientes de TRANSFERENCIA
        if iid=="23":
             messagebox.showinfo("Datos Transferencia n°1", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2])+"--------> "+valor[3])
        if iid=="24":
             messagebox.showinfo("Datos Transferencia n°2", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2])+"--------> "+valor[3])
        if iid=="25":
             messagebox.showinfo("Datos Transferencia n°3", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2])+"--------> "+valor[3])
        if iid=="26":
             messagebox.showinfo("Datos Transferencia n°4", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2])+"--------> "+valor[3])

        #IF para los Clientes de PRÉSTAMO
        if iid=="27":
             messagebox.showinfo("Datos Préstamo n°1", " Nombre: "+valor[0]+"\n Monto solicitado: "+str(valor[1])+"\n N° Cuotas: "+str(valor[2]))
        if iid=="28":
             messagebox.showinfo("Datos Préstamo n°2", " Nombre: "+valor[0]+"\n Monto solicitado: "+str(valor[1])+"\n N° Cuotas: "+str(valor[2]))
        if iid=="29":
             messagebox.showinfo("Datos Préstamo n°3", " Nombre: "+valor[0]+"\n Monto solicitado: "+str(valor[1])+"\n N° Cuotas: "+str(valor[2]))
        if iid=="30":
             messagebox.showinfo("Datos Préstamo n°4", " Nombre: "+valor[0]+"\n Monto solicitado: "+str(valor[1])+"\n N° Cuotas: "+str(valor[2]))




        #IF para los FUNCIONARIOS
        if iid=="11":
            messagebox.showinfo("Datos Funcionario 1", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2]))
        if iid=="12":
            messagebox.showinfo("Datos Funcionario 2", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2]))
        if iid=="13":
            messagebox.showinfo("Datos Funcionario 3", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2]))
        
        #IF Para los CLIENTES
        if iid=="7":
            messagebox.showinfo("Datos Cliente 1", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="8":
            messagebox.showinfo("Datos Cliente 2", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="9":
            messagebox.showinfo("Datos Cliente 3", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="10":
            messagebox.showinfo("Datos Cliente 4", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="31":
            messagebox.showinfo("Datos Cliente 5", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="32":
            messagebox.showinfo("Datos Cliente 6", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="33":
            messagebox.showinfo("Datos Cliente 7", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="34":
            messagebox.showinfo("Datos Cliente 8", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="35":
            messagebox.showinfo("Datos Cliente 9", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="36":
            messagebox.showinfo("Datos Cliente 10", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="37":
            messagebox.showinfo("Datos Cliente 11", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="38":
            messagebox.showinfo("Datos Cliente 12", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="39":
            messagebox.showinfo("Datos Cliente 13", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="40":
            messagebox.showinfo("Datos Cliente 14", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="41":
            messagebox.showinfo("Datos Cliente 15", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="42":
            messagebox.showinfo("Datos Cliente 16", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))



arbol.bind("<<TreeviewSelect>>", itemSeleccionado)


root.mainloop()