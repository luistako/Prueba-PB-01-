from dispositivo import Dispositivo

 #creo la clase computador 
 #es una clase hija
class Computador(Dispositivo):
    def __init__(self,marca,modelo,precio,ram):
        super().__init__(marca,modelo,precio)
        self.ram = ram #agrege un nuevo atributo 

    def descripcion(self):
        return f" la marca del computador es: {self.marca}, modelo {self.modelo}, la cantidad de ram en su computadora es de {self.ram}"