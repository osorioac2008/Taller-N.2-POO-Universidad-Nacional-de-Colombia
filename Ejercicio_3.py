from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = "gasolina"
    BIOETANOL = "bioetanol"
    DIESEL = "diesel"
    BIODIESEL = "biodiesel"
    GAS = "gas"

class TipoAuto(Enum):
    CIUDAD = "ciudad"
    SUBCOMPACTO = "subcompacto"
    COMPACTO = "compacto"
    FAMILIAR = "familiar"
    EJECUTIVO = "ejecutivo"
    SUV = "suv"

class Color(Enum):
    BLANCO = "blanco"
    NEGRO = "negro"
    ROJO = "rojo"
    AZUL = "azul"
    NARANJA = "naranja"
    amarillo = "amarillo"
    verde = "verde"
    violeta = "violeta"

class Automovil:
        
    def __init__(self, marca, modelo, motor, combustible : TipoCombustible, tipo : TipoAuto, puertas, asientos, velocidad_max, color : Color, velocidad_actual=0):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.puertas = puertas
        self.asientos = asientos
        self.velocidad_max = velocidad_max
        self._velocidad_actual = velocidad_actual
        
        if not isinstance(combustible, TipoCombustible):
            raise ValueError("El tipo de combustible no es válido")
        self.combustible = combustible
        
        if not isinstance(tipo, TipoAuto):
            raise ValueError("El tipo de auto no es válido")
        self.tipo = tipo
        
        if not isinstance(color, Color):
            raise ValueError("El color no es válido")
        self.color = color

    @property
    def velocidad_actual(self):
        return self._velocidad_actual

    @velocidad_actual.setter
    def velocidad_actual(self, nueva_velocidad):
        if nueva_velocidad > self.velocidad_max:
            print("La velocidad no puede superar la velocidad máxima del vehículo")
        elif nueva_velocidad < 0:
            print("La velocidad no puede ser negativa")
        else:
            self._velocidad_actual = nueva_velocidad

    def acelerar(self, incremento):
        self.velocidad_actual = self._velocidad_actual + incremento

    def desacelerar(self, decremento):
        self.velocidad_actual = self._velocidad_actual - decremento

    def frenar(self):
        self._velocidad_actual = 0
        
    def llegada(self, distancia):
        if self.velocidad_actual == 0:
            print("El carro esta detenido")
        else:
            dist = distancia/self.velocidad_actual
            print(f"El tiempo estimado de llegada es: {dist} horas")

    def especificaciones(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nMotor: {self.motor}\nCombustible: {self.combustible}\nTipo: {self.tipo}\nPuertas: {self.puertas}\nAsientos: {self.asientos}\nVelocidad máxima: {self.velocidad_max} km/h\nColor: {self.color}\nVelocidad actual: {self.velocidad_actual} km/h")


auto1 = Automovil("Ford", 2018, 3, TipoCombustible.DIESEL, TipoAuto.SUV, 5, 6, 300, Color.NEGRO, 250) 

auto1.especificaciones()

auto1.velocidad_actual = 100
print(f"Velocidad actual = {auto1.velocidad_actual} km/h")

auto1.acelerar(20)
print(f"Velocidad actual = {auto1.velocidad_actual} km/h")

auto1.llegada(340)

auto1.desacelerar(50)
print(f"Velocidad actual = {auto1.velocidad_actual} km/h")

auto1.frenar()
print(f"Velocidad actual = {auto1.velocidad_actual} km/h")
