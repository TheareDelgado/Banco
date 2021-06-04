from Persona import *
class Cliente():
    def __init__(self):
        self.clavecliente=0
        self.saldocliente=0

    def ponerClavecliente(self,clavecliente):
        self.clavecliente=clavecliente

    def ponerSaldocliente(self,saldocliente):
        self.saldocliente=saldocliente
    def setNombre(self,nombre):
         self.nombre=nombre
    def setApellido(self,apellido):
         self.apellido=apellido        
    def setRut(self,rut):
         self.rut=rut

    def tomarClavecliente(self):
        return self.clavecliente
    def tomarSaldoCliente(self):
        return self.saldocliente
    def getNombre(self):
         return self.nombre          
    def getApellido(self):
         return self.apellido
    def getRut(self):
         return self.rut
    
    def ClientesEnCola(self,nombrecliente,apellidocliente,rutcliente,clavecliente,saldocliente):
        return ("Cliente : "+ nombrecliente+ " " + apellidocliente +" Con rut : "+ str(rutcliente) +" y SALDO : "+ str(saldocliente))
