
#clase padre
class Dispositivo:
    def __init__(self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo
        self.__precio = precio #incerto los atributos

    def get_precio(self): 
        return self.__precio
    
    def set_precio( self, nuevo__precio):
        if nuevo__precio > 0: #defino el precio minimo de los dispositivos
            self.__precio = nuevo__precio
            print(f"El precio de {self.marca} {self.modelo} ha sido actualizado a ${self.__precio}.")
        else:
            print("Error: El precio debe ser un valor sobre 0")
#en esta linea se aplica el polimorfismo 
    def descripcion(self):
        return f"la marca del despositivo es {self.marca} y el modelo {self.modelo}"
