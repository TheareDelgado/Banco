from Cliente import *
from Prestamo import *
from Persona import *
class dispensador(Cliente):
    def __init__(self,Nombre,Apellido,Rut,clave,saldo,Cantidadpres,cantidadCuo,Interes):
        Cliente.__init__(self,Nombre,Apellido,Rut,clave,saldo)
        self.contadorpersonas=0
        def DatosCliente(self,Nombre,Apellido,Rut):
            self.Nombre=Persona.tomarNombrepersona
            self.Apellido=Persona.tomarApellidopersona
            self.Rut=Persona.tomarRutpersona

        def Clientess(self):
            return self.Nombre
            return self.Apellido
            return self.Rut

        def ponerEnServicio(self,saldo,op):
            self.PA=[]
            self.PB=[]
            self.op=0
            if  saldo>=500000:
                self.PA.append(Clientess)
            elif  saldo<500000:
                self.PB.append(Clientess)
            elif op==4:
                self.PA.append(Clientess)
            elif   op!=4:
                self.PB.append(Clientess)
                


        def ListaDeEspera(self):
            self.cont=0
            self.sumadorB=0
            self.sumadorA=0
            for i in range(1,101,1):
                cont=cont+1
                if i%3!=0:
                    return print ("A" + self.PA[sumadorA] + " Su posicion es " + cont)
                    sumadorA=sumadorA+1
                    contadorpersonas=comtadorpersonas+1
                else:
                    return print ("B" + self.PB[sumadorB] + " Su posicion es " + cont)
                    sumadorB=sumadorB+1
                    contadorpersonas=comtadorpersonas+1
            return print("En total se atendieron un total de : "+ contadorpersonas+ " de personas")



            
        
                
                
        
        
        
