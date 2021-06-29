

from Persona import *
from Cliente import *
from Operaciones import *
from Prestamo import *


class Dispensador():
    def __init__(self):
        self.listaPersonas=[]
        self.Coladeposito=[]
        self.Colaretirar=[]
        self.Colatransferir=[]
        self.colaprestamo=[] 
        self.listaTabla=[]
        self.listaOperacion=[] 
        self.listaFuncionarios=[]

    def agregarFuncionarios(self,persona):
        self.listaFuncionarios.append(persona)
    def agregarTabla(self, persona):
        self.listaTabla.append(persona)
    def agregarDeposito(self, persona):
        self.Coladeposito.append(persona)
    def agregarRetirar(self, persona):
        self.Colaretirar.append(persona)
    def agregarTransferir(self, persona):
        self.Colatransferir.append(persona)
    def agregarPrestamo(self, persona):
        self.colaprestamo.append(persona)
    def getListaFuncionarios(self):
        return self.listaFuncionarios

    def getListaTabla(self):
        return self.listaTabla

    def getLista(self):
        return self.listaPersonas

    def getListaDeposito(self):
        return self.Coladeposito
    def getListaRetirar(self):
        return self.Colaretirar
    def getListaTransferir(self):
        return self.Colatransferir
    def getListaPrestamo(self):
        return self.colaprestamo
    
    def agregarPersonas(self, persona):
        self.listaPersonas.append(persona)
       
    def agregarCliente(self, cliente):
        self.listaPersonas.append(cliente)    
    def mostrar(self):
        for persona in self.listaPersonas:
            info="el nombre  :"+ persona.getNombre()+"apellido  :"+ persona.getApellido()+ "rut :"+ persona.getRut()+ "saldo  :"+str(persona.getSaldo())+"operacion es  : "+persona.getOperacion()
            print (info)
    def mostrarDeposito(self):
        for persona in self.Coladeposito:
            info="el nombre  :"+ persona.getNombre()+"apellido  :"+ persona.getApellido()+ "rut :"+ persona.getRut()+ "saldo  :"+str(persona.getSaldo())+"operacion es  : "+persona.getOperacion()
            print (info)
    def mostrarListatabla(self):
        for persona in self.listaTabla:
            info="el nombre  :"+ persona.getNombre()+"apellido  :"+ persona.getApellido()+ "rut :"+ persona.getRut()+ "saldo  :"+str(persona.getSaldo())+"operacion es  : "+persona.getOperacion()
            print (info)
    
          
    

                
