from pathlib import WindowsPath
import tkinter 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Button

from numpy import mat
from Cliente import *
from Persona import *
from dispensador import *
from Banco import *
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
from Funcionario import *

#Creando banco

#Creando personas
Aaaaaaa=1
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
p4.setRut("202254772")
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

operaciones=["Sin Operacion","Depositar","Retirar","Transferir","Prestamo"]


root = Tk()
root.title("Banco") #Nombre que aparece en la ventana
root.geometry("1248x708")  #Define tamaño de la ventana
root.resizable(width=False, height=False)
#DATOS RANDOMSSS
#opciones=["Sin Operacion","Depositar","Retirar","Transferir","Prestamo"]
#DATOS DE CLIENTE
rut=StringVar()

#DATOS DE FUNCIONARIO
rutf=StringVar()

#LLAMANDO A CLASES

#DATOS PRESTAMO
prestamosol=StringVar()
cantidadcuotas=StringVar()
A=[]
B=[]
cont1=1
cont2=1
cont3=1
cont4=1
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
    ventanaDepositar=Toplevel(root)
    ventanaDepositar.title("Depositar")
    ventanaDepositar.geometry("600x400")
    ventanaDepositar.resizable(width=False, height=False)
    global cont1
    def enDeposito():
        for persona in listadoPersonas.getLista():
            if (ingresaRutCliente.get()==persona.getRut()):
                persona.setOperacion(operaciones[1])
                listadoPersonas.agregarDeposito(persona)
                listadoPersonas.agregarTabla(persona)
                A.append("Depositar")
        
        global cont1
        B.append(cont1)  
        cont1=cont1+1              
        ventanaDepositar.destroy()

    imagen = PhotoImage (file = "./ventanaDepositar.png") 
    fondo=Label(ventanaDepositar, image = imagen).place( x=0, y=0)

    #Entry y Label

    ingresaCuentaDeposito = ttk.Entry(ventanaDepositar)
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
    global cont2

    def enRetirar():

        for persona in listadoPersonas.getLista():
            if (ingresaRutCliente.get()==persona.getRut()):
                persona.setOperacion(operaciones[2])
                listadoPersonas.agregarRetirar(persona)
                listadoPersonas.agregarTabla(persona)
                A.append("Retirar")

        global cont2
        B.append(cont2)   
        cont2=cont2+1
        ventanaRetirar.destroy()


    imagen = PhotoImage (file = "./ventanaDepositar.png") 
    fondo=Label(ventanaRetirar, image = imagen).place( x=0, y=0)


    ingresaCuentaRetiro = ttk.Entry(ventanaRetirar)
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
    global cont3

    def enTransferir():

        for persona in listadoPersonas.getLista():
            if (ingresaRutCliente.get()==persona.getRut()):
                persona.setOperacion(operaciones[3])
                listadoPersonas.agregarTransferir(persona)
                listadoPersonas.agregarTabla(persona)
                A.append("Transferir")
                 
        global cont3
        B.append(cont3)         
        cont3=cont3+1
        ventanaTransferir.destroy()


    imagen = PhotoImage (file = "./ventanaTransferir.png") 
    fondo=Label(ventanaTransferir, image = imagen).place( x=0, y=0)





    ingresaNombreTransferir = ttk.Entry(ventanaTransferir)
    ingresaNombreTransferir.place_configure(x=416, y=133 , width=169, height=17)

    ingresaApellidoTransferir = ttk.Entry(ventanaTransferir)
    ingresaApellidoTransferir.place_configure(x=416, y=160 , width=169, height=17)

    ingresaCorreoTransferir = ttk.Entry(ventanaTransferir)
    ingresaCorreoTransferir.place_configure(x=416, y=190 , width=169, height=17)

    ingresaCuentaTransferir = ttk.Entry(ventanaTransferir)
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
    ventanaPrestamo.title("Prestamo")
    ventanaPrestamo.geometry("600x400")
    ventanaPrestamo.resizable(width=False, height=False)
    global cont4
   

    def enPrestamo():

        for persona in listadoPersonas.getLista():
            if (ingresaRutCliente.get()==persona.getRut()):
                persona.setOperacion(operaciones[4])
                listadoPersonas.agregarPrestamo(persona)
                listadoPersonas.agregarTabla(persona)
                A.append("Prestamo")

        global cont4
        B.append(cont4)    
        cont4=cont4+1
        ventanaPrestamo.destroy()


    imagen = PhotoImage (file = "./ventanaPrestamo.png") 
    fondo=Label(ventanaPrestamo, image = imagen).place( x=0, y=0)

    ingresaMonto = ttk.Entry(ventanaPrestamo)
    ingresaMonto.place()
    


    ingresaMotivoPrestamo = ttk.Entry(ventanaPrestamo)
    ingresaMotivoPrestamo.place_configure(x=416, y=201 , width=169, height=17)

    ingresaMontoPrestamo = ttk.Combobox(ventanaPrestamo,values=("$150.000","$300.000","$600.000"),textvariable=prestamosol)
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
    ventanaGrafico=Toplevel(root)
    ventanaGrafico.title("Análisis esttadísticos")
    ventanaGrafico.geometry("1248x708")
    ventanaGrafico.resizable(width=False, height=False)






    ventanaGrafico.mainloop()
#Si una de las variables es 0 que no muestre el label y solo muestre las otras operaciones!!!




    #ventanaGrafico.mainloop()


def abrirMostrarCola():

    def elimina():
        x = tabla.selection()
        tabla.delete(x)
        global contadortabla
        contadortabla=True
    def finzalizaProceso():
        seleccionado = tabla.focus()
        if str(seleccionado)=="I001":
          valuess = tabla.item(seleccionado, text="", values=(B[0],A[0],ru[0],"Finalizado"))
        elif str(seleccionado)=="I002":
          valuess = tabla.item(seleccionado, text="", values=(B[1],A[1],ru[1],"Finalizado"))
        elif str(seleccionado)=="I003":
          valuess = tabla.item(seleccionado, text="", values=(B[2],A[2],ru[2],"Finalizado"))
        elif str(seleccionado)=="I004":
          valuess = tabla.item(seleccionado, text="", values=(B[3],A[3],ru[3],"Finalizado"))
        elif str(seleccionado)=="I005":
          valuess = tabla.item(seleccionado, text="", values=(B[4],A[4],ru[4],"Finalizado"))
        elif str(seleccionado)=="I006":
          valuess = tabla.item(seleccionado, text="", values=(B[5],A[5],ru[5],"Finalizado"))
        elif str(seleccionado)=="I007":
          valuess = tabla.item(seleccionado, text="", values=(B[6],A[6],ru[6],"Finalizado"))
        elif str(seleccionado)=="I008":
          valuess = tabla.item(seleccionado, text="", values=(B[7],A[7],ru[7],"Finalizado"))
        elif str(seleccionado)=="I009":
          valuess = tabla.item(seleccionado, text="", values=(B[8],A[8],ru[8],"Finalizado"))
        elif str(seleccionado)=="I010":
          valuess = tabla.item(seleccionado, text="", values=(B[9],A[9],ru[9],"Finalizado"))
        elif str(seleccionado)=="I011":
          valuess = tabla.item(seleccionado, text="", values=(B[10],A[10],ru[10],"Finalizado"))
    


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
    botonEliminar = ttk.Button(ventanaMostrarCola, image= imagenEliminar, command = elimina)
    botonEliminar.place( x=827, y=70)

    imagenFinalizar = Image.open("./finalizarServicio.png")
    imagenFinalizar = ImageTk.PhotoImage(imagenFinalizar)
    botonFinalizar = ttk.Button(ventanaMostrarCola, image= imagenFinalizar, command = finzalizaProceso)
    botonFinalizar.place( x=827, y=153)

    imagenActualizar = Image.open("./actualizar.png")
    imagenActualizar = ImageTk.PhotoImage(imagenActualizar)
    botonActualizar = ttk.Button(ventanaMostrarCola, image= imagenActualizar)
    botonActualizar.place( x=827, y=233)


    #La idea que tenemos para los botones eliminar, actualizar y finalizar es que al apretarse cualquiera de estos botones
    #aparezca un nuevo topLevel (uno por cada botón) que pida RUT junto a un botón de confirmar, de modo que si el rut coincide con uno de los que están
    #registrados, la operación se realice, de otro modo, aparezca un mensaje de que la operación/rut es inválido (showmessage)



    FiltrarOperaciones = ttk.Combobox(ventanaMostrarCola,values=("Depositar","Trasnferir","Retirar","Prestamo"),textvariable=FiltroOp)
    FiltrarOperaciones.place_configure(x=199, y=326 , width=280, height=20)

    FiltrarEstados = ttk.Combobox(ventanaMostrarCola,values=("Aceptado","Rechazado","En proceso"),textvariable=FiltroEs)
    FiltrarEstados.place_configure(x=199, y=349 , width=280, height=20)

    
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
    for persona in listadoPersonas.getListaTabla():
        ru.append(persona.getRut())
        num=n
        est="En proceso"
        fin="Finalizado"
        tabla.insert("",END,text="",values=(B[m],A[I],ru[b],est))
        n=n+1
        I=I+1
        b=b+1
        m=m+1
        global contadortabla
        if contadortabla==True:
            elimina()
    ventanaMostrarCola.mainloop()


#-------------------------------------------------------------------

                             #DEF RANDOMS

def ConfirmarDatos():
    for persona in listadoPersonas.getLista():
        if (ingresaRutCliente.get()==persona.getRut()):
            ingresaNombreCliente = ttk.Label(root, text=persona.getNombre(), background="gray")
            ingresaNombreCliente.place(x=187, y=213, width=270, height=20)
            ingresaApellidoCliente = ttk.Label(root,text=persona.getApellido(), background="gray")
            ingresaApellidoCliente.place( x=187, y=240, width=270, height=20)
            ingresaSaldoCliente = ttk.Label(root,text=persona.getSaldo(), background="gray")
            ingresaSaldoCliente.place( x=187, y=292, width=270, height=20)
       
def Mostrardatosfun():
    for Funcionario in listadoPersonas.getListaFuncionarios():
        if (ingresaRutFuncionario.get()==Funcionario.getrutfuncionario()):
            ingresaNombreFuncionario = ttk.Label(root,text=Funcionario.getnombrefuncionario(), background="gray")                         
            ingresaNombreFuncionario.place( x=782, y=213, width=270, height=20)  
            ingresaApellidoFuncionario = ttk.Label(root,text=Funcionario.getapellidofuncionario(), background="gray")
            ingresaApellidoFuncionario.place( x=782, y=239, width=270, height=20)
       

        
#*********************ENTRYS CLIENTE******************************************

#ttk.Entry(root)

ingresaRutCliente = ttk.Entry(root,textvariable=rut)
ingresaRutCliente.place( x=187, y=266, width=270, height=20)  


#************************ENTRYS FUNCIONARIO***********************************

ingresaRutFuncionario = ttk.Entry(root,textvariable=rutf)
ingresaRutFuncionario.place( x=782, y=265, width=270, height=20)  


#*******************BOTONES***************************************************


#------Depositar----

imagenDepositar = Image.open("./depositar.png")
imagenDepositar = ImageTk.PhotoImage(imagenDepositar)
botonDepositar = ttk.Button(canvas, image= imagenDepositar, command = abrirDepositar)
botonDepositar.place( x=15, y=445)



#------Retirar-----
imagenRetirar = Image.open("./retirar.png")
imagenRetirar = ImageTk.PhotoImage(imagenRetirar)
botonRetirar = ttk.Button(canvas, image= imagenRetirar, command = abrirRetirar)
botonRetirar.place( x=15, y=536)

#------Transferir-----
imagenTransferir = Image.open("./transferir.png")
#imagenTransferir = imagenTransferir.resize((31,53),Image.ANTIALIAS)
imagenTransferir = ImageTk.PhotoImage(imagenTransferir)
botonTransferir = ttk.Button(canvas, image= imagenTransferir, command = abrirTransferir)
botonTransferir.place( x=329, y=437)

#------Prestamo-----

imagenPrestamo = Image.open("./prestamo.png")
#imagenPrestamo = imagenPrestamo.resize((50,35),Image.ANTIALIAS)
imagenPrestamo = ImageTk.PhotoImage(imagenPrestamo)
botonPrestamo = ttk.Button(canvas, image= imagenPrestamo, command = abrirPrestamo)
botonPrestamo.place( x=312, y=540)



#------Analisis Estadisticos-----

imagenGrafico = Image.open("./grafico.png")
#imagenGrafico= imagenGrafico.resize((50,46),Image.ANTIALIAS)
imagenGrafico = ImageTk.PhotoImage(imagenGrafico)
botonGrafico = ttk.Button(canvas, image= imagenGrafico, command = abrirGrafico)
botonGrafico.place( x=747, y=440)

#------Cola-----

imagenCola = Image.open("./atendido.png")
imagenCola= imagenCola.resize((65,55),Image.ANTIALIAS)
imagenCola = ImageTk.PhotoImage(imagenCola)
botonCola = ttk.Button(canvas, image= imagenCola, command = abrirMostrarCola)
botonCola.place( x=776, y=8)

#----------Confirmar---------
imagenConfirmaCliente1 = Image.open("./guardarCliente1.png")
imagenConfirmaCliente1 = ImageTk.PhotoImage(imagenConfirmaCliente1)
botonConfirmarCliente1 = ttk.Button(canvas, image= imagenConfirmaCliente1,command = ConfirmarDatos)
botonConfirmarCliente1.place( x=278, y=329)


imagenConfirmaFuncionario = Image.open("./guardarFuncionario.png")
imagenConfirmaFuncionario = ImageTk.PhotoImage(imagenConfirmaFuncionario)
botonConfirmarFuncionario = ttk.Button(canvas, image= imagenConfirmaFuncionario,command = Mostrardatosfun)
botonConfirmarFuncionario.place( x=870, y=334) 

#*****************************************************************************





#*****************************************************************************
root.mainloop() #Ejecución programa