#ESTA CLASE SE DEBE REHACER CON LAS NUEVAS LISTAS Y MUCHOS MAS DEF
from Persona import *
from Cliente import *
from Operaciones import *
from Prestamo import *
class dispensador(Persona):
    def __init__(self,Nombre,Apellido,Rut,clave,saldo):
        Persona.__init__(self,Nombre,Apellido,Rut)
        self.contadorpersonas=0

    def DatosClientes(self,Nombre,Apellido,Rut):
            self.Nombre=Persona.tomarNombrepersona
            self.Apellido=Persona.tomarApellidopersona
            self.Rut=Persona.tomarRutpersona

    def Clientess(self):
            return self.Nombre
            return self.Apellido
            return self.Rut

    def ponerEnServicio(self,Nombre,Apellido,Rut,Clave,saldo,op,PA,PB):
            self.PA=[]
            self.PB=[]
            self.op=op
            A=Cliente(Nombre,Apellido,Rut,Clave,saldo)
            if  saldo>=500000:
                PA.append(A.ClientesEnCola)
                return (A.ClientesEnCola)
            elif  saldo<500000:
                PB.append(A.ClientesEnCola)
                return (A.ClientesEnCola)
            elif op==4:
                PA.append(A.ClientesEnCola)
                return (A.ClientesEnCola)
            elif   op!=4:
                PB.append(A.ClientesEnCola)
                return (A.ClientesEnCola)
                


    def ListaDeEspera(self,cont):
            self.cont=0
            self.sumadorB=0
            self.sumadorA=0
            for i in range(1,101,1):
                cont=cont+1
                if i%3!=0:
                    return print ("A" + PA[sumadorA] + " Su posicion es " + cont)
                    sumadorA=sumadorA+1
                    contadorpersonas=comtadorpersonas+1
                else:
                    return print ("B" + PB[sumadorB] + " Su posicion es " + cont)
                    sumadorB=sumadorB+1
                    contadorpersonas=comtadorpersonas+1
            return print("En total se atendieron un total de : "+ contadorpersonas+ " de personas")
    
#DEF PARA PARA OPERACION REALIZADA
    def numerodeticekt(self):
        self.tiketdeposito=0
        self.tiketretirar=0
        self.tikettransferir=0
        self.tiketprestamo=0
        if self.ops==1:
            self.tiketdeposito=self.tiketdeposito+1
            return "Su ticket es: "+self.tiketdeposito
        if self.ops==2:
            self.tiketretirar=self.tiketretirar+1
            return "Su ticket es: "+self.tiketretirar
        if self.ops==3:
            self.tikettransferir=self.tikettransferir+1
            return "Su ticket es: "+self.tikettransferir
        if self.ops==4:
            self.tiketprestamo=self.tiketprestamor+1
            return "Su ticket es: "+self.tiketprestamo
#----------------------------------------------------------------------------
    #####FIN DEFS CONTADORES
#----------------------------------------------------------------------------       

#INICIO DEFS CONTADOR DE DINERO POR CADA OPERACION
       
