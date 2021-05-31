class Persona():
     def __init__(self):
        self.nombre=""
        self.apellido=""
        self.rut=""
        self.saldo = 0
        self.operacion= ""
        
        #AGREGAR PONER Y TOMAR DE SALDO Y OP

     def setNombre(self,nombre):
         self.nombre=nombre
     def setApellido(self,apellido):
         self.apellido=apellido        
     def setRut(self,rut):
         self.rut=rut
     def setSaldo(self, saldo):
         self.saldo=saldo
     def setOperacion(self, operacion):
         self.operacion=operacion


 
     def getNombre(self):
         return self.nombre          
     def getApellido(self):
         return self.apellido
     def getRut(self):
         return self.rut
     def getSaldo(self):
         return self.saldo
     def getOperacion(self):
         return self.operacion

     def __str__(self) :
         return self.nombre+" "+self.apellido+""+self.rut

