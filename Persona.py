class Persona(object):
     def __init__(self,nombrepersona,apellidopersona,rutpersona):
        self.nombrepersona=["Cesar","Felipe","Diego"," Theare"]
        self.apellidopersona=["Mora","Vera","Gutierrez","Delgado"]
        self.rutpersona=["203770936","20","20","202254472"]

        def PonerNombrepersona(self,nombrepersona):
            self.nombrepersona=nombrepersona
        
        def ponerApellidopersona(self,apellidopersona):
            self.apellidopersona=apellidopersona
        
        def ponerRutpersona(self,rutpersona):
             self.rutpersona=rutpersona


 
        def tomarNombrepersona(self):
            return self.nombrepersona
            
        def tomarApellidopersona(self):
            return self.apellidopersona

        def tomarRutpersona(self):
            return self.rutpersona

        def __str__(self) :
            return self.nombrepersona+" "+self.apellidopersona+""+self.rutpersona

