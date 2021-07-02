from Main import abrirDepositar
from pathlib import WindowsPath
import tkinter 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from Main import *
import statistics as stats
from numpy import mat
import matplotlib.pyplot as plt


NombreClienteNuevo=""
RutClienteNuevo=""
SaldoClienteNuevo=""
rutFinal=""
ApellidoClienteNuevo=""
NombreDestino=""
ApellidoDestino=""
MontoDestino=""
MontoFinal=""


#crea ventana
root = Tk()
root.title("Menú Jerárquico Banco")
root.geometry("450x400")
root.resizable(width=False, height=False)
img = PhotoImage (file = "./ventanaMenu.png") 
fondoMenu=Label(root, image = img).place( x=0, y=0)



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
arbol.insert("", END, text="Cliente n°3", iid=17, open=False, values=("Eduardo Molina","26.680.492-6","$550.000"), image=imagenCliente)
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
arbol.insert("", END, text="Cliente 3", iid=9, open=False, values=("Eduardo", "Molina","26.680.492-1","$340.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 4", iid=10, open=False, values=("Susana", "Gomez","10.433.522-5","$200.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 5", iid=31, open=False, values=("Alejandro", "Perez","18.769.066-8","$1.000.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 6", iid=32, open=False, values=("Marcela", "Valenzuela","9.675.192-3","$1.250.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 7", iid=33, open=False, values=("Moises", "Cruz","13.005.382-3","$500.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 8", iid=34, open=False, values=("Angela", "Vera","18.351.461-2","$230.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 9", iid=35, open=False, values=("Antonio", "Alvarez","21.480.890-0","$750.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 10", iid=36, open=False, values=("Manuel", "Estrada","16.002.895-5","$400.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 11", iid=37, open=False, values=("Mauro", "Hernandez","18.329.054-1","$800.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 12", iid=38, open=False, values=("Leticia", "Mora","11.777.803-7","$980.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 13", iid=39, open=False, values=("Alan", "Cortes","15.376.718-1","$320.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 14", iid=40, open=False, values=("Daniela", "Muñoz","21.705.714-0","$175.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 15", iid=41, open=False, values=("Felipe", "Ortiz","24.163.364-0","$250.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 16", iid=42, open=False, values=("Bryan", "Carrasco","19.834.112-6","$435.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 17", iid=43, open=False, values=("Julio", "Martinez","12.972.114-6","$350.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 18", iid=44, open=False, values=("Ulises", "Reyes","20.369.833-5","$125.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 19", iid=45, open=False, values=("Sebastian", "Campos","11.744.612-3","$75.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 20", iid=46, open=False, values=("Mario", "Rojas","30.842.516-9","$190.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 21", iid=47, open=False, values=("Alexis", "Sanchez","32.101.259-0","$245.000"), image=imagenCliente)
arbol.insert("", END, text="Cliente 22", iid=48, open=False, values=("Humberto", "Suazo","25.231.228-5","$120.000"), image=imagenCliente)


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
arbol.move(43,1,16)
arbol.move(44,1,17)
arbol.move(45,1,18)
arbol.move(46,1,19)
arbol.move(47,1,20)
arbol.move(48,1,21)

#sub-opciones funcionarios
arbol.insert("", END, text="Funcionario 1", iid=11, open=False, values=("Cesar ","Mora ", "20377093-6"), image=imagenFuncionario)
arbol.insert("", END, text="Funcionario 2", iid=12, open=False, values=("Theare ","Delgado ", "20225477-2"), image=imagenFuncionario)
arbol.insert("", END, text="Funcionario 3", iid=13, open=False, values=("Diego ","Gonzalez ", "20297405-8"), image=imagenFuncionario)

arbol.move(11,2,0)  
arbol.move(12,2,1)
arbol.move(13,2,2)


#DASHBOARD
imagenOpReal = Image.open("./pie-chart.png")
imagenOpReal =imagenOpReal.resize((18,21),Image.ANTIALIAS)
imagenOpReal = ImageTk.PhotoImage(imagenOpReal)

imagenDinero = Image.open("./profits.png")
imagenDinero =imagenDinero.resize((18,21),Image.ANTIALIAS)
imagenDinero = ImageTk.PhotoImage(imagenDinero)

arbol.insert("", END, text="Dashboard", iid=49, open=False)

#sub-opciones dashboard


#posición
arbol.place(x=30,y=65)
def abrirDepositar(): 
        ventanaDepositar=Toplevel(root)
        ventanaDepositar.title("Depositar")
        ventanaDepositar.geometry("600x400")
        ventanaDepositar.resizable(width=False, height=False)
        global NombreClienteNuevo,RutClienteNuevo,SaldoClienteNuevo,y1,ñ,ñ1,ApellidoClienteNuevo,rutFinal,MontoDestino
        
        def enDeposito():
            global y1,ñ,ñ1
            for persona in listadoPersonas.getLista():
                if (ingresaCuentaDeposito.get()==persona.getRut()):
                    NombreClienteNuevo=persona.getNombre()
                    RutClienteNuevo=persona.getRut()
                    SaldoClienteNuevo=persona.getSaldo()
                    ApellidoClienteNuevo=persona.getApellido()
                    rutFinal=RutClienteNuevo[0:2]+"."+RutClienteNuevo[2:5]+"."+RutClienteNuevo[5:8]+"-"+RutClienteNuevo[8]
                    MontoDestino=ingresaMontoDeposito.get()
                    LargoMonto=len(MontoDestino)                  
                    if LargoMonto==4:
                        MontoFinal="$"+MontoDestino[0:1]+"."+MontoDestino[1:4]
                    if LargoMonto==5:
                        MontoFinal="$"+MontoDestino[0:2]+"."+MontoDestino[2:5]
                    if LargoMonto==6:
                        MontoFinal="$"+MontoDestino[0:3]+"."+MontoDestino[3:6]
                    if LargoMonto==7:
                        MontoFinal="$"+MontoDestino[0:1]+"."+MontoDestino[1:4]+"."+MontoDestino[4:7]
                    persona.setOperacion(operaciones[1])
                    listadoPersonas.agregarDeposito(persona)
                    listadoPersonas.agregarTabla(persona)
                    A.append("Depositar")
                    C.append(Op.getEstado())
                

            arbol.insert("", END, text="Cliente n°"+str(ñ1), iid=y1, open=False, values=(NombreClienteNuevo+" "+ApellidoClienteNuevo,rutFinal,MontoFinal), image=imagenCliente)
            arbol.move(y1,3,ñ)
        

           
           
            global Dep,ListaDep,ListaTo,cont1
            cont1=cont1+1 
            y1=y1+1
            ñ=ñ+1
            ñ1=ñ1+1
            B.append(cont1)
            ListaDep.append(int(ingresaMontoDeposito.get()))
            ListaTo.append(int(ingresaMontoDeposito.get()))
            Dep=Dep+(int(ingresaMontoDeposito.get()))
            ingresaCuentaDeposito.delete(0,"end")
            ventanaDepositar.destroy()
        imagen = PhotoImage (file = "./ventanaDepositar.png") 
        fondo=Label(ventanaDepositar, image = imagen).place( x=0, y=0)
        
        #Entry y Label

        ingresaCuentaDeposito = ttk.Entry(ventanaDepositar,text=rutv)
        ingresaCuentaDeposito.place_configure(x=400, y=220 , width=169, height=17)

        ingresaMontoDeposito = ttk.Entry(ventanaDepositar)
        ingresaMontoDeposito.place_configure(x=400, y=248 , width=169, height=17)


        imagenConfirmaDepositar = Image.open("./confirmaDepositar.png")
        imagenConfirmaDepositar = ImageTk.PhotoImage(imagenConfirmaDepositar)
        botonConfirmarCliente2 = ttk.Button(ventanaDepositar, image= imagenConfirmaDepositar, command = enDeposito)
        botonConfirmarCliente2.place( x=434, y=288)


        ventanaDepositar.mainloop()
def abrirRetirar():
        ventanaRetirar=Toplevel(root)
        ventanaRetirar.title("Retirar")
        ventanaRetirar.geometry("600x400")
        ventanaRetirar.resizable(width=False, height=False)
        global NombreClienteNuevo,RutClienteNuevo,SaldoClienteNuevo,ApellidoClienteNuevo,y1,ñ,ñ1,rutFinal
        def enRetirar():
            global B1,r,r1,r2
            for persona in listadoPersonas.getLista():
                if (ingresaCuentaRetiro.get()==persona.getRut()):
                    NombreClienteNuevo=persona.getNombre()
                    RutClienteNuevo=persona.getRut()
                    SaldoClienteNuevo=persona.getSaldo()
                    ApellidoClienteNuevo=persona.getApellido()
                    rutFinal=RutClienteNuevo[0:2]+"."+RutClienteNuevo[2:5]+"."+RutClienteNuevo[5:8]+"-"+RutClienteNuevo[8]
                    MontoDestino=ingresaMontoRetiro.get()
                    LargoMonto=len(MontoDestino)
                    if LargoMonto==4:
                        MontoFinal="$"+MontoDestino[0:1]+"."+MontoDestino[1:4]
                    if LargoMonto==5:
                        MontoFinal="$"+MontoDestino[0:2]+"."+MontoDestino[2:5]
                    if LargoMonto==6:
                        MontoFinal="$"+MontoDestino[0:3]+"."+MontoDestino[3:6]
                    if LargoMonto==7:
                        MontoFinal="$"+MontoDestino[0:1]+"."+MontoDestino[1:4]+"."+MontoDestino[4:7]

                    A.append("Retirar")
                    C.append(Op.getEstado())
            arbol.insert("", END, text="Cliente n°"+str(r2), iid=r, open=False, values=(NombreClienteNuevo+" "+ApellidoClienteNuevo,rutFinal,MontoFinal), image=imagenCliente)
            arbol.move(r,4,r1)

            global cont2
            global Ret,ListaRet,ListaTo
            r=r+1
            r1=r1+1
            r2=r2+1
            cont2=cont2+1
            B.append(cont2)
            ListaRet.append(int(ingresaMontoRetiro.get()))
            ListaTo.append(int(ingresaMontoRetiro.get()))
            Ret=Ret+(int(ingresaMontoRetiro.get()))   
            ingresaCuentaRetiro.delete(0,"end")
            ventanaRetirar.destroy()

        imagen = PhotoImage (file = "./ventanaDepositar.png") 
        fondo=Label(ventanaRetirar, image = imagen).place( x=0, y=0)
        
        ingresaCuentaRetiro = ttk.Entry(ventanaRetirar,text=rutv)
        ingresaCuentaRetiro.place_configure(x=400, y=220  , width=169, height=17)

        ingresaMontoRetiro = ttk.Entry(ventanaRetirar)
        ingresaMontoRetiro.place_configure(x=400, y=248 , width=169, height=17)


        imagenConfirmaRetirar = Image.open("./confirmaDepositar.png")
        imagenConfirmaRetirar = ImageTk.PhotoImage(imagenConfirmaRetirar)
        botonConfirmarRetiro = ttk.Button(ventanaRetirar, image= imagenConfirmaRetirar, command = enRetirar)
        botonConfirmarRetiro.place( x=434, y=288)


        ventanaRetirar.mainloop()

def abrirTransferir(): 
        ventanaTransferir=Toplevel(root)
        ventanaTransferir.title("Transferir")
        ventanaTransferir.geometry("600x400")
        ventanaTransferir.resizable(width=False, height=False)
        global NombreClienteNuevo,RutClienteNuevo,SaldoClienteNuevo,t,t1,t2,rutFinal,ApellidoClienteNuevo,NombreDestino,ApellidoDestino,MontoDestino,MontoFinal
        

        def enTransferir():
            global t,t1,t2
            global C1  
            global C2
            for persona in listadoPersonas.getLista():
                if (ingresaCuentaTransferir.get()==persona.getRut()):
                    NombreClienteNuevo=persona.getNombre()
                    RutClienteNuevo=persona.getRut()
                    rutFinal=RutClienteNuevo[0:2]+"."+RutClienteNuevo[2:5]+"."+RutClienteNuevo[5:8]+"-"+RutClienteNuevo[8]
                    NombreDestino=ingresaNombreTransferir.get()
                    ApellidoDestino=ingresaApellidoTransferir.get()
                    MontoDestino=ingresaMontoTransferir.get()
                    LargoMonto=len(MontoDestino)
                    #MontoFinal=MontoDestino[0:3]+"."+[3:5]
                    if LargoMonto==4:
                        MontoFinal="$"+MontoDestino[0:1]+"."+MontoDestino[1:4]
                    if LargoMonto==5:
                        MontoFinal="$"+MontoDestino[0:2]+"."+MontoDestino[2:5]
                    if LargoMonto==6:
                        MontoFinal="$"+MontoDestino[0:3]+"."+MontoDestino[3:6]
                    if LargoMonto==7:
                        MontoFinal="$"+MontoDestino[0:1]+"."+MontoDestino[1:4]+"."+MontoDestino[4:7]

                    SaldoClienteNuevo=persona.getSaldo()
                    ApellidoClienteNuevo=persona.getApellido()
                    persona.setOperacion(operaciones[3])
                    
            arbol.insert("", END, text="Cliente n°"+str(t2), iid=t, open=False, values=(NombreClienteNuevo+" "+ApellidoClienteNuevo,rutFinal,MontoFinal+"-------->"+" "+NombreDestino+" "+ApellidoDestino), image=imagenCliente)
            arbol.move(t,5,t1)
                    
            global cont3
            t=t+1
            t1=t1+1
            t2=t2+1
            global Trans,ListaTrans,ListaTo
            cont3=cont3+1
            B.append(cont3)  
            ListaTrans.append(int(ingresaMontoTransferir.get()))
            ListaTo.append(int(ingresaMontoTransferir.get()))
            Trans=Trans+(int(ingresaMontoTransferir.get()))     
            ingresaCuentaTransferir.delete(0,"end")
            ventanaTransferir.destroy()


        imagen = PhotoImage (file = "./ventanaTransferir.png") 
        fondo=Label(ventanaTransferir, image = imagen).place( x=0, y=0)





        ingresaNombreTransferir = ttk.Entry(ventanaTransferir)
        ingresaNombreTransferir.place_configure(x=416, y=133 , width=169, height=17)

        ingresaApellidoTransferir = ttk.Entry(ventanaTransferir)
        ingresaApellidoTransferir.place_configure(x=416, y=160 , width=169, height=17)

        ingresaCorreoTransferir = ttk.Entry(ventanaTransferir)
        ingresaCorreoTransferir.place_configure(x=416, y=190 , width=169, height=17)

        ingresaCuentaTransferir = ttk.Entry(ventanaTransferir,text=rutv)
        ingresaCuentaTransferir.place_configure(x=416, y=218 , width=169, height=17)

        ingresaMontoTransferir = ttk.Entry(ventanaTransferir)
        ingresaMontoTransferir.place_configure(x=417, y=248 , width=169, height=17)

        ingresaBancoTransferir = ttk.Entry(ventanaTransferir)
        ingresaBancoTransferir.place_configure(x=417, y=276 , width=169, height=17)


        imagenConfirmaCliente4 = Image.open("./confirmarPrestamo.png")
        imagenConfirmaCliente4 = ImageTk.PhotoImage(imagenConfirmaCliente4)
        botonConfirmarCliente4 = ttk.Button(ventanaTransferir, image= imagenConfirmaCliente4, command = enTransferir)
        botonConfirmarCliente4.place( x=434, y=316)

        ventanaTransferir.mainloop()
def abrirPrestamo():
        ventanaPrestamo=Toplevel(root)
        ventanaPrestamo.title("Préstamo")
        ventanaPrestamo.geometry("600x400")
        ventanaPrestamo.resizable(width=False, height=False)
        global NombreClienteNuevo,RutClienteNuevo,SaldoClienteNuevo,t,t1,t2,rutFinal,ApellidoClienteNuevo,MontoFinal
    

        def enPrestamo():
            global p,p1,p2
            global C2
            for persona in listadoPersonas.getLista():
                if (ingresaMotivoPrestamo.get()==persona.getRut()):
                    NombreClienteNuevo=persona.getNombre()
                    ApellidoClienteNuevo=persona.getApellido()
                    #NombreDestino=ingresaNombreTransferir.get()
                    #ApellidoDestino=ingresaApellidoTransferir.get()
                    MontoSolicitado=ingresaMontoPrestamo.get()
                    MontoFinal="$"+MontoSolicitado[0:3]+"."+MontoSolicitado[3:6]
                    nCuotas=ingresaCuotaPrestamo.get()
                    persona.setOperacion(operaciones[4])
                    listadoPersonas.agregarPrestamo(persona)
                    listadoPersonas.agregarTabla(persona)
                    
            arbol.insert("", END, text="Cliente n°"+str(p2), iid=p, open=False, values=(NombreClienteNuevo+" "+ApellidoClienteNuevo,MontoFinal,nCuotas), image=imagenCliente)
            arbol.move(p,6,p1)
                    
            global cont4
            global Presta,ListaPresta,ListaTo
            p=p+1
            p1=p1+1
            p2=p2+1
            cont4=cont4+1
            B.append(cont4)  
            ListaPresta.append(int(ingresaMontoPrestamo.get()))
            ListaTo.append(int(ingresaMontoPrestamo.get()))
            Presta=Presta+(int(ingresaMontoPrestamo.get()))
            ingresaCuotaPrestamo.delete(0,"end")
            ingresaMontoPrestamo.delete(0,"end")
            ventanaPrestamo.destroy()


        imagen = PhotoImage (file = "./ventanaPrestamo2.png") 
        fondo=Label(ventanaPrestamo, image = imagen).place( x=0, y=0)


        ingresaMotivoPrestamo = ttk.Entry(ventanaPrestamo)
        ingresaMotivoPrestamo.place_configure(x=416, y=223 , width=169, height=17)

        ingresaMontoPrestamo = ttk.Combobox(ventanaPrestamo,values=("$150.000","$300.000","$600.000"),textvariable=prestamosol)
        ingresaMontoPrestamo.place_configure(x=416, y=249 , width=169, height=17)
        ingresaCuotaPrestamo = ttk.Combobox(ventanaPrestamo,values=("3","6","9"),textvariable=cantidadcuotas)
        ingresaCuotaPrestamo.place_configure(x=416, y=276 , width=169, height=17)
        

        imagenConfirmaCliente5 = Image.open("./confirmarPrestamo.png")
        imagenConfirmaCliente5 = ImageTk.PhotoImage(imagenConfirmaCliente5)
        botonConfirmarCliente5 = ttk.Button(ventanaPrestamo, image= imagenConfirmaCliente5, command = enPrestamo)
        botonConfirmarCliente5.place( x=435, y=315)
        ventanaPrestamo.mainloop()
def abrirGrafico():
        ventanaGrafico=Toplevel(root)
        ventanaGrafico.title("Análisis estadísticos")
        ventanaGrafico.geometry("950x500")
        ventanaGrafico.resizable(width=False, height=False)


        imagen = PhotoImage (file = "./ventanaAnalisis2.png") 
        fondo=Label(ventanaGrafico, image = imagen).place( x=0, y=0)

        def MostrarGrafico():
            global cont1,cont2,cont3,cont4
            global cont1,cont2,cont3,cont4,contadorfinal
            contadorfinal=contadorfinal+cont1+cont2+cont3+cont4
            Graficos=ttk.Label(ventanaGrafico,text=contadorfinal)
            Graficos.place(x=87,y=278, width=136, height=15)
            contadorfinal=0
            if(cont4==0 and cont1>=1 and cont2>=1 and cont3>=1):
                fig=plt.figure("Cantidad de operaciones realizadas")

                plt.title("Gráfico de operaciones realizadas")
                
                operaciones = [cont1, cont2, cont3]
                label = ["Depositar", "Retirar", "Transferir"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                grafico=plt.show()

            elif(cont4>=1 and cont1==0 and cont2>=1 and cont3>=1):
                fig=plt.figure("Cantidad de operaciones realizadas")

                plt.title("Gráfico de operaciones realizadas")

                operaciones = [cont3, cont2, cont4]
                label = ["Transferir", "Retirar", "Préstamo"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()

            elif(cont4>=1 and cont1>=1 and cont3>=1 and cont2==0):
                fig=plt.figure("Cantidad de operaciones realizadas")

                plt.title("Gráfico de operaciones realizadas")
                
                operaciones = [cont1,cont3,cont4]
                label = ["Depositar", "Transferir", "Préstamo"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%", colors= colores)
                plt.show()

            elif(cont4>=1 and cont1>=1 and cont2>=1 and cont3==0):
                fig=plt.figure("Cantidad de operaciones realizadas")

                plt.title("Gráfico de operaciones realizadas")
               
                operaciones = [cont1, cont2, cont4]
                label = ["Depositar", "Retirar", "Préstamo"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()

            elif(cont4>=1 and cont1>=1 and cont2>=1 and cont3>=1):
                fig=plt.figure("Cantidad de operaciones realizadas")

                plt.title("Gráfico de operaciones realizadas")
                
                operaciones = [cont1, cont3, cont2, cont4]
                label = ["Depositar", "Transferir", "Retirar", "Préstamo"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()

            elif(cont4>=0 and cont1>=1 and cont2>=1 and cont3>=0):
                fig=plt.figure("Cantidad de operaciones realizadas")

                plt.title("Gráfico de operaciones realizadas")
                
                operaciones = [cont1, cont2, ]
                label = ["Depositar", "Retirar"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()

            elif(cont4>=1 and cont1==0 and cont2==0 and cont3==0):
                fig=plt.figure("Cantidad de operaciones realizadas")

                plt.title("Gráfico de operaciones realizadas")
                
                operaciones = [cont4]
                label = ["Préstamo"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()
            elif(cont4==0 and cont1>=1 and cont2==0 and cont3==0):
                fig=plt.figure("Cantidad de operaciones realizadas")

                plt.title("Gráfico de operaciones realizadas")
                
                operaciones = [cont1]
                label = ["Depositar"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()
            elif(cont4==0 and cont1==0 and cont2>=1 and cont3==0):
                fig=plt.figure("Cantidad de operaciones realizadas")

                plt.title("Gráfico de operaciones realizadas")
      
                operaciones = [cont2]
                label = ["Retirar"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()
            elif(cont4==0 and cont1==0 and cont2==0 and cont3>=1):
                fig=plt.figure("Cantidad de operaciones realizadas")

                plt.title("Gráfico de operaciones realizadas")

                operaciones = [cont3]
                label = ["Transferir"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()
        def MovimientoDinero():
            global Dep,Ret,Trans,Presta,contadorfinal2
            contadorfinal2=contadorfinal2+Dep+Ret+Trans+Presta
            
            LargoContadorFinal=len(str(contadorfinal2))

            if LargoContadorFinal==7:
                contadorfinal5="$"+str(contadorfinal2)[0:1]+"."+str(contadorfinal2)[1:4]+"."+str(contadorfinal2)[4:7]              
            if LargoContadorFinal==8:
                contadorfinal5="$"+str(contadorfinal2)[0:2]+"."+str(contadorfinal2)[2:5]+"."+str(contadorfinal2)[5:8] 
            if LargoContadorFinal==9:
                contadorfinal5="$"+str(contadorfinal2)[0:3]+"."+str(contadorfinal2)[3:6]+"."+str(contadorfinal2)[6:9] 
                  
            Dinero=ttk.Label(ventanaGrafico,text=contadorfinal5)
            Dinero.place(x=387,y=278, width=136, height=15)
            contadorfinal2=0

            if(Presta==0 and Dep>=1 and Ret>=1 and Trans>=1):

                fig=plt.figure("Cantidad de dinero por operaciones")

                plt.title("Gráfico de dinero por operación")
            
                plt.ylabel('Dinero')
            
                operaciones = [Dep, Ret, Trans]
                label = ["Depositar", "Retirar", "Transferir"]
                plt.bar(label, operaciones)

                plt.show()
            elif(Presta==0 and Dep>=1 and Ret>=1 and Trans>=0):

                fig=plt.figure("Cantidad de dinero por operaciones")

                plt.title("Gráfico de dinero por operación")
                
                plt.ylabel('Dinero')
                
                operaciones = [Dep, Ret]
                label = ["Depositar", "Retirar"]
                plt.bar(label, operaciones)

                plt.show()
            elif(Presta>=1 and Dep==0 and Ret>=1 and Trans>=1):


                fig=plt.figure("Cantidad de dinero por operaciones")

                plt.title("Gráfico de dinero por operación")
                
                plt.ylabel('Dinero')
                
                operaciones = [Presta, Ret, Trans]
                label = ["Prestamo", "Retirar", "Transferir"]
                plt.bar(label, operaciones)

                plt.show()
            elif(Presta>=1 and Dep>=1 and Ret==0 and Trans>=1):

                fig=plt.figure("Cantidad de dinero por operaciones")

                plt.title("Gráfico de dinero por operación")

                plt.ylabel('Dinero')
                
                operaciones = [Presta,Dep, Trans]
                label = ["Prestamo", "Depositar", "Transferir"]
                plt.bar(label, operaciones)
                plt.show()
            elif(Presta>=1 and Dep>=1 and Ret>=1 and Trans==0):

                fig=plt.figure("Cantidad de dinero por operaciones")

                plt.title("Gráfico de dinero por operación")
                
                operaciones = [Presta,Dep, Ret]
                plt.ylabel('Dinero')
                label = ["Prestamo", "Depositar", "Retirar"]
                plt.bar(label, operaciones)

                plt.show()
            elif(Presta>=1 and Dep>=1 and Ret>=1 and Trans>=1):
                
                fig=plt.figure("Cantidad de dinero por operaciones")

                plt.title("Gráfico de dinero por operación")
            
                operaciones = [Presta,Dep,Ret, Trans]
                plt.ylabel('Dinero')
                label = ["Prestamo", "Depositar","Retirar", "Transferir"]
                plt.bar(label, operaciones)

                plt.show()
            elif(Presta>=1 and Dep==0 and Ret==0 and Trans==0):

                fig=plt.figure("Cantidad de dinero por operaciones")

                plt.title("Gráfico de dinero por operación")

                plt.ylabel('Dinero')
                operaciones = [Presta]
                label = ["Prestamo"]
                plt.bar(label, operaciones)
                plt.show()
            elif(Presta==0 and Dep>=1 and Ret==0 and Trans==0):

                fig=plt.figure("Cantidad de dinero por operaciones")

                plt.title("Gráfico de dinero por operación")

                plt.ylabel('Dinero')
                operaciones = [Dep]
                label = ["Depositar"]
                plt.bar(label, operaciones)
                plt.show()
            elif(Presta==0 and Dep==0 and Ret>=1 and Trans==0):

                fig=plt.figure("Cantidad de dinero por operaciones")

                plt.title("Gráfico de dinero por operación")

                plt.ylabel('Dinero')
                operaciones = [Ret]
                label = ["Retirar"]
                plt.bar(label, operaciones)
                plt.show()
            elif(Presta==0 and Dep==0 and Ret==0 and Trans>=1):

                fig=plt.figure("Cantidad de dinero por operaciones")
                
                plt.title("Gráfico de dinero por operación")

                plt.ylabel('Dinero')
                operaciones = [Trans]
                label = ["Transferir"]
                plt.bar(label, operaciones)
                plt.show()


        def CalculosMat():
            global contadorfinal3,contadorfinal4,Dep,Ret,Trans,Presta,cont1,cont2,cont3,cont4
            global contadorDep,contadorRet,contadorTrans,contadorPresta
            global ListaDep,ListaRet,ListaTrans,ListaPresta,ListaTo
            #Definiendo contadores dinero separado y juntos
            contadorfinal3=contadorfinal3+Dep+Ret+Trans+Presta
            contadorDep=contadorDep+Dep
            contadorRet=contadorRet+Ret
            contadorTrans=contadorTrans+Trans
            contadorPresta=contadorPresta+Presta
            #Definiendo contadores personjas separado y juntos
            contadorfinal4=contadorfinal4+cont1+cont2+cont3+cont4
            media=int(contadorfinal3/contadorfinal4)
            

            if(cont1>=1 and cont2>=1 and cont3>=1 and cont4>=1):
                #Media
                mediaDep=int(contadorDep/cont1)
                mediaRet=int(contadorRet/cont2)
                mediaTrans=int(contadorTrans/cont3)
                mediaPresta=int(contadorPresta/cont4)

                #             label media
                mediaDep=ttk.Label(ventanaGrafico,text=mediaDep)
                mediaDep.place(x=195,y=400, width=140, height=16)
                mediaRet=ttk.Label(ventanaGrafico,text=mediaRet)
                mediaRet.place(x=195,y=424, width=140, height=16)
                mediaTrans=ttk.Label(ventanaGrafico,text=mediaTrans)
                mediaTrans.place(x=195,y=445, width=140, height=16)
                mediaPresta=ttk.Label(ventanaGrafico,text=mediaPresta)
                mediaPresta.place(x=195,y=468, width=140, height=16)
                #Mediana
                medianaDep=(stats.median(ListaDep))
                medianaRet=(stats.median(ListaRet))
                medianaTrans=(stats.median(ListaTrans))
                medianaPresta=(stats.median(ListaPresta))

                medianaDepo=ttk.Label(ventanaGrafico,text=medianaDep)
                medianaDepo.place(x=359,y=400, width=135, height=16)
                medianaReti=ttk.Label(ventanaGrafico,text=medianaRet)
                medianaReti.place(x=359,y=424, width=135, height=16)
                medianaTransf=ttk.Label(ventanaGrafico,text=medianaTrans)
                medianaTransf.place(x=359,y=445, width=135, height=16)
                medianaPrestam=ttk.Label(ventanaGrafico,text=medianaPresta)
                medianaPrestam.place(x=359,y=468, width=135, height=16)
                #Moda
                modaDep=(stats.mode(ListaDep))
                modaRet=(stats.mode(ListaRet))
                modaTrans=(stats.mode(ListaTrans))
                modaPresta=(stats.mode(ListaPresta))

                modaDepo=ttk.Label(ventanaGrafico,text= modaDep)
                modaDepo.place(x=518,y=400, width=113, height=16)
                modaReti=ttk.Label(ventanaGrafico,text= modaRet)
                modaReti.place(x=518,y=424, width=113, height=16)
                modaTransf=ttk.Label(ventanaGrafico,text= modaTrans)
                modaTransf.place(x=518,y=445, width=113, height=16)
                modaPrestam=ttk.Label(ventanaGrafico,text= modaPresta)
                modaPrestam.place(x=518,y=468, width=113, height=16)
                #desv estandar
                DesvDep=(stats.mode(ListaDep))
                DesvRet=(stats.mode(ListaRet))
                DesvTrans=(stats.mode(ListaTrans))
                DesvPresta=(stats.mode(ListaPresta))

                DesDepo=ttk.Label(ventanaGrafico,text= DesvDep)
                DesDepo.place(x=654,y=400, width=240, height=16)
                DesReti=ttk.Label(ventanaGrafico,text= DesvRet)
                DesReti.place(x=654,y=424, width=240, height=16)
                DesTransf=ttk.Label(ventanaGrafico,text= DesvTrans)
                DesTransf.place(x=654,y=445, width=240, height=16)
                DesPrestam=ttk.Label(ventanaGrafico,text= DesvPresta)
                DesPrestam.place(x=654,y=468, width=240, height=16)
            #-------------LISTO-----------------
            elif(cont1>=1 and cont2>=1 and cont3>=0 and cont4>=0):
                #Media
                mediaDep=int(contadorDep/cont1)
                mediaRet=int(contadorRet/cont2)

                #             label media
                mediaDep=ttk.Label(ventanaGrafico,text=mediaDep)
                mediaDep.place(x=195,y=400, width=140, height=16)
                mediaRet=ttk.Label(ventanaGrafico,text=mediaRet)
                mediaRet.place(x=195,y=424, width=140, height=16)

                #Mediana
                medianaDep=(stats.median(ListaDep))
                medianaRet=(stats.median(ListaRet))


                medianaDepo=ttk.Label(ventanaGrafico,text=medianaDep)
                medianaDepo.place(x=359,y=400, width=135, height=16)
                medianaReti=ttk.Label(ventanaGrafico,text=medianaRet)
                medianaReti.place(x=359,y=424, width=135, height=16)

                #Moda
                modaDep=(stats.mode(ListaDep))
                modaRet=(stats.mode(ListaRet))


                modaDepo=ttk.Label(ventanaGrafico,text= modaDep)
                modaDepo.place(x=518,y=400, width=113, height=16)
                modaReti=ttk.Label(ventanaGrafico,text= modaRet)
                modaReti.place(x=518,y=424, width=113, height=16)

                #desv estandar
                DesvDep=(stats.mode(ListaDep))
                DesvRet=(stats.mode(ListaRet))

                DesDepo=ttk.Label(ventanaGrafico,text= DesvDep)
                DesDepo.place(x=654,y=400, width=240, height=16)
                DesReti=ttk.Label(ventanaGrafico,text= DesvRet)
                DesReti.place(x=654,y=424, width=240, height=16)

            #-------------LISTO-----------------
            elif(cont1==0 and cont2>=1 and cont3>=1 and cont4>=1):
                #Media
                mediaRet=int(contadorRet/cont2)
                mediaTrans=int(contadorTrans/cont3)
                mediaPresta=int(contadorPresta/cont4)

                mediaRet=ttk.Label(ventanaGrafico,text=mediaRet)
                mediaRet.place(x=195,y=424, width=140, height=16)
                mediaTrans=ttk.Label(ventanaGrafico,text=mediaTrans)
                mediaTrans.place(x=195,y=445, width=140, height=16)
                mediaPresta=ttk.Label(ventanaGrafico,text=mediaPresta)
                mediaPresta.place(x=195,y=468, width=140, height=16)
                #Mediana
                medianaRet=(stats.median(ListaRet))
                medianaTrans=(stats.median(ListaTrans))
                medianaPresta=(stats.median(ListaPresta))

                medianaReti=ttk.Label(ventanaGrafico,text=medianaRet)
                medianaReti.place(x=359,y=424, width=135, height=16)
                medianaTransf=ttk.Label(ventanaGrafico,text=medianaTrans)
                medianaTransf.place(x=359,y=445, width=135, height=16)
                medianaPrestam=ttk.Label(ventanaGrafico,text=medianaPresta)
                medianaPrestam.place(x=359,y=468, width=135, height=16)
                #Moda
                modaRet=(stats.mode(ListaRet))
                modaTrans=(stats.mode(ListaTrans))
                modaPresta=(stats.mode(ListaPresta))

                modaReti=ttk.Label(ventanaGrafico,text= modaRet)
                modaReti.place(x=518,y=424, width=113, height=16)
                modaTransf=ttk.Label(ventanaGrafico,text= modaTrans)
                modaTransf.place(x=518,y=445, width=113, height=16)
                modaPrestam=ttk.Label(ventanaGrafico,text= modaPresta)
                modaPrestam.place(x=518,y=468, width=113, height=16)
                #Desv. Estandar
                DesvRet=(stats.mode(ListaRet))
                DesvTrans=(stats.mode(ListaTrans))
                DesvPresta=(stats.mode(ListaPresta))

                DesReti=ttk.Label(ventanaGrafico,text= DesvRet)
                DesReti.place(x=654,y=424, width=240, height=16)
                DesTransf=ttk.Label(ventanaGrafico,text= DesvTrans)
                DesTransf.place(x=654,y=445, width=240, height=16)
                DesPrestam=ttk.Label(ventanaGrafico,text= DesvPresta)
                DesPrestam.place(x=654,y=468, width=240, height=16)

                #listo 

            elif(cont1>=1 and cont2==0 and cont3>=1 and cont4>=1):
                #Media
                mediaDep=int(contadorDep/cont1)
                mediaTrans=int(contadorTrans/cont3)
                mediaPresta=int(contadorPresta/cont4)

                mediaDep=ttk.Label(ventanaGrafico,text=mediaDep)
                mediaDep.place(x=195,y=400, width=140, height=16)
                mediaTrans=ttk.Label(ventanaGrafico,text=mediaTrans)
                mediaTrans.place(x=195,y=445, width=140, height=16)
                mediaPresta=ttk.Label(ventanaGrafico,text=mediaPresta)
                mediaPresta.place(x=195,y=468, width=140, height=16)

                #Mediana
                medianaDep=(stats.median(ListaDep))
                medianaTrans=(stats.median(ListaTrans))
                medianaPresta=(stats.median(ListaPresta))

                medianaDepo=ttk.Label(ventanaGrafico,text=medianaDep)
                medianaDepo.place(x=359,y=400, width=135, height=16)
                medianaTransf=ttk.Label(ventanaGrafico,text=medianaTrans)
                medianaTransf.place(x=359,y=445, width=135, height=16)
                medianaPrestam=ttk.Label(ventanaGrafico,text=medianaPresta)
                medianaPrestam.place(x=359,y=468, width=135, height=16)
                #Moda
                modaDep=(stats.mode(ListaDep))
                modaTrans=(stats.mode(ListaTrans))
                modaPresta=(stats.mode(ListaPresta))

                modaDepo=ttk.Label(ventanaGrafico,text= modaDep)
                modaDepo.place(x=518,y=400, width=113, height=16)
                modaTransf=ttk.Label(ventanaGrafico,text= modaTrans)
                modaTransf.place(x=518,y=445, width=113, height=16)
                modaPrestam=ttk.Label(ventanaGrafico,text= modaPresta)
                modaPrestam.place(x=518,y=468, width=113, height=16)
                #Desv. Estandar
                DesvDep=(stats.mode(ListaDep))
                DesvTrans=(stats.mode(ListaTrans))
                DesvPresta=(stats.mode(ListaPresta))

                DesDepo=ttk.Label(ventanaGrafico,text= DesvDep)
                DesDepo.place(x=654,y=400, width=240, height=16)
                DesTransf=ttk.Label(ventanaGrafico,text= DesvTrans)
                DesTransf.place(x=654,y=445, width=240, height=16)
                DesPrestam=ttk.Label(ventanaGrafico,text= DesvPresta)
                DesPrestam.place(x=654,y=468, width=240, height=16)

                #listo

            elif(cont1>=1 and cont2>=1 and cont3==0 and cont4>=1):
                mediaDep=int(contadorDep/cont1)
                mediaRet=int(contadorRet/cont2)
                mediaPresta=int(contadorPresta/cont4)

                mediaDep=ttk.Label(ventanaGrafico,text=mediaDep)
                mediaDep.place(x=195,y=400, width=140, height=16)
                mediaRet=ttk.Label(ventanaGrafico,text=mediaRet)
                mediaRet.place(x=195,y=424, width=140, height=16)
                mediaPresta=ttk.Label(ventanaGrafico,text=mediaPresta)
                mediaPresta.place(x=195,y=468, width=140, height=16)
                #Mediana
                medianaDep=(stats.median(ListaDep))
                medianaRet=(stats.median(ListaRet))
                medianaPresta=(stats.median(ListaPresta))

                medianaDepo=ttk.Label(ventanaGrafico,text=medianaDep)
                medianaDepo.place(x=359,y=400, width=135, height=16)
                medianaReti=ttk.Label(ventanaGrafico,text=medianaRet)
                medianaReti.place(x=359,y=424, width=135, height=16)
                medianaPrestam=ttk.Label(ventanaGrafico,text=medianaPresta)
                medianaPrestam.place(x=359,y=468, width=135, height=16)
                #Labels Moda
                modaDep=(stats.mode(ListaDep))
                modaRet=(stats.mode(ListaRet))
                modaPresta=(stats.mode(ListaPresta))

                modaDepo=ttk.Label(ventanaGrafico,text= modaDep)
                modaDepo.place(x=518,y=400, width=113, height=16)
                modaReti=ttk.Label(ventanaGrafico,text= modaRet)
                modaReti.place(x=518,y=424, width=113, height=16)
                modaPrestam=ttk.Label(ventanaGrafico,text= modaPresta)
                modaPrestam.place(x=518,y=468, width=113, height=16)
                #desv estandar
                DesvDep=(stats.mode(ListaDep))
                DesvRet=(stats.mode(ListaRet))
                DesvPresta=(stats.mode(ListaPresta))

                DesDepo=ttk.Label(ventanaGrafico,text= DesvDep)
                DesDepo.place(x=654,y=400, width=240, height=16)
                DesReti=ttk.Label(ventanaGrafico,text= DesvRet)
                DesReti.place(x=654,y=424, width=240, height=16)
                DesPrestam=ttk.Label(ventanaGrafico,text= DesvPresta)
                DesPrestam.place(x=654,y=468, width=240, height=16)
                #listo

            elif(cont1>=1 and cont2>=1 and cont3>=1 and cont4==0):
                mediaDep=int(contadorDep/cont1)
                mediaRet=int(contadorRet/cont2)
                mediaTrans=int(contadorTrans/cont3)

                mediaDep=ttk.Label(ventanaGrafico,text=mediaDep)
                mediaDep.place(x=195,y=400, width=140, height=16)
                mediaRet=ttk.Label(ventanaGrafico,text=mediaRet)
                mediaRet.place(x=195,y=424, width=140, height=16)
                mediaTrans=ttk.Label(ventanaGrafico,text=mediaTrans)
                mediaTrans.place(x=195,y=445, width=140, height=16)
                #Mediana
                medianaDep=(stats.median(ListaDep))
                medianaRet=(stats.median(ListaRet))
                medianaTrans=(stats.median(ListaTrans))

                medianaDepo=ttk.Label(ventanaGrafico,text=medianaDep)
                medianaDepo.place(x=359,y=400, width=135, height=16)
                medianaReti=ttk.Label(ventanaGrafico,text=medianaRet)
                medianaReti.place(x=359,y=424, width=135, height=16)
                medianaTransf=ttk.Label(ventanaGrafico,text=medianaTrans)
                medianaTransf.place(x=359,y=445, width=135, height=16)
                #Moda
                modaDep=(stats.mode(ListaDep))
                modaRet=(stats.mode(ListaRet))
                modaTrans=(stats.mode(ListaTrans))

                modaDepo=ttk.Label(ventanaGrafico,text= modaDep)
                modaDepo.place(x=518,y=400, width=113, height=16)
                modaReti=ttk.Label(ventanaGrafico,text= modaRet)
                modaReti.place(x=518,y=424, width=113, height=16)
                modaTransf=ttk.Label(ventanaGrafico,text= modaTrans)
                modaTransf.place(x=518,y=445, width=113, height=16)
                #desv estandar
                DesvDep=(stats.mode(ListaDep))
                DesvRet=(stats.mode(ListaRet))
                DesvTrans=(stats.mode(ListaTrans))

                DesDepo=ttk.Label(ventanaGrafico,text= DesvDep)
                DesDepo.place(x=654,y=400, width=240, height=16)
                DesReti=ttk.Label(ventanaGrafico,text= DesvRet)
                DesReti.place(x=654,y=424, width=240, height=16)
                DesTransf=ttk.Label(ventanaGrafico,text= DesvTrans)
                DesTransf.place(x=654,y=445, width=240, height=16)
                #listo
            elif(cont1>=1 and cont2==0 and cont3==0 and cont4==0):
                mediaDep=int(contadorDep/cont1)
                mediaDep=ttk.Label(ventanaGrafico,text=mediaDep)
                mediaDep.place(x=195,y=400, width=140, height=16)
                #Mediana
                medianaDep=(stats.median(ListaDep))
                medianaDepo=ttk.Label(ventanaGrafico,text=medianaDep)
                medianaDepo.place(x=359,y=400, width=135, height=16)
                #Moda
                modaDep=(stats.mode(ListaDep))
                modaDepo=ttk.Label(ventanaGrafico,text= modaDep)
                modaDepo.place(x=518,y=400, width=113, height=16)
                #desv estandar
                DesvDep=(stats.mode(ListaDep))
                DesDepo=ttk.Label(ventanaGrafico,text= DesvDep)
                DesDepo.place(x=654,y=400, width=240, height=16)


            elif(cont1==0 and cont2>=1 and cont3==0 and cont4==0):
                mediaRet=int(contadorRet/cont2)
                mediaRet=ttk.Label(ventanaGrafico,text=mediaRet)
                mediaRet.place(x=195,y=424, width=140, height=16)
                #Mediana
                medianaRet=(stats.median(ListaRet))
                medianaReti=ttk.Label(ventanaGrafico,text=medianaRet)
                medianaReti.place(x=359,y=424, width=135, height=16)
                #Moda
                modaRet=(stats.mode(ListaRet))
                modaReti=ttk.Label(ventanaGrafico,text= modaRet)
                modaReti.place(x=518,y=424, width=113, height=16)
                #desv estandar
                DesvRet=(stats.mode(ListaRet))
                DesReti=ttk.Label(ventanaGrafico,text= DesvRet)
                DesReti.place(x=654,y=424, width=240, height=16)
            elif(cont1==0 and cont2==0 and cont3>=1 and cont4==0):
                mediaTrans=int(contadorTrans/cont3)
                mediaTrans=ttk.Label(ventanaGrafico,text=mediaTrans)
                mediaTrans.place(x=195,y=445, width=140, height=16)
                #Mediana
                medianaTrans=(stats.median(ListaTrans))
                medianaTransf=ttk.Label(ventanaGrafico,text=medianaTrans)
                medianaTransf.place(x=359,y=445, width=135, height=16)
                #Moda
                modaTrans=(stats.mode(ListaTrans))
                modaTransf=ttk.Label(ventanaGrafico,text= modaTrans)
                modaTransf.place(x=518,y=445, width=113, height=16)
                #Desv estandar
                DesvTrans=(stats.mode(ListaTrans))
                DesTransf=ttk.Label(ventanaGrafico,text= DesvTrans)
                DesTransf.place(x=654,y=445, width=240, height=16)

            elif(cont1==0 and cont2==0 and cont3==0 and cont4>=1):
                mediaPresta=int(contadorPresta/cont4)
                mediaPresta=ttk.Label(ventanaGrafico,text=mediaPresta)
                mediaPresta.place(x=195,y=468, width=140, height=16)
                #Mediana
                medianaPresta=(stats.median(ListaPresta))
                medianaPrestam=ttk.Label(ventanaGrafico,text=medianaPresta)
                medianaPrestam.place(x=359,y=468, width=135, height=16)
                #Moda
                modaPresta=(stats.mode(ListaPresta))
                modaPrestam=ttk.Label(ventanaGrafico,text= modaPresta)
                modaPrestam.place(x=518,y=468, width=113, height=16)
                #desv estandar
                DesvPresta=(stats.mode(ListaPresta))
                DesPrestam=ttk.Label(ventanaGrafico,text= DesvPresta)
                DesPrestam.place(x=654,y=468, width=240, height=16)

            contadorfinal3=0
            contadorfinal4=0
            media=0
            contadorDep=0
            contadorRet=0
            contadorTrans=0
            contadorPresta=0

        #gráfico por operaciones
        imgMostrarGraficoOp = Image.open("./operacionesRealizadas.png")
        imgMostrarGraficoOp = ImageTk.PhotoImage(imgMostrarGraficoOp)
        botonMostrarGrafico = ttk.Button(ventanaGrafico, image= imgMostrarGraficoOp, command = MostrarGrafico)
        botonMostrarGrafico.place( x=88, y=107)

        #gráfico por dinero
        imgMostrarGraficoDin = Image.open("./dineroTrabajado.png")
        imgMostrarGraficoDin = ImageTk.PhotoImage(imgMostrarGraficoDin)
        botonMostrarDinero = ttk.Button(ventanaGrafico, image= imgMostrarGraficoDin, command = MovimientoDinero)
        botonMostrarDinero.place( x=385, y=107)



        #mostrar todo
        imgMostrarTodo = Image.open("./mostrarDatos.png")
        imgMostrarTodo = ImageTk.PhotoImage(imgMostrarTodo)
        botonMostrarCalculos = ttk.Button(ventanaGrafico,image=imgMostrarTodo, command = CalculosMat)
        botonMostrarCalculos.place( x=678, y=107)
        ventanaGrafico.mainloop()
def itemSeleccionado(event):
    for selected_item in arbol.selection():
        item = arbol.item(selected_item)

        valor = item["values"]
        nombreOpcion = item["text"]
        img = item["image"]
        abierto = item["open"]

        iid=arbol.focus()

        if iid=="3":
            global NombreClienteNuevo,RutClienteNuevo,SaldoClienteNuevo
            abrirDepositar()
        if iid=="4":
            global NombreClienteNuevo,RutClienteNuevo,SaldoClienteNuevo
            abrirRetirar()
        if iid=="5":
            global NombreClienteNuevo,RutClienteNuevo,SaldoClienteNuevo
            abrirTransferir()
        if iid=="6":
            global NombreClienteNuevo,RutClienteNuevo,SaldoClienteNuevo
            abrirPrestamo()
        if iid=="49":
            abrirGrafico()
        
            



        #IF para los Clientes de DEPOSITAR
        if iid=="15":
             messagebox.showinfo("Datos Deposito n°1", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="16":
             messagebox.showinfo("Datos Deposito n°2", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="17":
             messagebox.showinfo("Datos Deposito n°3", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="18":
             messagebox.showinfo("Datos Deposito n°4", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="52":
            messagebox.showinfo("Datos Deposito n°5", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="53":
            messagebox.showinfo("Datos Deposito n°6", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="54":
            messagebox.showinfo("Datos Deposito n°7", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="55":
            messagebox.showinfo("Datos Deposito n°8", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))

        #IF para los Clientes de RETIRAR
        if iid=="19":
             messagebox.showinfo("Datos Retiro n°1", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="20":
             messagebox.showinfo("Datos Retiro n°2", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="21":
             messagebox.showinfo("Datos Retiro n°3", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="22":
             messagebox.showinfo("Datos Retiro n°4", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="56":
            messagebox.showinfo("Datos Retiro n°5", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="57":
            messagebox.showinfo("Datos Retiro n°6", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="58":
            messagebox.showinfo("Datos Retiro n°7", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="59":
            messagebox.showinfo("Datos Retiro n°8", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))

        #IF para los Clientes de TRANSFERENCIA
        if iid=="23":
             messagebox.showinfo("Datos Transferencia n°1", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2])+"--------> "+valor[3])
        if iid=="24":
             messagebox.showinfo("Datos Transferencia n°2", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2])+"--------> "+valor[3])
        if iid=="25":
             messagebox.showinfo("Datos Transferencia n°3", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2])+"--------> "+valor[3])
        if iid=="26":
             messagebox.showinfo("Datos Transferencia n°4", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2])+"--------> "+valor[3])
        if iid=="60":
            messagebox.showinfo("Datos Transferencia n°5", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="61":
            messagebox.showinfo("Datos Transferencia n°6", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="62":
            messagebox.showinfo("Datos Transferencia n°7", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        if iid=="63":
            messagebox.showinfo("Datos Transferencia n°8", " Nombre: "+valor[0]+"\n Rut: "+str(valor[1])+"\n Monto: "+str(valor[2]))
        #IF para los Clientes de PRÉSTAMO
        if iid=="27":
             messagebox.showinfo("Datos Préstamo n°1", " Nombre: "+valor[0]+"\n Monto solicitado: "+str(valor[1])+"\n N° Cuotas: "+str(valor[2]))
        if iid=="28":
             messagebox.showinfo("Datos Préstamo n°2", " Nombre: "+valor[0]+"\n Monto solicitado: "+str(valor[1])+"\n N° Cuotas: "+str(valor[2]))
        if iid=="29":
             messagebox.showinfo("Datos Préstamo n°3", " Nombre: "+valor[0]+"\n Monto solicitado: "+str(valor[1])+"\n N° Cuotas: "+str(valor[2]))
        if iid=="30":
             messagebox.showinfo("Datos Préstamo n°4", " Nombre: "+valor[0]+"\n Monto solicitado: "+str(valor[1])+"\n N° Cuotas: "+str(valor[2]))
        if iid=="64":
            messagebox.showinfo("Datos Préstamo n°5", " Nombre: "+valor[0]+"\n Monto solicitado: "+str(valor[1])+"\n N° Cuotas: "+str(valor[2]))
        if iid=="65":
            messagebox.showinfo("Datos Préstamo n°6", " Nombre: "+valor[0]+"\n Monto solicitado: "+str(valor[1])+"\n N° Cuotas: "+str(valor[2]))
        if iid=="66":
            messagebox.showinfo("Datos Préstamo n°8", " Nombre: "+valor[0]+"\n Monto solicitado: "+str(valor[1])+"\n N° Cuotas: "+str(valor[2]))
        if iid=="67":
            messagebox.showinfo("Datos Préstamo n°9", " Nombre: "+valor[0]+"\n Monto solicitado: "+str(valor[1])+"\n N° Cuotas: "+str(valor[2]))



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
        if iid=="43":
            messagebox.showinfo("Datos Cliente 17", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="44":
            messagebox.showinfo("Datos Cliente 18", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="45":
            messagebox.showinfo("Datos Cliente 19", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="46":
            messagebox.showinfo("Datos Cliente 20", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="47":
            messagebox.showinfo("Datos Cliente 21", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))
        if iid=="48":
            messagebox.showinfo("Datos Cliente 22", " Nombre: " +valor[0]+"\n Apellido: "+valor[1]+"\n Rut: "+str(valor[2])+"\n Saldo: "+str(valor[3]))


arbol.bind("<Double-1>", itemSeleccionado)

root.mainloop()