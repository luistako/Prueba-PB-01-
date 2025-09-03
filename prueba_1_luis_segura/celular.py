from dispositivo import Dispositivo

 #creo la clase celular 
 #es una clase hija
class Celular(Dispositivo):
    def __init__(self,marca,modelo,precio,megapixeles):
        super().__init__(marca,modelo,precio)
        self.megapixeles = megapixeles #agrege un nuevo atributo 

    def descripcion(self):
        return f" la marca de su celular es: {self.marca}, modelo {self.modelo}, la cantidad de megapixeles de su camara es {self.megapixeles}"