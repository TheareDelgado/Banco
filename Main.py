from pathlib import WindowsPath
import tkinter 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Button
from Cliente import *
from Persona import *
from dispensador import *
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
from Funcionario import *

#Creando personas

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


p2.setNombre("Felipe")
p2.setApellido("Vera")
p2.setRut("202175936")
p2.setSaldo(600000)

p3.setNombre("Diego")
p3.setApellido("Gonzalez")
p3.setRut("202974058")
p3.setSaldo(10000000)

p4.setNombre("Theare")
p4.setApellido("Delgado")
p4.setRut("202254472")
p4.setSaldo(500000)

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


root = Tk()
root.title("Banco") #Nombre que aparece en la ventana
root.geometry("1248x1543")  #Define tamaño de la ventana
root.resizable(width=False, height=False)
#DATOS RANDOMSSS
opciones=["1","2","3","4"]
#DATOS DE CLIENTE
rut=StringVar()

#DATOS DE FUNCIONARIO
rutf=StringVar()

#LLAMANDO A CLASES

#DATOS PRESTAMO
prestamosol=StringVar()
cantidadcuotas=StringVar()
LISTAALTA=[StringVar()]
LISTABAJA=[StringVar()]
A=[]


frame=Frame()
frame.pack()

#********************BACKGROUND***********************************************

background_img = Image.open("./EDD/bank.png")
background_tkimg = ImageTk.PhotoImage(background_img)
canvas = Canvas(root, highlightthickness=0)
canvas.pack(expand = True, fill = "both")
canvas.create_image(0,0, image = background_tkimg, anchor = "nw")
root.update()

#****************************************************************************


def abrirDepositar():
    ventanaDepositar=Toplevel(root)
    ventanaDepositar.title("Depositar")
    ventanaDepositar.geometry("1248x708")
    ventanaDepositar.resizable(width=False, height=False)

    def enDeposito():
        for persona in listadoPersonas.getLista():
            if (ingresaRutCliente.get()==persona.getRut()):
                persona.setOperacion("Depositar")
                listadoPersonas.agregarDeposito(persona)
                listadoPersonas.agregarTabla(persona)
                A.append("Depositar")
                
                
                
        
        ventanaDepositar.destroy()


    imagen = PhotoImage (file = "./EDD/ventanaDepositar.png") 
    fondo=Label(ventanaDepositar, image = imagen).place( x=0, y=0)

    #Entry y Label

    ingresaCuentaDeposito = ttk.Entry(ventanaDepositar)
    ingresaCuentaDeposito.place_configure(x=842, y=353 , width=270, height=20)

    ingresaMontoDeposito = ttk.Entry(ventanaDepositar)
    ingresaMontoDeposito.place_configure(x=842, y=379 , width=270, height=20)


    imagenConfirmaCliente2 = Image.open("./EDD/guardarCliente2.png")
    imagenConfirmaCliente2 = ImageTk.PhotoImage(imagenConfirmaCliente2)
    botonConfirmarCliente2 = ttk.Button(ventanaDepositar, image= imagenConfirmaCliente2, command = enDeposito)
    botonConfirmarCliente2.place( x=838, y=525)


    ventanaDepositar.mainloop()


def abrirRetirar():
    ventanaRetirar=Toplevel(root)
    ventanaRetirar.title("Retirar")
    ventanaRetirar.geometry("1248x708")
    ventanaRetirar.resizable(width=False, height=False)

    def enRetirar():
        for persona in listadoPersonas.getLista():
            if (ingresaRutCliente.get()==persona.getRut()):
                persona.setOperacion("Retirar")
                listadoPersonas.agregarRetirar(persona)
                listadoPersonas.agregarTabla(persona)
                A.append("Retirar")

        ventanaRetirar.destroy()


    imagen = PhotoImage (file = "./EDD/ventanaDepositar.png") 
    fondo=Label(ventanaRetirar, image = imagen).place( x=0, y=0)


    ingresaCuentaRetiro = ttk.Entry(ventanaRetirar)
    ingresaCuentaRetiro.place_configure(x=842, y=353 , width=270, height=20)

    ingresaMontoRetiro = ttk.Entry(ventanaRetirar)
    ingresaMontoRetiro.place_configure(x=842, y=379 , width=270, height=20)


    imagenConfirmaCliente3 = Image.open("./EDD/guardarCliente2.png")
    imagenConfirmaCliente3 = ImageTk.PhotoImage(imagenConfirmaCliente3)
    botonConfirmarCliente3 = ttk.Button(ventanaRetirar, image= imagenConfirmaCliente3, command = enRetirar)
    botonConfirmarCliente3.place( x=838, y=525)

    ventanaRetirar.mainloop()


def abrirTransferir():
    ventanaTransferir=Toplevel(root)
    ventanaTransferir.title("Transferir")
    ventanaTransferir.geometry("1248x708")
    ventanaTransferir.resizable(width=False, height=False)

    def enTransferir():
        for persona in listadoPersonas.getLista():
            if (ingresaRutCliente.get()==persona.getRut()):
                persona.setOperacion("Transferir")
                listadoPersonas.agregarTransferir(persona)
                listadoPersonas.agregarTabla(persona)
                A.append("Transferir")

        ventanaTransferir.destroy()


    imagen = PhotoImage (file = "./EDD/ventanaTransferir.png") 
    fondo=Label(ventanaTransferir, image = imagen).place( x=0, y=0)





    ingresaNombreTransferir = ttk.Entry(ventanaTransferir)
    ingresaNombreTransferir.place_configure(x=875, y=349 , width=270, height=20)

    ingresaApellidoTransferir = ttk.Entry(ventanaTransferir)
    ingresaApellidoTransferir.place_configure(x=875, y=375 , width=270, height=20)

    ingresaCorreoTransferir = ttk.Entry(ventanaTransferir)
    ingresaCorreoTransferir.place_configure(x=875, y=402 , width=270, height=20)

    ingresaCuentaTransferir = ttk.Entry(ventanaTransferir)
    ingresaCuentaTransferir.place_configure(x=875, y=428 , width=270, height=20)

    ingresaMontoTransferir = ttk.Entry(ventanaTransferir)
    ingresaMontoTransferir.place_configure(x=875, y=452 , width=270, height=20)

    ingresaBancoTransferir = ttk.Entry(ventanaTransferir)
    ingresaBancoTransferir.place_configure(x=875, y=476 , width=270, height=20)


    imagenConfirmaCliente4 = Image.open("./EDD/guardarCliente2.png")
    imagenConfirmaCliente4 = ImageTk.PhotoImage(imagenConfirmaCliente4)
    botonConfirmarCliente4 = ttk.Button(ventanaTransferir, image= imagenConfirmaCliente4, command = enTransferir)
    botonConfirmarCliente4.place( x=836, y=525)

    ventanaTransferir.mainloop()


def abrirPrestamo():
    ventanaPrestamo=Toplevel(root)
    ventanaPrestamo.title("Prestamo")
    ventanaPrestamo.geometry("1248x708")
    ventanaPrestamo.resizable(width=False, height=False)

    def enPrestamo():
        for persona in listadoPersonas.getLista():
            if (ingresaRutCliente.get()==persona.getRut()):
                persona.setOperacion("Prestamo")
                listadoPersonas.agregarPrestamo(persona)
                listadoPersonas.agregarTabla(persona)
                A.append("Prestamo")

        ventanaPrestamo.destroy()


    imagen = PhotoImage (file = "./EDD/ventanaPrestamo.png") 
    fondo=Label(ventanaPrestamo, image = imagen).place( x=0, y=0)

    ingresaMonto = ttk.Entry(ventanaPrestamo)
    ingresaMonto.place()
    


    ingresaMotivoPrestamo = ttk.Entry(ventanaPrestamo)
    ingresaMotivoPrestamo.place_configure(x=892, y=364 , width=270, height=20)

    ingresaMontoPrestamo = ttk.Combobox(ventanaPrestamo,values=("$150.000","$300.000","$600.000"),textvariable=prestamosol)
    ingresaMontoPrestamo.place_configure(x=893, y=389 , width=270, height=20)
    for persona in listadoPersonas.getLista():
        if (ingresaRutCliente.get()==persona.getRut()):
            ingresaPresupuestoPrestamo = ttk.Label(ventanaPrestamo,text=persona.getSaldo())
            ingresaPresupuestoPrestamo.place_configure(x=892, y=415 , width=270, height=20)
    ingresaCuotaPrestamo = ttk.Combobox(ventanaPrestamo,values=("3","6","9"),textvariable=cantidadcuotas)
    ingresaCuotaPrestamo.place_configure(x=892, y=442 , width=270, height=20)
    

    imagenConfirmaCliente5 = Image.open("./EDD/guardarCliente2.png")
    imagenConfirmaCliente5 = ImageTk.PhotoImage(imagenConfirmaCliente5)
    botonConfirmarCliente5 = ttk.Button(ventanaPrestamo, image= imagenConfirmaCliente5, command = enPrestamo)
    botonConfirmarCliente5.place( x=840, y=535)
    ventanaPrestamo.mainloop()


def abrirGrafico():
    #ventanaGrafico=Toplevel(root)
    #ventanaGrafico.title("Gráfico")
    #ventanaGrafico.geometry("1248x708")
    #ventanaGrafico.resizable(width=False, height=False)
    cantidadPrestamos = 0
    cantidadDepositos = 6
    cantidadRetirar = 5
    cantidadTransferencias = 9

    if(cantidadPrestamos==0 and cantidadDepositos>=1 and cantidadRetirar>=1 and cantidadTransferencias>=1):
        operaciones = [cantidadDepositos, cantidadTransferencias, cantidadRetirar]
        normdata = colors.Normalize(min(operaciones), max(operaciones))
        colormap = cm.get_cmap("Blues")
        colores =colormap(normdata(operaciones))

        label = ["Depositar", "Transferir", "Retirar"]

        plt.pie(operaciones, labels=label, autopct="%0.1f %%", colors= colores)
        plt.show()

    if(cantidadPrestamos>=1 and cantidadDepositos==0 and cantidadRetirar>=1 and cantidadTransferencias>=1):
        operaciones = [cantidadTransferencias, cantidadRetirar, cantidadPrestamos]
        normdata = colors.Normalize(min(operaciones), max(operaciones))
        colormap = cm.get_cmap("Blues")
        colores =colormap(normdata(operaciones))

        label = ["Transferir", "Retirar", "Préstamo"]

        plt.pie(operaciones, labels=label, autopct="%0.1f %%", colors= colores)
        plt.show()

    if(cantidadPrestamos>=1 and cantidadDepositos>=1 and cantidadTransferencias>=1 and cantidadRetirar==0):
        operaciones = [cantidadDepositos, cantidadTransferencias, cantidadPrestamos]
        normdata = colors.Normalize(min(operaciones), max(operaciones))
        colormap = cm.get_cmap("Blues")
        colores =colormap(normdata(operaciones))

        label = ["Depositar", "Transferir", "Préstamo"]

        plt.pie(operaciones, labels=label, autopct="%0.1f %%", colors= colores)
        plt.show()

    if(cantidadPrestamos>=1 and cantidadDepositos>=1 and cantidadRetirar>=1 and cantidadTransferencias==0):
        operaciones = [cantidadDepositos, cantidadRetirar, cantidadPrestamos]
        normdata = colors.Normalize(min(operaciones), max(operaciones))
        colormap = cm.get_cmap("Blues")
        colores =colormap(normdata(operaciones))

        label = ["Depositar", "Retirar", "Préstamo"]

        plt.pie(operaciones, labels=label, autopct="%0.1f %%", colors= colores)
        plt.show()

    if(cantidadPrestamos>=1 and cantidadDepositos>=1 and cantidadRetirar>=1 and cantidadTransferencias>=1):
        operaciones = [cantidadDepositos, cantidadTransferencias, cantidadRetirar, cantidadPrestamos]
        normdata = colors.Normalize(min(operaciones), max(operaciones))
        colormap = cm.get_cmap("Blues")
        colores =colormap(normdata(operaciones))

        label = ["Depositar", "Transferir", "Retirar", "Préstamo"]

        plt.pie(operaciones, labels=label, autopct="%0.1f %%", colors= colores)
        plt.show()
    
#Si una de las variables es 0 que no muestre el label y solo muestre las otras operaciones!!!




    #ventanaGrafico.mainloop()


def abrirMostrarCola():
    ventanaMostrarCola=Toplevel(root)
    ventanaMostrarCola.title("Mostrar Colas de Servicio")
    ventanaMostrarCola.geometry("1200x350")
    ventanaMostrarCola.resizable(width=False, height=False)
    #Fondo de la ventanaMostrarcola
    imagen = PhotoImage (file = "./EDD/fondoCDS.png") 
    fondo=Label(ventanaMostrarCola, image = imagen).place( x=0, y=0)
    #Botones para filtrar las Colas de prioridades#############
    #Boton para filtrar la tabla por colas de prioridad de depositos
    imagenDepositar1 = Image.open("./EDD/depositar.png")
    imagenDepositar1 = ImageTk.PhotoImage(imagenDepositar1)
    botonDepositar1 = ttk.Button(ventanaMostrarCola,image= imagenDepositar)
    botonDepositar1.place( x=80, y=22, width=90, height=60)
    #Boton para filtrar la tabla por colas de prioridad de Retiros
    imagenRetirar1 = Image.open("./EDD/retirar.png")
    imagenRetirar1 = imagenRetirar1.resize((65,54),Image.ANTIALIAS)
    imagenRetirar1 = ImageTk.PhotoImage(imagenRetirar1)
    botonRetirar1 = ttk.Button(ventanaMostrarCola, image= imagenRetirar1)
    botonRetirar1.place( x=80, y=150, width=90, height=60)
    #Boton para filtrar la tabla por colas de prioridad de Transferencias
    imagenTransferir1 = Image.open("./EDD/transferir.png")
    imagenTransferir1 = imagenTransferir1.resize((42,53),Image.ANTIALIAS)
    imagenTransferir1 = ImageTk.PhotoImage(imagenTransferir1)
    botonTransferir1 = ttk.Button(ventanaMostrarCola, image= imagenTransferir1)
    botonTransferir1.place( x=1025, y=22, width=90, height=60)
    #Boton para filtrar la tabla por colas de prioridad de Prestamos
    imagenPrestamo1 = Image.open("./EDD/prestamo.png")
    imagenPrestamo1 = imagenPrestamo1.resize((60,53),Image.ANTIALIAS)
    imagenPrestamo1 = ImageTk.PhotoImage(imagenPrestamo1)
    botonPrestamo1 = ttk.Button(ventanaMostrarCola, image= imagenPrestamo1)
    botonPrestamo1.place( x=1025, y=150, width=90, height=60)

    #Falta modificar el command de cada boton para de este modo llamar a un metodo que limpie la tabla y la actualize con las colas que se le solicitan
    #Falta agregar label en la tabla colocando a que cola pertenece cada boton,(ejemplo: en el boton de depositar colocar un label que diga "Cola de depositos", y asi con los demas botones)

    #Creacion de la tabla
    tabla = ttk.Treeview(ventanaMostrarCola)
    tabla['columns']=("Rut","Operacion", "N° Atencion","Estado")
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

    
    
    tabla.pack()
    n=1
    I=0
    for persona in listadoPersonas.getListaTabla():
        tabla.insert("",END,text="2",values=(persona.getRut(),A[I],n,"En proceso"))
        I=I+1
        n=n+1
        
    ventanaMostrarCola.mainloop()


   
    
        

  

#-------------------------------------------------------------------

                             #DEF RANDOMS


def ConfirmarDatos():
    for persona in listadoPersonas.getLista():
        if (ingresaRutCliente.get()==persona.getRut()):
            ingresaNombreCliente = ttk.Label(root, text=persona.getNombre())
            ingresaNombreCliente.place(x=193, y=213, width=270, height=20)
            ingresaApellidoCliente = ttk.Label(root,text=persona.getApellido())
            ingresaApellidoCliente.place( x=193, y=240, width=270, height=20) 
            ingresaSaldoCliente = ttk.Label(root,text=persona.getSaldo())
            ingresaSaldoCliente.place( x=193, y=292, width=270, height=20)
       
def Mostrardatosfun():
    for Funcionario in listadoPersonas.getListaFuncionarios():
        if (ingresaRutFuncionario.get()==Funcionario.getrutfuncionario()):
            ingresaNombreFuncionario = ttk.Label(root,text=Funcionario.getnombrefuncionario())                         
            ingresaNombreFuncionario.place( x=793, y=213, width=270, height=20)  
            ingresaApellidoFuncionario = ttk.Label(root,text=Funcionario.getapellidofuncionario())
            ingresaApellidoFuncionario.place( x=793, y=240, width=270, height=20)
       

        
#*********************ENTRYS CLIENTE******************************************

#ttk.Entry(root)

ingresaRutCliente = ttk.Entry(root,textvariable=rut)
ingresaRutCliente.place( x=193, y=266, width=270, height=20)  


#************************ENTRYS FUNCIONARIO***********************************

ingresaRutFuncionario = ttk.Entry(root,textvariable=rutf)
ingresaRutFuncionario.place( x=793, y=266, width=270, height=20)  


#*******************BOTONES***************************************************


#------Depositar----

imagenDepositar = Image.open("./EDD/depositar.png")
imagenDepositar = ImageTk.PhotoImage(imagenDepositar)
botonDepositar = ttk.Button(canvas, image= imagenDepositar, command = abrirDepositar)
botonDepositar.place( x=81, y=404)



#------Retirar-----
imagenRetirar = Image.open("./EDD/retirar.png")
imagenRetirar = imagenRetirar.resize((50,44),Image.ANTIALIAS)
imagenRetirar = ImageTk.PhotoImage(imagenRetirar)
botonRetirar = ttk.Button(canvas, image= imagenRetirar, command = abrirRetirar)
botonRetirar.place( x=81, y=459)

#------Transferir-----
imagenTransferir = Image.open("./EDD/transferir.png")
imagenTransferir = imagenTransferir.resize((31,53),Image.ANTIALIAS)
imagenTransferir = ImageTk.PhotoImage(imagenTransferir)
botonTransferir = ttk.Button(canvas, image= imagenTransferir, command = abrirTransferir)
botonTransferir.place( x=88, y=509)

#------Prestamo-----

imagenPrestamo = Image.open("./EDD/prestamo.png")
imagenPrestamo = imagenPrestamo.resize((50,35),Image.ANTIALIAS)
imagenPrestamo = ImageTk.PhotoImage(imagenPrestamo)
botonPrestamo = ttk.Button(canvas, image= imagenPrestamo, command = abrirPrestamo)
botonPrestamo.place( x=81, y=570)



#------Analisis Estadisticos-----

imagenGrafico = Image.open("./EDD/grafico.png")
imagenGrafico= imagenGrafico.resize((50,46),Image.ANTIALIAS)
imagenGrafico = ImageTk.PhotoImage(imagenGrafico)
botonGrafico = ttk.Button(canvas, image= imagenGrafico, command = abrirGrafico)
botonGrafico.place( x=675, y=400)

#------Cola-----

imagenCola = Image.open("./EDD/atendido.png")
imagenCola= imagenCola.resize((65,55),Image.ANTIALIAS)
imagenCola = ImageTk.PhotoImage(imagenCola)
botonCola = ttk.Button(canvas, image= imagenCola, command = abrirMostrarCola)
botonCola.place( x=779, y=8)

#----------Confirmar---------
imagenConfirmaCliente1 = Image.open("./EDD/guardarCliente1.png")
imagenConfirmaCliente1 = ImageTk.PhotoImage(imagenConfirmaCliente1)
botonConfirmarCliente1 = ttk.Button(canvas, image= imagenConfirmaCliente1,command = ConfirmarDatos)
botonConfirmarCliente1.place( x=288, y=334)


imagenConfirmaFuncionario = Image.open("./EDD/guardarFuncionario.png")
imagenConfirmaFuncionario = ImageTk.PhotoImage(imagenConfirmaFuncionario)
botonConfirmarFuncionario = ttk.Button(canvas, image= imagenConfirmaFuncionario,command = Mostrardatosfun)
botonConfirmarFuncionario.place( x=884, y=334) 

#*****************************************************************************






#*****************************************************************************
root.mainloop() #Ejecución programa