from dispositivo import Dispositivo

 #creo la clase tablet 
 #es una clase hija
class Tablet(Dispositivo):
    def __init__(self,marca,modelo,precio,tamaño_pantalla):
        super().__init__(marca,modelo,precio)
        self.tamaño_pantalla = tamaño_pantalla #agrege un nuevo atributo 

    def descripcion(self):
        return f" la marca del tablet es: {self.marca}, modelo {self.modelo}, {self.tamaño_pantalla} tamaño de pantalla"