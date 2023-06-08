class Vehiculo:
    def __init__(self,color,tipo,cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 20
        self.direccion = 0
    
    def acelerar(self, cambio):
        self.velocidad += cambio
    
    def girar(self, grados):
        self.direccion += grados
        



