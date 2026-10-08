class Persona:
    def __init__(self, Nombre, apellido,  Edad, documento, Año_Nacimiento, Pais, Genero):
        self.Nombre = Nombre
        self.apellido = apellido
        self.Edad = Edad
        self.documento = documento
        self.Año_Nacimiento = Año_Nacimiento
        self.Pais = Pais
        self.Genero = Genero

    def presentacion(self):
        if self.Año_Nacimiento != 2026 - self.Edad:
            raise ValueError("La edad no coincide con el año de nacimiento.") 
        else:
            return (f"Hola, mi nombre es {self.Nombre}, mi apellido es {self.apellido}, tengo {self.Edad} años, mi documento es {self.documento}, nací en {self.Año_Nacimiento} y soy de {self.Pais}. Por cierto, soy {self.Genero}.")


persona_1 = Persona(input(), input(), int(input()), int(input()), int(input()), input(), input())
persona_2 = Persona(input(), input(),  int(input()), int(input()), int(input()), input(), input())

print(persona_1.presentacion())
print(persona_2.presentacion())
