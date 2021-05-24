from Persona import *
from dispensador import*
class Funcionario(Persona):
    def __init__(self, nombrefuncionario,apellidofuncionario,rutfuncionario):
        Persona.__init__(self,nombrefuncionario,apellidofuncionario,rutfuncionario)
        def __str__(self):
            return self.nombrefuncionario+" "+self.apellidofuncionario+" "+self.rutfuncionario

        def TomarDatos():
           return dispensador.ListaDeEspera(get.contadorpersonas)
           