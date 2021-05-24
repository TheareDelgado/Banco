from Persona import *
import random
class Cliente(Persona):
    def __init__(self, nombrecliente,apellidocliente,rutcliente,clavecliente,saldocliente):
        Persona.__init__(nombrecliente,apellidocliente,rutcliente)
        self.clave=["3535","1212","1213","0213"]
        self.saldo=0

    def ponerClavecliente(self,clavecliente):
        self.clavecliente=clave

    def ponerSaldocliente(self,saldocliente):
        self.saldocliente=saldo

    def tomarClavecliente(self):
        return self.clavecliente

    