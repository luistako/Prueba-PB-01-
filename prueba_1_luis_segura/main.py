from celular import Celular
from computadora import Computador
from tablet import Tablet
from tienda import Tienda

#estoy creando una instancia de la tienda 
tienda_principal = Tienda()

#intancia los vehiculos
mi_celular = Celular("Motorola","Android", 18000,16)
mi_tablet = Computador("motorola","Android", 40000,8)
mi_computadora = Tablet("Mac", "Aple" ,81000, 12)

print("------modificacion de Precios ------")
mi_celular.set_precio(24500) #en esta linea modifico el precio 

print("-----agregar dispositivos al catalago--------")
tienda_principal.agregar_dispositivo(mi_celular)
tienda_principal.agregar_dispositivo(mi_computadora)
tienda_principal.agregar_dispositivo(mi_tablet)

tienda_principal.mostrar_catalago()