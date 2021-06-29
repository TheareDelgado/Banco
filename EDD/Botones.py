import numpy as np 

import pylab as pl 

from pandasgui import show

import pandas as pd

from tkinter import *

from tkinter import font

from tkinter import messagebox

#pip install Pillow

from PIL import Image,ImageTk

from tkinter import ttk

from tkinter import font

from time import sleep

import time

from datetime import date

from datetime import datetime
#Día y Fecha actual

Day = date.today()

fechaHoy = datetime.now()

cPrincipal = Tk()

cPrincipal.title("Banco")

cPrincipal.geometry('1920x2373')



# Background

img = PhotoImage(file="./etd/bank1.png")

etiquetaIcono = Label(cPrincipal,image=img)

etiquetaIcono.grid(row=0,column=0)

#Fuentes para presentaciones en label, button ...

fuente0 = font.Font(family="Bradley Hand ITC", size=30, weight="bold")

fuente1 = font.Font(family="Times New Roman", size=20, weight="bold")

fuente2 = font.Font(family="Calibri", size=19, weight="bold")

fuente3 = font.Font(family="Times New Roman", size=15, weight="bold")

fuente4 = font.Font(family="Times New Roman", size=12, weight="bold")



eT1= Label(cPrincipal,fg="black",font=fuente0,text="Universidad Central - Aplicaciones").place(x=550,y=8)

# Botón Limpiar campos

bLimpiar = Image.open('./botones/limpiar.png')

bLimpiar = bLimpiar.resize((90, 80), Image.ANTIALIAS)

bLimpiar = ImageTk.PhotoImage(bLimpiar)

botonLimp = Button(cPrincipal,font=fuente3, image=bLimpiar,fg="black",command=limpiar).place(x=720,y=240)

# mostrar montos y vuelto

mPagar=    IntVar()

Vuelto     =    IntVar()

ponerMonto=Entry(cPrincipal,state="readonly",textvariable=mPagar).place(x=800,y=90) #Monto a pagar

ponerVuelto=Entry(cPrincipal,state="readonly",textvariable=Vuelto).place(x=800,y=200) #Vuelto

# mostrar montos y vueltomPagar=    IntVar()Vuelto     =    IntVar()ponerMonto=Entry(cPrincipal,state="readonly",textvariable=mPagar).place(x=800,y=90) #Monto a pagarponerVuelto=Entry(cPrincipal,state="readonly",textvariable=Vuelto).place(x=800,y=200) #Vuelto

# mostrar estadisticasbVendidos= Image.open('./botones/vendidos.png')bVendidos = bVendidos.resize((90, 80), Image.ANTIALIAS)bVendidos = ImageTk.PhotoImage(bVendidos)eT8= Label(cPrincipal,font=fuente2,fg="black",text="Ventas Realizadas").place(x=950,y=50)botonV= Button (cPrincipal, font=fuente4,text="Vendido", image=bVendidos,fg="black",command=estadisticasVentas).place(x=920,y=240)eT8=Label(cPrincipal, fg="Blue",text="Total Tazas :").place(x=950,y=140)eT9=Label(cPrincipal, fg="Blue",text="Monto : $").place(x=950,y=160)eT10=Label(cPrincipal, fg="Blue",text="Mocachino:").place(x=950,y=80)eT11=Label(cPrincipal, fg="Blue",text="Taiwan:").place(x=950,y=100)eT12=Label(cPrincipal, fg="Blue",text="Luna Llena:").place(x=950,y=120)


cPrincipal.mainloop()