import math

class Figuras:
    pass

    class circulo:
        def __init__(self, radio):
            self.radio = radio
            self.pi = math.pi
        
        def area_circulo(self):
            print(f"Area: {self.pi * (self.radio ** 2)}")
    
    class rectangulo:
        def __init__(self, base_r, altura_r):
            self.base = base_r
            self.altura = altura_r
        
        def area_rectangulo(self):
            print(f"Area: {self.base * self.altura}")
            
    class cuadrado:
        def __init__(self, lado):
            self.lado = lado
        
        def area_cuadrado(self):
            print(f"Area: {self.lado**2}")
    
    class triangulo:
        def __init__(self, base_t, altura_t, hipotenusa = 0):
            self.base = base_t
            self.altura = altura_t
            self._hipotenusa = hipotenusa   
        
        @property
        def hipotenusa(self):
            return self._hipotenusa
        @hipotenusa.setter
        def hipotenusa(self, value):
            self._hipotenusa = value
            
       
        def area_triangulo(self):
            print(f"Area: {(self.base * self.altura) / 2}")
        
        def pitagoras(self):
            Hipotenusa = math.sqrt((self.base**2) + (self.altura**2))
            if Hipotenusa <= self.altura + self.base and self.base <= self.altura + Hipotenusa and self.altura <= self.base + Hipotenusa:
                print("El triangulo es valido")
                print(f"Hipotenusa: {Hipotenusa}")
                self.hipotenusa = Hipotenusa

            else:
                print("El triangulo no es valido")
                return None
           
        def tipo_trangulo(self):
            if self._hipotenusa == self.base and self._hipotenusa == self.altura:
                print("El triangulo es equilatero")
            elif self._hipotenusa == self.base or self._hipotenusa == self.altura or self.base == self.altura:
                print("El triangulo es isosceles")
            else:
                print("El triangulo es escaleno")

circulo = Figuras.circulo(5)
rectangulo = Figuras.rectangulo(2, 4)
cuadrado = Figuras.cuadrado(3)
triangulo = Figuras.triangulo(3, 4)

circulo.area_circulo()
rectangulo.area_rectangulo()
cuadrado.area_cuadrado()
triangulo.area_triangulo()
triangulo.pitagoras()
triangulo.tipo_trangulo()
