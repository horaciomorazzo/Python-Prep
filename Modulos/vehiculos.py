class vehiculo:
    def __init__(self,color,tipo,cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0
    def Acelerar(self, vel):
        self.velocidad += vel

    def Frenar(self, vel):
        self.velocidad -= vel
    
    def Doblar(self, grados):
        self.direccion += grados

auto1 = vehiculo('rojo','moto',1000)
moto1 = vehiculo('verde','moto',150)
camion1 = vehiculo('gris','camión',10000)
auto1.Acelerar(120)
print(auto1.velocidad)
auto1.Frenar(60)
print(auto1.velocidad)
