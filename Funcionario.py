from Persona import *
from dispensador import*
class Funcionario():
     def __init__(self, ):
        Persona.__init__(self)
     def __str__(self):
            return self.nombrefuncionario+" "+self.apellidofuncionario+" "+self.rutfuncionario
     def setnombrefuncionario(self,nombrefuncionario):
         self.nombrefuncionario=nombrefuncionario
     def setapellidofuncionario(self,apellidofuncionario):
         self.apellidofuncionario=apellidofuncionario       
     def setrutfuncionario(self,rutfuncionario):
         self.rutfuncionario=rutfuncionario

 
     def getnombrefuncionario(self):
         return self.nombrefuncionario         
     def getapellidofuncionario(self):
         return self.apellidofuncionario
     def getrutfuncionario(self):
         return self.rutfuncionario


     def __str__(self) :
         return self.nombrefuncionario +" "+self.apellidofuncionario+""+self.rutfuncionario

        #def TomarDatos():
           #return dispensador.ListaDeEspera(get.contadorpersonas)
           