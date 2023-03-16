class Jugador:

    def __init__(self, peso=float, altura=float, edad=int):
        self.peso = peso
        self.altura = altura
        self.edad = edad
    
    def datos_jugador(self):
        return f'\n| Peso: {self.peso} \n| Altura: {self.altura} \n| Edad: {self.edad} \n'

class Delantero(Jugador):

    def __init__(self, peso=float, altura=float, edad=int):
        super().__init__(peso, altura, edad)
        self.golesEchos= 2
    
    def datos_delantero(self):
        return f'\n| Delantero \n| Peso: {self.peso} \n| Altura: {self.altura} \n| Edad: {self.edad} \n|  Goles echos: {self.golesEchos}'

class Defensa(Jugador):

    def __init__(self, peso=float, altura=float, edad=int):
        super().__init__(peso, altura, edad)
        self.golessalvados = 5
    
    def datos_defensa(self):
        return f'\n| Defensa \n| Peso: {self.peso} \n| Altura: {self.altura} \n| Edad: {self.edad} \n| Goles defendidos: {self.golessalvados}'



Jugador1 = Delantero(74.7,1.80,25)
print(Jugador1.datos_delantero())

Jugador2 = Defensa(82.0,2.10,28)
print(Jugador2.datos_defensa())