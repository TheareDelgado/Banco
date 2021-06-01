class Persona():
     def __init__(self):
        operaciones=["Sin Operacion","Depositar","Retirar","Transferir","Prestamo"]
        self.nombre=""
        self.apellido=""
        self.rut=""
        self.saldo = 0
        self.operacion= operaciones[0]
        self.N_atencion= 1
        
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
     def setN_atencion(self, N_atencion):
         self.N_atencion=N_atencion


 
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
     def getN_atencion(self):
         return self.N_atencion

     def __str__(self) :
         return self.nombre+" "+self.apellido+""+self.rut

