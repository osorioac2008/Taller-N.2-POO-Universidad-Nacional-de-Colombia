from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    def __init__(self, nombre, satelites, masa, volumen, diametro, distancia_sol, tipo : TipoPlaneta, observable : bool, periodo_orb, periodo_rot):
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.observable = observable
        self.periodo_orb = periodo_orb
        self.periodo_rot = periodo_rot

        if  not isinstance(tipo, TipoPlaneta):
            raise ValueError("Ese no es un tipo de planeta")
        self.tipo = tipo
     
    def densidad(self):
        return self.masa / self.volumen
    
    def exterior(self):
            if self.distancia_sol / 149597870 > 3.4:
                return "Se considera exterior"
            
            return "No se considera exterior"
       
    def presentacion(self):     
        return (f"El planeta {self.nombre} tiene {self.satelites} satélites, una masa de {self.masa} kg, un volumen de {self.volumen} km³, un diámetro de {self.diametro} km, se encuentra a {self.distancia_sol} millones de km del sol, es un planeta {self.tipo} y es observable: {self.observable}.\n Su densidad es de {self.densidad()} kg/km³ y cabe recalcar sus dos tipos de rotaciones, su rotacion orbital ronda {self.periodo_orb} años y su rotacion sobre su propio eje es de {self.periodo_rot} días.")
    

planeta_1 = Planeta("Tierra", 1, 5.972 * 10**24, 1.08321 * 10**12, 12742, 149597870, TipoPlaneta.TERRESTRE, True, 1, 365.25)
planeta_2 = Planeta("Jupiter", 79, 1.898 * 10**27, 1.43128 * 10**15, 139820, 778547200, TipoPlaneta.GASEOSO, True, 11.86, 0.41)
print(planeta_1.presentacion(), planeta_1.densidad(), planeta_1.exterior())
print(planeta_2.presentacion(), planeta_2.densidad(), planeta_2.exterior())
