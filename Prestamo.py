from Persona import *
class Prestamo(Persona):
    def __init__(self, nombrepersona,apellidopersona,rutpersona,clave,saldo,Cantidadpres,cantidadCuo,Interes,estadoPrestamo):
        Persona.__init__(self,nombrecliente,apellidocliente,rutcliente,clavecliente,saldocliente)
        self.Cantidadpres=Cantidadpres
        self.cantidadCuo=cantidadCuo
        self.interes=Interes
        self.estadoPrestamo=estadoPrestamo
#getter
    def getCantidadPrestamo(self):
        return self.Cantidadpres
    def getCantidadCuotas(self):
        return self.cantidadCuo
    def getInterese(self):
        return self.interes
    def getEstados(self):
        return self.estadoPrestamo

#setter
    def setCantidadPrestamo(self,Cantidadpres):
        self.Cantidadpres=Cantidadpres
    def setCantidadCuotas(self,cantidadCuo):
        self.cantidadCuo=cantidadCuo
    def setIntereses(self,Interes):
        self.interes=Interes
    def setEstados(self,estadoPrestamo):
        self.estadoPrestamo=estadoPrestamo
#------------------------------------------------------
#------------------------------------------------------
    def ponerCantidadPres(self,Cantidadpres):
            Prestamo=('150000','300000','600000')
            if Cantidadpres==1:
                return Prestamo[0]
            elif Cantidadpres==2:
                return Prestamo[1]
            elif Cantidadpres==3:
                return Prestamo[2]

    def ponerCantidadCuotas(self,cantidadCuo):
            Cuotas=('3','6','9')
            if Cantidadcuo==1:
                return Cuotas[0]
            elif Cantidadcuo==2:
                return Cuotas[1]
            elif Cantidadcuo==3:
                return Cuotas[2]

    def saberestadoprestamo(self,estadoPrestamo):
            if self.estadoPrestamo==False:
                return activarprestamo()
            else:
                return "Ya tiene un prestamo"


    def activarprestamo(self,Cantidadpres,cantidadCuo):
            if Cantidadpres==150000 and cantidadCuo==3:
                self.estadoPrestamo=True
                pagomensual=Cantidadpres/cantidadCuo
                interes=Prestamo*0.1
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Cantidadpres==150000 and cantidadCuo==6:
                self.estadoPrestamo=True
                pagomensual=Cantidadpres/cantidadCuo
                interes=Prestamo*0.2
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Cantidadpres==150000 and cantidadCuo==9:
                self.estadoPrestamo=True
                pagomensual=Cantidadpres/cantidadCuo
                interes=Prestamo*0.3
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Cantidadpres==300000 and cantidadCuo==3:
                self.estadoPrestamo=True
                pagomensual=Cantidadpres/cantidadCuo
                interes=Prestamo*0.1
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Cantidadpres==300000 and cantidadCuo==6:
                self.estadoPrestamo=True
                pagomensual=Cantidadpres/cantidadCuo
                interes=Prestamo*0.2
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Cantidadpres==300000 and cantidadCuo==9:
                self.estadoPrestamo=True
                pagomensual=Cantidadpres/cantidadCuo
                interes=Prestamo*0.3
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Cantidadpres==600000 and cantidadCuo==3:
                self.estadoPrestamo=True
                pagomensual=Cantidadpres/cantidadCuo
                interes=Prestamo*0.1
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Cantidadpres==600000 and cantidadCuo==6:
                self.estadoPrestamo=True
                pagomensual=Cantidadpres/cantidadCuo
                interes=Prestamo*0.2
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Cantidadpres==600000 and cantidadCuo==9:
                self.estadoPrestamo=True
                pagomensual=Cantidadpres/cantidadCuo
                interes=Prestamo*0.3
                pagofinal=pagomensual+Interes
                return pagofinal
                
                


        
