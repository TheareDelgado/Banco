from Cliente import *
class Prestamo(Persona):
    def __init__(self, nombrepersona,apellidopersona,rutpersona,clave,saldo,Cantidadpres,cantidadCuo,Interes,estadoPrestamo):
        Cliente.__init__(self,nombrecliente,apellidocliente,rutcliente,clavecliente,saldocliente)
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

        def saberestadoprestamo():
            if self.estadoPrestamo==False:
                return activarprestamo()
            else:
                return "Ya tiene un prestamo"


        def activarprestamo():
            if Prestamo==150000 and Cuotas==3:
                self.estadoPrestamo=True
                pagomensual=Prestamo/Cuotas
                interes=Prestamo*0.1
                self.Interes=interes
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Prestamo==150000 and Cuotas==6:
                self.estadoPrestamo=True
                pagomensual=Prestamo/Cuotas
                interes=Prestamo*0.2
                self.Interes=interes
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Prestamo==150000 and Cuotas==9:
                self.estadoPrestamo=True
                pagomensual=Prestamo/Cuotas
                interes=Prestamo*0.3
                self.Interes=interes
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Prestamo==300000 and Cuotas==3:
                self.estadoPrestamo=True
                pagomensual=Prestamo/Cuotas
                interes=Prestamo*0.1
                self.Interes=interes
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Prestamo==300000 and Cuotas==6:
                self.estadoPrestamo=True
                pagomensual=Prestamo/Cuotas
                interes=Prestamo*0.2
                self.Interes=interes
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Prestamo==300000 and Cuotas==9:
                self.estadoPrestamo=True
                pagomensual=Prestamo/Cuotas
                interes=Prestamo*0.3
                self.Interes=interes
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Prestamo==600000 and Cuotas==3:
                self.estadoPrestamo=True
                pagomensual=Prestamo/Cuotas
                interes=Prestamo*0.1
                self.Interes=interes
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Prestamo==600000 and Cuotas==6:
                self.estadoPrestamo=True
                pagomensual=Prestamo/Cuotas
                interes=Prestamo*0.2
                self.Interes=interes
                pagofinal=pagomensual+Interes
                return pagofinal
            elif Prestamo==600000 and Cuotas==9:
                self.estadoPrestamo=True
                pagomensual=Prestamo/Cuotas
                interes=Prestamo*0.3
                self.Interes=interes
                pagofinal=pagomensual+Interes
                return pagofinal
                
                


        
