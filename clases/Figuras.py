import math


class Punto:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


class Circulo:
    def __init__(self, radio: int, centro: Punto):
        self.radio: int = radio
        self.centro: Punto = centro

    def calcular_area(self) -> float:
        return  math.pi * self.radio ** 2

    def esta_en_el_circulo(self, puntodado: Punto):
        self.puntodado: Punto = puntodado
        if (self.puntodado.x-self.centro.x)**2 + (self.puntodado.y-self.centro.y)**2 <= self.radio**2:
            return True
        else:
            return False

        #Crear metodo en la clase circulo donde dado otro circulo, debe decir si los circulos se intersectan
