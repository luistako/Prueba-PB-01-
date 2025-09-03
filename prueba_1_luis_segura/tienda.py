
#defino la clase de gestion del catalago de vehiculos 
class Tienda:
    def __init__(self):
        self.dispositivo = []

    def agregar_dispositivo(self,dispositivo):
        self.dispositivo.append(dispositivo)
        print(f"dispositivo {dispositivo.marca} {dispositivo.modelo} para agregar al catalago")

    def mostrar_catalago(self):
        total_catalago = 0
        print("------ Catalago de dispositivo --------")
        for dispositivo in self.dispositivo:
            print(f" {dispositivo.descripcion()}")
            print(f" Precio: ${dispositivo.get_precio()}")
            total_catalago += dispositivo.get_precio()
        print (f"total de dispositivos en stock: {len(self.dispositivo)}") #aca voy a mostrar el catalago que tengo 
        print (f"valor total del catalago: $ {total_catalago}") # en esta linea se muestra el valor que hay en el catalago 