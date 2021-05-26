from Persona import *
class Cliente(Persona):
    def __init__(self, nombrecliente,apellidocliente,rutcliente,clavecliente,saldocliente):
        Persona.__init__(self,nombrecliente,apellidocliente,rutcliente)
        self.clavecliente=clavecliente
        self.saldocliente=saldocliente

    def ponerClavecliente(self,clavecliente):
        self.clavecliente=clavecliente

    def ponerSaldocliente(self,saldocliente):
        self.saldocliente=saldocliente

    def tomarClavecliente(self):
        return self.clavecliente
    def tomarSaldoCliente(self):
        return self.saldocliente
    
    def ClientesEnCola(self,nombrecliente,apellidocliente,rutcliente,clavecliente,saldocliente):
        return ("Cliente : "+ nombrecliente+ " " + apellidocliente +" Con rut : "+ str(rutcliente) +" y SALDO : "+ str(saldocliente))
