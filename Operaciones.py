from Cliente import *

class Operaciones(Cliente):
    def __init__(self, nombrecliente, apellidocliente, rutcliente, clavecliente, saldocliente):
     Cliente.__init__(self,nombrecliente, apellidocliente, rutcliente, clavecliente, saldocliente)
     self.nombreop=nombrecliente
     self.apellidoop=apellidocliente
     self.rutop=rutcliente

     self.claveop=clavecliente
     self.saldoop=saldocliente

     def depositar (self, rut, monto, saldo,vrut):
        vrut=str(input("ingrese su rut sin puntos ni guion"))
        monto=int(input("ingrese monto que quiere depositar"))
        if vrut==rut:
                  saldo=saldo+monto
                  return print ("Su nuevo saldo es : "+ saldo)

        else:
                  return print ("no se puede depositar el monto debido a que el rut no es valido")

     def retirar (self, rut, clave, montor, saldo, vrut, vclave):
        vrut=str(input("ingrese su rut sin puntos ni guion"))
        vclave=int(input("ingrese su clave de 4 digitos"))
        montor=int(input("ingrese monto que quiere retirar de su cuenta"))

        if vrut == rut and vclave == clave and montor < saldo:
            saldo=saldo-montor
            return print ("Su nuevo saldo es : "+ saldo)

     def Transferir(self, rut, clave, saldo, montor, rutd):
        montor=int(input("ingrese monto el cual quiere transferir de su cuenta"))
        rutd=int(input("ingrese el rut del destinatario"))
        if validarut == true and montor<saldo:
            rutd=rutd+montor
            return print ("se ha depositado con exito un monto de "+ montor+ "al rut  : "+ rutd)