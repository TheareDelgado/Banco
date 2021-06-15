from pathlib import WindowsPath
import tkinter 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Button
from tkinter import messagebox
from numpy import mat
from Cliente import *
from Persona import *
from dispensador import *
from Banco import *
from Operaciones import *
from Prestamo import *
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
from Funcionario import *
import statistics as stats



#Creando banco

#Creando personas
Op=Operaciones()
Prest=Prestamo()
p1=Persona()
p2=Persona()
p3=Persona()
p4=Persona()

#creando funcionarios

p5=Funcionario()
p6=Funcionario()
p7=Funcionario()
p8=Funcionario()

#falta administrar las claves de cada usuario
p1.setNombre("Cesar")
p1.setApellido("Mora")
p1.setRut("203770936")
p1.setSaldo(300000)
p1.setClave("3535")

p2.setNombre("Felipe")
p2.setApellido("Vera")
p2.setRut("202175936")
p2.setSaldo(600000)
p2.setClave("0213")

p3.setNombre("Diego")
p3.setApellido("Gonzalez")
p3.setRut("202974058")
p3.setSaldo(10000000)
p3.setClave("1010")

p4.setNombre("Theare")
p4.setApellido("Delgado")
p4.setRut("202254772")
p4.setSaldo(500000)
p4.setClave("2020")

###################################
p5.setnombrefuncionario("Albo")
p5.setapellidofuncionario("Fix")
p5.setrutfuncionario("203770456")

p6.setnombrefuncionario("Cesar")
p6.setapellidofuncionario("Perez")
p6.setrutfuncionario("203770325")

p7.setnombrefuncionario("There")
p7.setapellidofuncionario("Smith")
p7.setrutfuncionario("203754623")

p8.setnombrefuncionario("Felipino")
p8.setapellidofuncionario("Ortiz")
p8.setrutfuncionario("202172345")



#Creando listado de personas

listadoPersonas= Dispensador()
listadoPersonas.agregarPersonas(p1)
listadoPersonas.agregarPersonas(p2)
listadoPersonas.agregarPersonas(p3)
listadoPersonas.agregarPersonas(p4)
listadoPersonas.agregarFuncionarios(p5)
listadoPersonas.agregarFuncionarios(p6)
listadoPersonas.agregarFuncionarios(p7)
listadoPersonas.agregarFuncionarios(p8)

operaciones=["Sin Operacion","Depositar","Retirar","Transferir","Prestamo"]


root = Tk()
root.title("Banco") #Nombre que aparece en la ventana
root.geometry("1248x708")  #Define tamaño de la ventana
root.resizable(width=False, height=False)
#DATOS RANDOMSSS
#opciones=["Sin Operacion","Depositar","Retirar","Transferir","Prestamo"]
#DATOS DE CLIENTE
rut=StringVar()
rutv=StringVar()
#DATOS DE FUNCIONARIO
rutf=StringVar()
A1=""
B1=""
C1=""
C2=False
#Creando Variables para guardar dinero
Dep=0
Ret=0
Trans=0
Presta=0
#LLAMANDO A CLASES

#DATOS PRESTAMO
prestamosol=StringVar()
cantidadcuotas=StringVar()
A=[]
B=[]
C=[]
ListaDep=[]
ListaRet=[]
ListaTrans=[]
ListaPresta=[]
ListaTo=[]
contadorDep=0
contadorRet=0
contadorTrans=0
contadorPresta=0
contadorfinal=0
contadorfinal2=0
contadorfinal3=0
contadorfinal4=0
cont1=0
cont2=0
cont3=0
cont4=0
contadortabla=False
listaBorrados=[]
FiltroOp=StringVar()
FiltroEs=StringVar()


frame=Frame()
frame.pack()

#********************BACKGROUND***********************************************

background_img = Image.open("./bank.png")
background_tkimg = ImageTk.PhotoImage(background_img)
canvas = Canvas(root, highlightthickness=0)
canvas.pack(expand = True, fill = "both")
canvas.create_image(0,0, image = background_tkimg, anchor = "nw")
root.update()

#****************************************************************************





def abrirDepositar():
    if(ingresaRutCliente.get()==""):
        messagebox.showerror("Error", "Ingrese su RUT antes de realizar una operación")
    else:
        global cont1,ListaDep,ListaTo,C
        messagebox.showinfo(message="Usted es el n°"+str(cont1+1)+" en la cola", title="Depositar")  
        ventanaDepositar=Toplevel(root)
        ventanaDepositar.title("Depositar")
        ventanaDepositar.geometry("600x400")
        ventanaDepositar.resizable(width=False, height=False)
        def enDeposito():
            for persona in listadoPersonas.getLista():
                if (ingresaRutCliente.get()==persona.getRut()):
                    persona.setOperacion(operaciones[1])
                    listadoPersonas.agregarDeposito(persona)
                    listadoPersonas.agregarTabla(persona)
                    if (rutv.get()==ingresaRutCliente.get()):
                      Op.setSaldoop(persona.getSaldo())
                      Op.setMonto(int(ingresaMontoDeposito.get()))
                      A1=(Op.depositar(persona.getRut(), Op.getSaldoop(), Op.getmonto(), rutv))
                      Op.setEstado("Aceptado")
                    else:
                      Op.setEstado("Rechazado")
                    print(A1)
                    persona.setSaldo(A1)
                    A.append("Depositar")
                    C.append(Op.getEstado())
        
        
            global cont1
            global Dep,ListaDep,ListaTo
            cont1=cont1+1   
            B.append(cont1)
            ListaDep.append(int(ingresaMontoDeposito.get()))
            ListaTo.append(int(ingresaMontoDeposito.get()))
            Dep=Dep+(int(ingresaMontoDeposito.get()))
            blancos()
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
    if(ingresaRutCliente.get()==""):
        messagebox.showerror("Error", "Ingrese su RUT antes de realizar una operación")
    else:
        global cont2,ListaRet,ListaTo,C
        messagebox.showinfo(message="Usted es el n°"+str(cont2+1)+" en la cola", title="Retirar")
        ventanaRetirar=Toplevel(root)
        ventanaRetirar.title("Retirar")
        ventanaRetirar.geometry("600x400")
        ventanaRetirar.resizable(width=False, height=False)
        def enRetirar():
            global B1
            for persona in listadoPersonas.getLista():
                if (ingresaRutCliente.get()==persona.getRut()):
                    persona.setOperacion(operaciones[2])
                    listadoPersonas.agregarRetirar(persona)
                    listadoPersonas.agregarTabla(persona)
                    Op.setSaldoop(persona.getSaldo())
                    Op.setMontor(int(ingresaMontoRetiro.get()))
                    if ((rutv.get() == ingresaRutCliente.get()) and ( Op.getMontor()< Op.getSaldoop())):
                       B1=(Op.retirar(persona.getRut(), Op.getSaldoop(), Op.getMontor(), rutv))
                       Op.setEstado("Aceptado")
                       persona.setSaldo(B1)
                    else:
                        Op.setEstado("Rechazado")
                    print(B1)
                    A.append("Retirar")
                    C.append(Op.getEstado())

            global cont2
            global Ret,ListaRet,ListaTo
            cont2=cont2+1
            B.append(cont2)
            ListaRet.append(int(ingresaMontoRetiro.get()))
            ListaTo.append(int(ingresaMontoRetiro.get()))
            Ret=Ret+(int(ingresaMontoRetiro.get()))   
            blancos()
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
    if(ingresaRutCliente.get()==""):
        messagebox.showerror("Error", "Ingrese su RUT antes de realizar una operación")
    else:
        global cont3,ListaTrans,ListaTo,C
        messagebox.showinfo(message="Usted es el n°"+str(cont3+1)+" en la cola", title="Transferir")  
        ventanaTransferir=Toplevel(root)
        ventanaTransferir.title("Transferir")
        ventanaTransferir.geometry("600x400")
        ventanaTransferir.resizable(width=False, height=False)
        

        def enTransferir():

            global C1  
            global C2
            for persona in listadoPersonas.getLista():
                if (ingresaRutCliente.get()==persona.getRut()):
                    persona.setOperacion(operaciones[3])
                    listadoPersonas.agregarTransferir(persona)
                    listadoPersonas.agregarTabla(persona)
                    Op.setClave(persona.getClave())
                    Op.setSaldoop(persona.getSaldo())
                    Op.setMontor(int(ingresaMontoTransferir.get()))
                    if (Op.getMontor()<=Op.getSaldoop()):
                        C1=Op.TransferirUsuario(rutv.get(), Op.getClave(), Op.getSaldoop(), Op.getMontor())
                        C2=True
                        Op.setEstado("Aceptado")
                        persona.setSaldo(C1)
                    else:
                        C2=False
                        Op.setEstado("Rechazado")   
                    print(C1)
            for persona in listadoPersonas.getLista():
                if rutv.get()==persona.getRut() and C2==True:
                    Op.setSaldoop(persona.getSaldo())
                    Op.setMontor(int(ingresaMontoTransferir.get()))
                    C1=Op.TransferirCliente(rutv.get(), Op.getSaldoop(), Op.getMontor())
                    print(C1)
                    persona.setSaldo(C1)
                    C2=False
                    A.append("Transferir")
                    C.append(Op.getEstado())
                else:
                    A.append("Transferir")
                    C.append(Op.getEstado())
                    
            global cont3
            global Trans,ListaTrans,ListaTo
            cont3=cont3+1
            B.append(cont3)  
            ListaTrans.append(int(ingresaMontoTransferir.get()))
            ListaTo.append(int(ingresaMontoTransferir.get()))
            Trans=Trans+(int(ingresaMontoTransferir.get()))     
            blancos()
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
    if(ingresaRutCliente.get()==""):
        messagebox.showerror("Error", "Ingrese su RUT antes de realizar una operación")
    else:
        global cont4,ListaPresta,ListaTo,C
        messagebox.showinfo(message="Usted es el n°"+str(cont4+1)+" en la cola", title="Préstamo") 
        ventanaPrestamo=Toplevel(root)
        ventanaPrestamo.title("Préstamo")
        ventanaPrestamo.geometry("600x400")
        ventanaPrestamo.resizable(width=False, height=False)
        
    

        def enPrestamo():
            
            global C2
            for persona in listadoPersonas.getLista():
                if (ingresaRutCliente.get()==persona.getRut()):
                    persona.setOperacion(operaciones[4])
                    listadoPersonas.agregarPrestamo(persona)
                    listadoPersonas.agregarTabla(persona)
                    A.append("Prestamo")
                    Op.setEstado("Aceptado")
                    C.append(Op.getEstado())
                else:
                    Op.setEstado("Rechazado")
                    

            global cont4
            global Presta,ListaPresta,ListaTo
            cont4=cont4+1
            B.append(cont4)  
            ListaPresta.append(int(ingresaMontoPrestamo.get()))
            ListaTo.append(int(ingresaMontoPrestamo.get()))
            Presta=Presta+(int(ingresaMontoPrestamo.get()))
            blancos()
            ingresaCuotaPrestamo.delete(0,"end")
            ingresaMontoPrestamo.delete(0,"end")
            ventanaPrestamo.destroy()


        imagen = PhotoImage (file = "./ventanaPrestamo.png") 
        fondo=Label(ventanaPrestamo, image = imagen).place( x=0, y=0)


        ingresaMotivoPrestamo = ttk.Entry(ventanaPrestamo)
        ingresaMotivoPrestamo.place_configure(x=416, y=201 , width=169, height=17)

        ingresaMontoPrestamo = ttk.Combobox(ventanaPrestamo,values=("150000","300000","600000"),textvariable=prestamosol)
        ingresaMontoPrestamo.place_configure(x=416, y=227 , width=169, height=17)
        for persona in listadoPersonas.getLista():
            if (ingresaRutCliente.get()==persona.getRut()):
                ingresaPresupuestoPrestamo = ttk.Label(ventanaPrestamo,text=persona.getSaldo())
                ingresaPresupuestoPrestamo.place_configure(x=416, y=253 , width=169, height=17)
        ingresaCuotaPrestamo = ttk.Combobox(ventanaPrestamo,values=("3","6","9"),textvariable=cantidadcuotas)
        ingresaCuotaPrestamo.place_configure(x=417, y=282 , width=169, height=17)
        

        imagenConfirmaCliente5 = Image.open("./confirmarPrestamo.png")
        imagenConfirmaCliente5 = ImageTk.PhotoImage(imagenConfirmaCliente5)
        botonConfirmarCliente5 = ttk.Button(ventanaPrestamo, image= imagenConfirmaCliente5, command = enPrestamo)
        botonConfirmarCliente5.place( x=435, y=315)
        ventanaPrestamo.mainloop()


def abrirGrafico():
    if(ingresaRutFuncionario.get()==""):
        messagebox.showerror("Error", "Ingrese su RUT antes de revisar estadisticas")
    else:
        ventanaGrafico=Toplevel(root)
        ventanaGrafico.title("Análisis estadísticos")
        ventanaGrafico.geometry("950x500")
        ventanaGrafico.resizable(width=False, height=False)


        imagen = PhotoImage (file = "./ventanaAnalisisE.png") 
        fondo=Label(ventanaGrafico, image = imagen).place( x=0, y=0)

        def MostrarGrafico():
            global cont1,cont2,cont3,cont4
            if(cont4==0 and cont1>=1 and cont2>=1 and cont3>=1):
                fig, ax = plt.subplots()
                ax.set_title('Cantidad de operaciones')
                operaciones = [cont1, cont2, cont3]
                label = ["Depositar", "Retirar", "Transferir"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                grafico=plt.show()

            elif(cont4>=1 and cont1==0 and cont2>=1 and cont3>=1):
                fig, ax = plt.subplots()
                ax.set_title('Cantidad de operaciones')
                operaciones = [cont3, cont2, cont4]
                label = ["Transferir", "Retirar", "Préstamo"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()

            elif(cont4>=1 and cont1>=1 and cont3>=1 and cont2==0):
                fig, ax = plt.subplots()
                ax.set_title('Cantidad de operaciones')
                operaciones = [cont1,cont3,cont4]
                label = ["Depositar", "Transferir", "Préstamo"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%", colors= colores)
                plt.show()

            elif(cont4>=1 and cont1>=1 and cont2>=1 and cont3==0):
                fig, ax = plt.subplots()
                ax.set_title('Cantidad de operaciones')
                operaciones = [cont1, cont2, cont4]
                label = ["Depositar", "Retirar", "Préstamo"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()

            elif(cont4>=1 and cont1>=1 and cont2>=1 and cont3>=1):
                fig, ax = plt.subplots()
                ax.set_title('Cantidad de operaciones')
                operaciones = [cont1, cont3, cont2, cont4]
                label = ["Depositar", "Transferir", "Retirar", "Préstamo"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()

            elif(cont4>=1 and cont1==0 and cont2==0 and cont3==0):
                fig, ax = plt.subplots()
                ax.set_title('Cantidad de operaciones')
                operaciones = [cont4]
                label = ["Préstamo"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()
            elif(cont4==0 and cont1>=1 and cont2==0 and cont3==0):
                fig, ax = plt.subplots()
                ax.set_title('Cantidad de operaciones')
                operaciones = [cont1]
                label = ["Depositar"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()
            elif(cont4==0 and cont1==0 and cont2>=1 and cont3==0):
                fig, ax = plt.subplots()
                ax.set_title('Cantidad de operaciones')
                operaciones = [cont2]
                label = ["PRetirar"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()
            elif(cont4==0 and cont1==0 and cont2==0 and cont3>=1):
                fig, ax = plt.subplots()
                ax.set_title('Cantidad de operaciones')
                operaciones = [cont3]
                label = ["Transferir"]
                plt.pie(operaciones, labels=label, autopct="%0.1f %%")
                plt.show()
        def MovimientoDinero():
            global Dep,Ret,Trans,Presta
            if(Presta==0 and Dep>=1 and Ret>=1 and Trans>=1):
                fig, ax = plt.subplots()
                #Colocamos una etiqueta en el eje Y
                ax.set_ylabel('Dinero')
                #Colocamos una etiqueta en el eje X
                ax.set_title('Cantidad de dinero por operaciones')
                operaciones = [Dep, Ret, Trans]
                label = ["Depositar", "Retirar", "Transferir"]
                plt.bar(label, operaciones)
                plt.show()
            elif(Presta>=1 and Dep==0 and Ret>=1 and Trans>=1):
                fig, ax = plt.subplots()
                #Colocamos una etiqueta en el eje Y
                ax.set_ylabel('Dinero')
                #Colocamos una etiqueta en el eje X
                ax.set_title('Cantidad de dinero por operaciones')
                operaciones = [Presta, Ret, Trans]
                label = ["Prestamo", "Retirar", "Transferir"]
                plt.bar(label, operaciones)
                plt.show()
            elif(Presta>=1 and Dep>=1 and Ret==0 and Trans>=1):
                fig, ax = plt.subplots()
                #Colocamos una etiqueta en el eje Y
                ax.set_ylabel('Dinero')
                #Colocamos una etiqueta en el eje X
                ax.set_title('Cantidad de dinero por operaciones')
                operaciones = [Presta,Dep, Trans]
                label = ["Prestamo", "Depositar", "Transferir"]
                plt.bar(label, operaciones)
                plt.show()
            elif(Presta>=1 and Dep>=1 and Ret>=1 and Trans==0):
                fig, ax = plt.subplots()
                #Colocamos una etiqueta en el eje Y
                ax.set_ylabel('Dinero')
                #Colocamos una etiqueta en el eje X
                ax.set_title('Cantidad de dinero por operaciones')
                operaciones = [Presta,Dep, Ret]
                label = ["Prestamo", "Depositar", "Retirar"]
                plt.bar(label, operaciones)
                plt.show()
            elif(Presta>=1 and Dep>=1 and Ret>=1 and Trans>=1):
                fig, ax = plt.subplots()
                #Colocamos una etiqueta en el eje Y
                ax.set_ylabel('Dinero')
                #Colocamos una etiqueta en el eje X
                ax.set_title('Cantidad de dinero por operaciones')
                operaciones = [Presta,Dep,Ret, Trans]
                label = ["Prestamo", "Depositar","Retirar", "Transferir"]
                plt.bar(label, operaciones)
                plt.show()
            elif(Presta>=1 and Dep==0 and Ret==0 and Trans==0):
                fig, ax = plt.subplots()
                #Colocamos una etiqueta en el eje Y
                ax.set_ylabel('Dinero')
                #Colocamos una etiqueta en el eje X
                ax.set_title('Cantidad de dinero por operaciones')
                operaciones = [Presta]
                label = ["Prestamo"]
                plt.bar(label, operaciones)
                plt.show()
            elif(Presta==0 and Dep>=1 and Ret==0 and Trans==0):
                fig, ax = plt.subplots()
                #Colocamos una etiqueta en el eje Y
                ax.set_ylabel('Dinero')
                #Colocamos una etiqueta en el eje X
                ax.set_title('Cantidad de dinero por operaciones')
                operaciones = [Dep]
                label = ["Depositar"]
                plt.bar(label, operaciones)
                plt.show()
            elif(Presta==0 and Dep==0 and Ret>=1 and Trans==0):
                fig, ax = plt.subplots()
                #Colocamos una etiqueta en el eje Y
                ax.set_ylabel('Dinero')
                #Colocamos una etiqueta en el eje X
                ax.set_title('Cantidad de dinero por operaciones')
                operaciones = [Ret]
                label = ["Retirar"]
                plt.bar(label, operaciones)
                plt.show()
            elif(Presta==0 and Dep==0 and Ret==0 and Trans>=1):
                fig, ax = plt.subplots()
                #Colocamos una etiqueta en el eje Y
                ax.set_ylabel('Dinero')
                #Colocamos una etiqueta en el eje X
                ax.set_title('Cantidad de dinero por operaciones')
                operaciones = [Trans]
                label = ["Transferir"]
                plt.bar(label, operaciones)
                plt.show()
        def TotalClientes():
            global cont1,cont2,cont3,cont4,contadorfinal
            contadorfinal=contadorfinal+cont1+cont2+cont3+cont4
            Graficos=ttk.Label(ventanaGrafico,text=contadorfinal)
            Graficos.place(x=282,y=130, width=99, height=15)
            contadorfinal=0
        def TotalDinero():
            global Dep,Ret,Trans,Presta,contadorfinal2
            contadorfinal2=contadorfinal2+Dep+Ret+Trans+Presta    
            Dinero=ttk.Label(ventanaGrafico,text=contadorfinal2)
            Dinero.place(x=282,y=220, width=99, height=15)
            contadorfinal2=0
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
            #Calculando medias de operacion
            media=int(contadorfinal3/contadorfinal4)
            mediaDep=int(contadorDep/cont1)
            mediaRet=int(contadorRet/cont2)
            mediaTrans=int(contadorTrans/cont3)
            mediaPresta=int(contadorPresta/cont4)
            #Medianas
            medianaDep=(stats.median(ListaDep))
            medianaRet=(stats.median(ListaRet))
            medianaTrans=(stats.median(ListaTrans))
            medianaPresta=(stats.median(ListaPresta))
            medianaTo=(stats.median(ListaTo))
            #MODAS
            modaDep=(stats.mode(ListaDep))
            modaRet=(stats.mode(ListaRet))
            modaTrans=(stats.mode(ListaTrans))
            modaPresta=(stats.mode(ListaPresta))
            modaTo=(stats.mode(ListaTo))
            #Desviacion estandar
            DesvDep=(stats.mode(ListaDep))
            DesvRet=(stats.mode(ListaRet))
            DesvTrans=(stats.mode(ListaTrans))
            DesvPresta=(stats.mode(ListaPresta))
            DesvTo=(stats.mode(ListaTo))
            #Llamando labels Media
            mediaDep=ttk.Label(ventanaGrafico,text=mediaDep)
            mediaDep.place(x=195,y=400, width=140, height=16)
            mediaRet=ttk.Label(ventanaGrafico,text=mediaRet)
            mediaRet.place(x=195,y=424, width=140, height=16)
            mediaTrans=ttk.Label(ventanaGrafico,text=mediaTrans)
            mediaTrans.place(x=195,y=445, width=140, height=16)
            mediaPresta=ttk.Label(ventanaGrafico,text=mediaPresta)
            mediaPresta.place(x=195,y=468, width=140, height=16)
            #Llamando labels Mediana
            medianaDepo=ttk.Label(ventanaGrafico,text=medianaDep)
            medianaDepo.place(x=359,y=400, width=135, height=16)
            medianaReti=ttk.Label(ventanaGrafico,text=medianaRet)
            medianaReti.place(x=359,y=424, width=135, height=16)
            medianaTransf=ttk.Label(ventanaGrafico,text=medianaTrans)
            medianaTransf.place(x=359,y=445, width=135, height=16)
            medianaPrestam=ttk.Label(ventanaGrafico,text=medianaPresta)
            medianaPrestam.place(x=359,y=468, width=135, height=16)
            #Llamando Labels Moda
            modaDepo=ttk.Label(ventanaGrafico,text= modaDep)
            modaDepo.place(x=518,y=400, width=113, height=16)
            modaReti=ttk.Label(ventanaGrafico,text= modaRet)
            modaReti.place(x=518,y=424, width=113, height=16)
            modaTransf=ttk.Label(ventanaGrafico,text= modaTrans)
            modaTransf.place(x=518,y=445, width=113, height=16)
            modaPrestam=ttk.Label(ventanaGrafico,text= modaPresta)
            modaPrestam.place(x=518,y=468, width=113, height=16)
            #Llamando labels desv estandar
            DesDepo=ttk.Label(ventanaGrafico,text= DesvDep)
            DesDepo.place(x=654,y=400, width=240, height=16)
            DesReti=ttk.Label(ventanaGrafico,text= DesvRet)
            DesReti.place(x=654,y=424, width=240, height=16)
            DesTransf=ttk.Label(ventanaGrafico,text= DesvTrans)
            DesTransf.place(x=654,y=445, width=240, height=16)
            DesPrestam=ttk.Label(ventanaGrafico,text= DesvPresta)
            DesPrestam.place(x=654,y=468, width=240, height=16)
            #----------------------------------------
            contadorfinal3=0
            contadorfinal4=0
            media=0
            contadorDep=0
            contadorRet=0
            contadorTrans=0
            contadorPresta=0

        #gráfico por operaciones
        imgMostrarGraficoOp = Image.open("./graficoOp.png")
        imgMostrarGraficoOp = ImageTk.PhotoImage(imgMostrarGraficoOp)
        botonMostrarGrafico = ttk.Button(ventanaGrafico, image= imgMostrarGraficoOp, command = MostrarGrafico)
        botonMostrarGrafico.place( x=550, y=105)

        #gráfico por dinero
        imgMostrarGraficoDin = Image.open("./graficoDinero.png")
        imgMostrarGraficoDin = ImageTk.PhotoImage(imgMostrarGraficoDin)
        botonMostrarDinero = ttk.Button(ventanaGrafico, image= imgMostrarGraficoDin, command = MovimientoDinero)
        botonMostrarDinero.place( x=550, y=196)

        #total clientes
        imgTotalClientes = Image.open("./totalPersonas.png")
        imgTotalClientes = ImageTk.PhotoImage(imgTotalClientes)
        botonMostrarClientes = ttk.Button(ventanaGrafico,image=imgTotalClientes, command = TotalClientes)
        botonMostrarClientes.place( x=27, y=105)

        #total dinero
        imgTotalDin = Image.open("./totalDinero.png")
        imgTotalDin = ImageTk.PhotoImage(imgTotalDin)
        botonMostrardinerototal = ttk.Button(ventanaGrafico,image=imgTotalDin, command = TotalDinero)
        botonMostrardinerototal.place( x=27, y=191)


        #mostrar todo
        imgMostrarTodo = Image.open("./mostrarTodo.png")
        imgMostrarTodo = ImageTk.PhotoImage(imgMostrarTodo)
        botonMostrarCalculos = ttk.Button(ventanaGrafico,image=imgMostrarTodo, command = CalculosMat)
        botonMostrarCalculos.place( x=27, y=278)

        blancosfu()
        ventanaGrafico.mainloop()







def abrirMostrarCola():



    def abrirConfirmaRutFinalizar():

        def confirmaFinaliza():
            for Funcionario in listadoPersonas.getListaFuncionarios():
                if (confirmaRut.get()==Funcionario.getrutfuncionario()):
                    finzalizaProceso()
                    ventanaConfirmaRut.destroy()

        ventanaConfirmaRut=Toplevel(root)
        ventanaConfirmaRut.title("RUT del Funcionario")
        ventanaConfirmaRut.geometry("300x100")
        ventanaConfirmaRut.resizable(width=False, height=False)

        imagenRUT = PhotoImage (file = "./ventanaFuncionario.png") 
        fondo=Label(ventanaConfirmaRut, image = imagenRUT).place( x=0, y=0)

        imagenConfirmarRut = Image.open("./confirmarVentana.png")
        imagenConfirmarRut = ImageTk.PhotoImage(imagenConfirmarRut)
        botonConfirmarRut = ttk.Button(ventanaConfirmaRut, image= imagenConfirmarRut, command= confirmaFinaliza)
        botonConfirmarRut.place( x=157, y=54)


        confirmaRut = ttk.Entry(ventanaConfirmaRut)
        confirmaRut.place( x=91, y=21, width=172, height=20)



        ventanaConfirmaRut.mainloop()

    def abrirConfirmaRutElimina():

        def confirmaElimina():
            for Funcionario in listadoPersonas.getListaFuncionarios():
                if (confirmaRut.get()==Funcionario.getrutfuncionario()):
                    elimina()
                    ventanaConfirmaRut.destroy()

        ventanaConfirmaRut=Toplevel(root)
        ventanaConfirmaRut.title("RUT del Funcionario")
        ventanaConfirmaRut.geometry("300x100")
        ventanaConfirmaRut.resizable(width=False, height=False)

        imagenRUT = PhotoImage (file = "./ventanaFuncionario.png") 
        fondo=Label(ventanaConfirmaRut, image = imagenRUT).place( x=0, y=0)

        imagenConfirmarRut = Image.open("./confirmarVentana.png")
        imagenConfirmarRut = ImageTk.PhotoImage(imagenConfirmarRut)
        botonConfirmarRut = ttk.Button(ventanaConfirmaRut, image= imagenConfirmarRut, command = confirmaElimina)
        botonConfirmarRut.place( x=157, y=54)


        confirmaRut = ttk.Entry(ventanaConfirmaRut)
        confirmaRut.place( x=91, y=21, width=172, height=20)




        ventanaConfirmaRut.mainloop()

    def elimina():
        x = tabla.selection()
        tabla.delete(x)
    def finzalizaProceso():
        global contadortabla
        seleccionado = tabla.focus()
        id2=tabla.set(seleccionado, "Estado", "Finalizado")
        return id2
        contadortabla=True
    def actualizarTabla():
        global C
        i=0
        records = tabla.get_children()
        for x in records:
            tabla.set(x,"Estado",C[i])
            i=i+1


    ventanaMostrarCola=Toplevel(root)
    ventanaMostrarCola.title("Mostrar Colas de Servicio")
    ventanaMostrarCola.geometry("1000x400")
    ventanaMostrarCola.resizable(width=False, height=False)
    #Fondo de la ventanaMostrarcola
    imagen = PhotoImage (file = "./ventanaCola.png") 
    fondo=Label(ventanaMostrarCola, image = imagen).place( x=0, y=0)
    #Botones para filtrar las Colas de prioridades#############
    imagenEliminar = Image.open("./eliminaServicio.png")
    imagenEliminar = ImageTk.PhotoImage(imagenEliminar)
    botonEliminar = ttk.Button(ventanaMostrarCola, image= imagenEliminar, command = abrirConfirmaRutElimina)
    botonEliminar.place( x=827, y=70)

    imagenFinalizar = Image.open("./finalizarServicio.png")
    imagenFinalizar = ImageTk.PhotoImage(imagenFinalizar)
    botonFinalizar = ttk.Button(ventanaMostrarCola, image= imagenFinalizar, command = abrirConfirmaRutFinalizar)
    botonFinalizar.place( x=827, y=153)

    imagenActualizar = Image.open("./actualizar.png")
    imagenActualizar = ImageTk.PhotoImage(imagenActualizar)
    botonActualizar = ttk.Button(ventanaMostrarCola, image= imagenActualizar,command=actualizarTabla)
    botonActualizar.place( x=827, y=233)


    
    #Creacion de la tabla
    tabla = ttk.Treeview(ventanaMostrarCola)
    tabla['columns']=("N° Atencion","Operacion", "Rut","Estado")
    tabla.column('#0', width=0, stretch=NO)
    tabla.column("Rut", anchor=CENTER, width=200)
    tabla.column("Operacion", anchor=CENTER, width=200)
    tabla.column("N° Atencion", anchor=CENTER, width=80)
    tabla.column("Estado", anchor=CENTER, width=200)
    


    tabla.heading('#0', text='', anchor=CENTER)
    tabla.heading("Rut", text="Rut", anchor=CENTER)
    tabla.heading("Operacion", text="Operacion", anchor=CENTER)
    tabla.heading("N° Atencion", text="N° Atencion", anchor=CENTER)
    tabla.heading("Estado", text="Estado", anchor=CENTER)
    

    
    tabla.place(x=57,y=70)
    n=1
    I=0
    b=0
    m=0
    ru=[]
    global contadortabla
    for persona in listadoPersonas.getListaTabla():
        ru.append(persona.getRut())
        num=n
        est="En proceso"
        fin="Finalizado"
        id=tabla.insert("",END,text="",values=([B[m],A[I],ru[b],est]))
        print(id)
        n=n+1
        I=I+1
        b=b+1
        m=m+1
        



    #***************FILTROS********************




    def callbackFunc(event):
     print("Seleccionó un nuevo elemento")
     global C
     i=0
     records = tabla.get_children()
     for x in records:
        tabla.set(x,"Estado",C[i])
        A=C[i]
        if A!=FiltroEs.get():
            tabla.detach(x,"Estado",C[i])
        i=i+1
            

    FiltrarOperaciones = ttk.Combobox(ventanaMostrarCola,values=("Mostrar todo","Depositar","Transferir","Retirar","Prestamo"),textvariable=FiltroOp, state="readonly")
    FiltrarOperaciones.place_configure(x=199, y=326 , width=280, height=20)
    FiltrarOperaciones.bind("<<ComboboxSelected>>", callbackFunc)

    FiltrarEstados = ttk.Combobox(ventanaMostrarCola,values=("Mostrar todo","Aceptado","Rechazado","En proceso"),textvariable=FiltroEs, state="readonly")
    FiltrarEstados.place_configure(x=199, y=349 , width=280, height=20)
    FiltrarOperaciones.bind("<<ComboboxSelected>>", callbackFunc)




    ventanaMostrarCola.mainloop()


#-------------------------------------------------------------------

                             #DEF RANDOMS
def blancos():
    ingresaRutCliente.delete(0,"end")
    ingresaApellidoCliente.destroy()
    ingresaNombreCliente.destroy()
    ingresaSaldoCliente.destroy()

def blancosfu():
    ingresaRutFuncionario.delete(0,"end")
    ingresaNombreFuncionario.destroy()
    ingresaApellidoFuncionario.destroy()

def ConfirmarDatos():
    global ingresaApellidoCliente
    global ingresaNombreCliente
    global ingresaSaldoCliente
    for persona in listadoPersonas.getLista():
        if (ingresaRutCliente.get()==persona.getRut()):
            ingresaNombreCliente = ttk.Label(root, text=persona.getNombre())
            ingresaNombreCliente.place(x=188, y=201, width=279, height=20)
            ingresaApellidoCliente = ttk.Label(root,text=persona.getApellido())
            ingresaApellidoCliente.place( x=188, y=229, width=279, height=20)
            ingresaSaldoCliente = ttk.Label(root,text=persona.getSaldo())
            ingresaSaldoCliente.place( x=188, y=284, width=279, height=20)
       
def Mostrardatosfun():
    global ingresaNombreFuncionario
    global ingresaApellidoFuncionario
    for Funcionario in listadoPersonas.getListaFuncionarios():
        if (ingresaRutFuncionario.get()==Funcionario.getrutfuncionario()):
            ingresaNombreFuncionario = ttk.Label(root,text=Funcionario.getnombrefuncionario())                         
            ingresaNombreFuncionario.place( x=811, y=201, width=279, height=20)  
            ingresaApellidoFuncionario = ttk.Label(root,text=Funcionario.getapellidofuncionario())
            ingresaApellidoFuncionario.place( x=811, y=229, width=279, height=20)
       

        
#*********************ENTRYS CLIENTE******************************************

#ttk.Entry(root)

ingresaRutCliente = ttk.Entry(root,textvariable=rut)
ingresaRutCliente.place( x=188, y=257, width=279, height=20)  


#************************ENTRYS FUNCIONARIO***********************************

ingresaRutFuncionario = ttk.Entry(root,textvariable=rutf)
ingresaRutFuncionario.place( x=811, y=257, width=279, height=20)  


#*******************BOTONES***************************************************


#------Depositar----

imagenDepositar = Image.open("./depositar.png")
imagenDepositar = ImageTk.PhotoImage(imagenDepositar)
botonDepositar = ttk.Button(canvas, image= imagenDepositar, command = abrirDepositar)
botonDepositar.place( x=49, y=425)



#------Retirar-----
imagenRetirar = Image.open("./retirar.png")
imagenRetirar = ImageTk.PhotoImage(imagenRetirar)
botonRetirar = ttk.Button(canvas, image= imagenRetirar, command = abrirRetirar)
botonRetirar.place( x=49, y=555)

#------Transferir-----
imagenTransferir = Image.open("./transferir.png")
#imagenTransferir = imagenTransferir.resize((31,53),Image.ANTIALIAS)
imagenTransferir = ImageTk.PhotoImage(imagenTransferir)
botonTransferir = ttk.Button(canvas, image= imagenTransferir, command = abrirTransferir)
botonTransferir.place( x=357, y=425)

#------Prestamo-----

imagenPrestamo = Image.open("./prestamo.png")
#imagenPrestamo = imagenPrestamo.resize((50,35),Image.ANTIALIAS)
imagenPrestamo = ImageTk.PhotoImage(imagenPrestamo)
botonPrestamo = ttk.Button(canvas, image= imagenPrestamo, command = abrirPrestamo)
botonPrestamo.place( x=357, y=555)



#------Analisis Estadisticos-----

imagenGrafico = Image.open("./grafico.png")
#imagenGrafico= imagenGrafico.resize((50,46),Image.ANTIALIAS)
imagenGrafico = ImageTk.PhotoImage(imagenGrafico)
botonGrafico = ttk.Button(canvas, image= imagenGrafico, command = abrirGrafico)
botonGrafico.place( x=793, y=425)

#------Cola-----

imagenCola = Image.open("./atendido.png")
imagenCola= imagenCola.resize((62,51),Image.ANTIALIAS)
imagenCola = ImageTk.PhotoImage(imagenCola)
botonCola = ttk.Button(canvas, image= imagenCola, command = abrirMostrarCola)
botonCola.place( x=750, y=1)

#----------Confirmar---------
imagenConfirmaCliente1 = Image.open("./guardarCliente1.png")
imagenConfirmaCliente1 = ImageTk.PhotoImage(imagenConfirmaCliente1)
botonConfirmarCliente1 = ttk.Button(canvas, image= imagenConfirmaCliente1,command = ConfirmarDatos)
botonConfirmarCliente1.place( x=280, y=325)


imagenConfirmaFuncionario = Image.open("./guardarFuncionario.png")
imagenConfirmaFuncionario = ImageTk.PhotoImage(imagenConfirmaFuncionario)
botonConfirmarFuncionario = ttk.Button(canvas, image= imagenConfirmaFuncionario,command = Mostrardatosfun)
botonConfirmarFuncionario.place( x=900, y=325) 

#*****************************************************************************





#*****************************************************************************
root.mainloop() #Ejecución programa