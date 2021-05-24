from Cliente import *
class Banco(Cliente):
    def __init__(self, nombrebanco,rutbanco,telefonobanco,direccionbanco):
        self.nombrebanco="Banco Touch"
        self.rutbanco="45111111-7"
        self.telefonobanco=948463452
        self.direccionbanco="Calle Arturo Prat 461"
        self.cliente1=Cliente

    def setNombrebanco(self,nombrebanco):
        self.nombrebanco=nombrebanco
        
    def setRutbanco(self,rutbanco):
        self.rutbanco=rutbanco

    def setTelefonobanco(self,telefonobanco):
        self.telefonobanco=telefonobanco

    def setDireccionbanco(self,direccionbanco):
        self.direccionbanco=direccionbanco
    
  
    def getNombre(self):
        return self.nombrebanco

    def getRUT(self):
        return self.rutbanco

    def getfono(self):
        return self.telefonobanco

    def getDireccion(self):
        return self.direccionbanco

    def __str__(self):
        return "Nombre del banco:"+self.nombrebanco+"\n Rut del banco:"+self.rutbanco+"\n Telefono del banco:"+str(self.telefonobanco)+"\n Direccion del banco:"+self.direccionbanco

    def setAceptar(self,saldocliente):
        plata =('Aceptado','Rechazado')
        if saldocliente>300:
            return plata[0]
    
    def setRechazar(self,saldocliente):
        plata=('Aceptado','Rechazado')
        if saldocliente<300:
            return plata[1]

    def setAceptarPrestamo(self,saldocliente):
        Solicitud=('Aceptada','Rechazada')
        if saldocliente>100000:
            return Solicitud[0]

    def setRechazarPrestamo(self,saldocliente):
        Solicitud=('Aceptada','Rechazada')
        if saldocliente<100000:
            return Solicitud[1]
            print("H07A")