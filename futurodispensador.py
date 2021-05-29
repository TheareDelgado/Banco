from Main import Nombres
from Persona import *
from Cliente import *
from Operaciones import *
from Prestamo import *
Coladeposito=[]
Colaretirar=[]
ColaTransferir=[]
Colaprestamo=[]

class futurodispensador(Persona):
    def __init__(self,Nombre,Apellido,Rut):
        Persona.__init__(self,Nombre,Apellido,Rut)
        self.Nombre=Nombre
        self.Apellido=Apellido
        self.Rut=Rut
        return Persona

    def LlamarClientes(self):
        return self.Nombre + self.Apellido + self.Rut

    def operaciondeposito(self,Nombre,Apellido,Rut,Clave,saldo):
        A=Cliente(Nombre,Apellido,Rut,Clave,saldo)
          
    def IngresoaListas(self,ops):
        self.contadordepositos=0
        self.contadorretiros=0
        self.contadortrasnferencia=0
        self.contadorPrestamo=0
        self.posicion=self.posicion
        self.ops=ops
        if ops==1:
            Coladeposito.append(self.Nombre, self.Apellido)
            self.contadordepositos=self.contadordepositos+1
            return self.contadordepositos
        elif ops==2:
            Colaretirar.append(self.Nombre, self.Apellido)
            self.contadorretiros=self.contadorretiros+1
            return self.contadorretiros
        elif ops==3:
            ColaTransferir.append(self.Nombre, self.Apellido)
            self.contadortrasnferencia=self.contadortrasnferencia+1
            return self.contadortrasnferencia
        elif ops==4:
            Colaprestamo.append(self.Nombre, self.Apellido)
            self.contadorPrestamo=self.contadorPrestamo+1
            return self.contadorPrestamo

    def numerodeticekt(self):
        self.tiketdeposito=0
        self.tiketretirar=0
        self.tikettransferir=0
        self.tiketprestamo=0
        if self.ops==1:
            self.tiketdeposito=self.tiketdeposito+1
            return "Su turno es: "+self.tiketdeposito
        if self.ops==2:
            self.tiketretirar=self.tiketretirar+1
            return "Su turno es: "+self.tiketretirar
        if self.ops==3:
            self.tikettransferir=self.tikettransferir+1
            return "Su turno es: "+self.tikettransferir
        if self.ops==4:
            self.tiketprestamo=self.tiketprestamor+1
            return "Su turno es: "+self.tiketprestamo
