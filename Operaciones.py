from Persona import *

class Operaciones():
    def __init__(self):
     self.nombreop=""
     self.apellidoop=""
     self.rutop=""

     self.claveop=0
     self.saldoop=0
     self.vrut=0
     self.monto=0
     self.montor=0
    def setNombreop(self,nombreop):
         self.nombreop=nombreop
    def setApellidoop(self,apellidoop):
         self.apellidoop=apellidoop        
    def setRutop(self,rutop):
         self.rutop=rutop
    def setSaldoop(self,saldoop):
        self.saldoop=saldoop
    def setVrut(self,vrut):
        self.vrut=vrut
    def setMonto(self,monto):
          self.monto=monto
    def setMontor(self,montor):
         self.montor=montor
    def setClave(self,claveop):
         self.claveop=claveop 
 
    def getNombreop(self):
         return self.nombreop          
    def getApellidoop(self):
         return self.apellidoop
    def getRutop(self):
         return self.rutop
    def getSaldoop(self):
         return self.saldoop
    def getvrut(self):
         return self.vrut
    def getmonto(self):
         return self.monto
    def getMontor(self):
         return self.montor 
    def getClave(self):
         return self.claveop   
 
    def depositar (self, rutop,saldoop,monto,vrut):
          self.saldoop=saldoop+self.monto
          return self.saldoop

    def retirar (self, rutop, saldoop,montor, vrut):
            self.saldoop=saldoop-self.montor
            return self.saldoop

    def TransferirUsuario(self, vrut, clave, saldoop, montor):
            self.saldoop=saldoop-self.montor
            return self.saldoop
    def TransferirCliente(self, vrut,saldoop, montor):
            self.saldoop=saldoop+self.montor
            return self.saldoop
 
