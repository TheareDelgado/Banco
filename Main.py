import tkinter 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Button
from Cliente import *
from Persona import *
import dispensador as D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors





root = Tk()
root.title("Banco") #Nombre que aparece en la ventana
root.geometry("1248x1543")  #Define tamaño de la ventana
root.resizable(width=False, height=False)
#DATOS RANDOMSSS
opciones=["1","2","3","4"]
#DATOS DE CLIENTE
rut=StringVar()
Rut=["203770936","20","202","202254472"]
Nombres=["Cesar","Felipe","Diego"," Theare"]
Apellidos=["Mora","Vera","Gutierrez","Delgado"]
saldo=(300000,600000,10000000,500000)
#DATOS DE FUNCIONARIO
rutf=StringVar()
Rutfu=["20377","20","202","20225"]
Nombresfu=["Albo","LUCA","Diego"," There"]
Apellidosfu=["FIX","Sancs","Gutierrez","Smith"]
#DATOS PRESTAMO
prestamosol=StringVar()
cantidadcuotas=StringVar()





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
    ventanaDepositar.geometry("1248x708")
    ventanaDepositar.resizable(width=False, height=False)


    imagen = PhotoImage (file = "./ventanaDepositar.png") 
    fondo=Label(ventanaDepositar, image = imagen).place( x=0, y=0)

    #Entry y Label

    ingresaCuentaDeposito = ttk.Entry(ventanaDepositar)
    ingresaCuentaDeposito.place_configure(x=842, y=353 , width=270, height=20)

    ingresaMontoDeposito = ttk.Entry(ventanaDepositar)
    ingresaMontoDeposito.place_configure(x=842, y=379 , width=270, height=20)


    imagenConfirmaCliente2 = Image.open("./guardarCliente2.png")
    imagenConfirmaCliente2 = ImageTk.PhotoImage(imagenConfirmaCliente2)
    botonConfirmarCliente2 = ttk.Button(ventanaDepositar, image= imagenConfirmaCliente2, command = ventanaDepositar.destroy)
    botonConfirmarCliente2.place( x=838, y=525)


    ventanaDepositar.mainloop()


def abrirRetirar():
    ventanaRetirar=Toplevel(root)
    ventanaRetirar.title("Retirar")
    ventanaRetirar.geometry("1248x708")
    ventanaRetirar.resizable(width=False, height=False)


    imagen = PhotoImage (file = "./ventanaDepositar.png") 
    fondo=Label(ventanaRetirar, image = imagen).place( x=0, y=0)


    ingresaCuentaRetiro = ttk.Entry(ventanaRetirar)
    ingresaCuentaRetiro.place_configure(x=842, y=353 , width=270, height=20)

    ingresaMontoRetiro = ttk.Entry(ventanaRetirar)
    ingresaMontoRetiro.place_configure(x=842, y=379 , width=270, height=20)


    imagenConfirmaCliente3 = Image.open("./guardarCliente2.png")
    imagenConfirmaCliente3 = ImageTk.PhotoImage(imagenConfirmaCliente3)
    botonConfirmarCliente3 = ttk.Button(ventanaRetirar, image= imagenConfirmaCliente3, command = ventanaRetirar.destroy)
    botonConfirmarCliente3.place( x=838, y=525)

    ventanaRetirar.mainloop()


def abrirTransferir():
    ventanaTransferir=Toplevel(root)
    ventanaTransferir.title("Transferir")
    ventanaTransferir.geometry("1248x708")
    ventanaTransferir.resizable(width=False, height=False)


    imagen = PhotoImage (file = "./ventanaTransferir.png") 
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


    imagenConfirmaCliente4 = Image.open("./guardarCliente2.png")
    imagenConfirmaCliente4 = ImageTk.PhotoImage(imagenConfirmaCliente4)
    botonConfirmarCliente4 = ttk.Button(ventanaTransferir, image= imagenConfirmaCliente4, command = ventanaTransferir.destroy)
    botonConfirmarCliente4.place( x=836, y=525)

    ventanaTransferir.mainloop()


def abrirPrestamo():
    ventanaPrestamo=Toplevel(root)
    ventanaPrestamo.title("Prestamo")
    ventanaPrestamo.geometry("1248x708")
    ventanaPrestamo.resizable(width=False, height=False)


    imagen = PhotoImage (file = "./ventanaPrestamo.png") 
    fondo=Label(ventanaPrestamo, image = imagen).place( x=0, y=0)

    ingresaMonto = ttk.Entry(ventanaPrestamo)
    ingresaMonto.place()


    ingresaMotivoPrestamo = ttk.Entry(ventanaPrestamo)
    ingresaMotivoPrestamo.place_configure(x=892, y=364 , width=270, height=20)

    ingresaMontoPrestamo = ttk.Combobox(ventanaPrestamo,values=("$150.000","$300.000","$600.000"),textvariable=prestamosol)
    ingresaMontoPrestamo.place_configure(x=893, y=389 , width=270, height=20)

    ingresaPresupuestoPrestamo = ttk.Entry(ventanaPrestamo)
    ingresaPresupuestoPrestamo.place_configure(x=892, y=415 , width=270, height=20)

    ingresaCuotaPrestamo = ttk.Combobox(ventanaPrestamo,values=("3","6","9"),textvariable=cantidadcuotas)
    ingresaCuotaPrestamo.place_configure(x=892, y=442 , width=270, height=20)


    imagenConfirmaCliente5 = Image.open("./guardarCliente2.png")
    imagenConfirmaCliente5 = ImageTk.PhotoImage(imagenConfirmaCliente5)
    botonConfirmarCliente5 = ttk.Button(ventanaPrestamo, image= imagenConfirmaCliente5, command = ventanaPrestamo.destroy)
    botonConfirmarCliente5.place( x=840, y=535)
    ventanaPrestamo.mainloop()


def abrirGrafico():
    #ventanaGrafico=Toplevel(root)
    #ventanaGrafico.title("Gráfico")
    #ventanaGrafico.geometry("1248x708")
    #ventanaGrafico.resizable(width=False, height=False)
    cantidadPrestamos = 10
    cantidadDepositos = 6
    cantidadRetirar = 4
    cantidadTransferencias = 0


    
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
    ventanaMostrarCola.geometry("1248x708")
    ventanaMostrarCola.resizable(width=False, height=False)

    tabla = ttk.Treeview(ventanaMostrarCola)
    tabla['columns']=("N° Cola", "Operación", "Nombre", "Apellido", "Rut")
    tabla.column('#0', width=0, stretch=NO)
    tabla.column('N° Cola',anchor=CENTER, width=50)
    tabla.column('Operación', anchor=CENTER, width=200)
    tabla.column('Nombre', anchor=CENTER, width=200)
    tabla.column('Apellido', anchor=CENTER, width=200)
    tabla.column("Rut", anchor=CENTER, width=200)

    tabla.heading('#0', text='', anchor=CENTER)
    tabla.heading('N° Cola', text='N° Cola', anchor=CENTER)
    tabla.heading('Operación', text='Operación', anchor=CENTER)
    tabla.heading('Nombre', text='Nombre', anchor=CENTER)
    tabla.heading('Apellido', text='Apellido', anchor=CENTER)
    tabla.heading("Rut", text="Rut", anchor=CENTER)

    tabla.pack()

    
    
    ventanaMostrarCola.mainloop()

#_---------------------------------------------------------------

#-------------------------------------------------------------------

                             #DEF RANDOMS


def Colass():
    dispensador.ListaDeEspera

def Prestamofinal():
    print("Se ah agragado a un cliente")
    D.ponerEnServicio.get()
    abrirPrestamo()


def ConfirmarDatos():
    if (rut.get()==Rut[0]):
        ingresaNombreCliente = ttk.Label(root, text=Nombres[0])
        ingresaNombreCliente.place(x=193, y=213, width=270, height=20)
        ingresaApellidoCliente = ttk.Label(root,text=Apellidos[0])
        ingresaApellidoCliente.place( x=193, y=240, width=270, height=20) 
        ingresaSaldoCliente = ttk.Label(root,text=saldo[0])
        ingresaSaldoCliente.place( x=193, y=292, width=270, height=20)
    elif (rut.get()==Rut[1]):
        ingresaNombreCliente = ttk.Label(root, text=Nombres[1])
        ingresaNombreCliente.place(x=193, y=213, width=270, height=20)
        ingresaApellidoCliente = ttk.Label(root,text=Apellidos[1])
        ingresaApellidoCliente.place( x=193, y=240, width=270, height=20) 
        ingresaSaldoCliente = ttk.Label(root,text=saldo[1])
        ingresaSaldoCliente.place( x=193, y=292, width=270, height=20)
    elif (rut.get()==Rut[2]):
        ingresaNombreCliente = ttk.Label(root, text=Nombres[2])
        ingresaNombreCliente.place(x=193, y=213, width=270, height=20)
        ingresaApellidoCliente = ttk.Label(root,text=Apellidos[2])
        ingresaApellidoCliente.place( x=193, y=240, width=270, height=20) 
        ingresaSaldoCliente = ttk.Label(root,text=saldo[2])
        ingresaSaldoCliente.place( x=193, y=292, width=270, height=20)
    elif (rut.get()==Rut[3]):
        ingresaNombreCliente = ttk.Label(root, text=Nombres[3])
        ingresaNombreCliente.place(x=193, y=213, width=270, height=20)
        ingresaApellidoCliente = ttk.Label(root,text=Apellidos[3])
        ingresaApellidoCliente.place( x=193, y=240, width=270, height=20) 
        ingresaSaldoCliente = ttk.Label(root,text=saldo[3])
        ingresaSaldoCliente.place( x=193, y=292, width=270, height=20)

def Mostrardatosfun():
    if(rutf.get()==Rutfu[0]):
        ingresaNombreFuncionario = ttk.Label(root,text=Nombresfu[0])                         
        ingresaNombreFuncionario.place( x=793, y=213, width=270, height=20)  
        ingresaApellidoFuncionario = ttk.Label(root,text=Apellidosfu[0])
        ingresaApellidoFuncionario.place( x=793, y=240, width=270, height=20)
    elif(rutf.get()==Rutfu[1]):
        ingresaNombreFuncionario = ttk.Label(root,text=Nombresfu[1])                         
        ingresaNombreFuncionario.place( x=793, y=213, width=270, height=20)  
        ingresaApellidoFuncionario = ttk.Label(root,text=Apellidosfu[1])
        ingresaApellidoFuncionario.place( x=793, y=240, width=270, height=20)
    elif(rutf.get()==Rutfu[2]):
        ingresaNombreFuncionario = ttk.Label(root,text=Nombresfu[2])                         
        ingresaNombreFuncionario.place( x=793, y=213, width=270, height=20)  
        ingresaApellidoFuncionario = ttk.Label(root,text=Apellidosfu[2])
        ingresaApellidoFuncionario.place( x=793, y=240, width=270, height=20)
    elif(rutf.get()==Rutfu[3]):
        ingresaNombreFuncionario = ttk.Label(root,text=Nombresfu[3])                         
        ingresaNombreFuncionario.place( x=793, y=213, width=270, height=20)  
        ingresaApellidoFuncionario = ttk-Label(root,text=Apellidosfu[3])
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

imagenDepositar = Image.open("./depositar.png")
imagenDepositar = ImageTk.PhotoImage(imagenDepositar)
botonDepositar = ttk.Button(canvas, image= imagenDepositar, command = abrirDepositar)
botonDepositar.place( x=81, y=404)



#------Retirar-----
imagenRetirar = Image.open("./retirar.png")
imagenRetirar = imagenRetirar.resize((50,44),Image.ANTIALIAS)
imagenRetirar = ImageTk.PhotoImage(imagenRetirar)
botonRetirar = ttk.Button(canvas, image= imagenRetirar, command = abrirRetirar)
botonRetirar.place( x=81, y=459)

#------Transferir-----
imagenTransferir = Image.open("./transferir.png")
imagenTransferir = imagenTransferir.resize((31,53),Image.ANTIALIAS)
imagenTransferir = ImageTk.PhotoImage(imagenTransferir)
botonTransferir = ttk.Button(canvas, image= imagenTransferir, command = abrirTransferir)
botonTransferir.place( x=88, y=509)

#------Prestamo-----

imagenPrestamo = Image.open("./prestamo.png")
imagenPrestamo = imagenPrestamo.resize((50,35),Image.ANTIALIAS)
imagenPrestamo = ImageTk.PhotoImage(imagenPrestamo)
botonPrestamo = ttk.Button(canvas, image= imagenPrestamo, command = Prestamofinal)
botonPrestamo.place( x=81, y=570)



#------Analisis Estadisticos-----

imagenGrafico = Image.open("./grafico.png")
imagenGrafico= imagenGrafico.resize((50,46),Image.ANTIALIAS)
imagenGrafico = ImageTk.PhotoImage(imagenGrafico)
botonGrafico = ttk.Button(canvas, image= imagenGrafico, command = abrirGrafico)
botonGrafico.place( x=675, y=400)

#------Cola-----

imagenCola = Image.open("./atendido.png")
imagenCola= imagenCola.resize((65,55),Image.ANTIALIAS)
imagenCola = ImageTk.PhotoImage(imagenCola)
botonCola = ttk.Button(canvas, image= imagenCola, command = abrirMostrarCola)
botonCola.place( x=779, y=8)

#----------Confirmar---------
imagenConfirmaCliente1 = Image.open("./guardarCliente1.png")
imagenConfirmaCliente1 = ImageTk.PhotoImage(imagenConfirmaCliente1)
botonConfirmarCliente1 = ttk.Button(canvas, image= imagenConfirmaCliente1,command = ConfirmarDatos)
botonConfirmarCliente1.place( x=288, y=334)


imagenConfirmaFuncionario = Image.open("./guardarFuncionario.png")
imagenConfirmaFuncionario = ImageTk.PhotoImage(imagenConfirmaFuncionario)
botonConfirmarFuncionario = ttk.Button(canvas, image= imagenConfirmaFuncionario,command = Mostrardatosfun)
botonConfirmarFuncionario.place( x=884, y=334) 

#*****************************************************************************






#*****************************************************************************
root.mainloop() #Ejecución programa