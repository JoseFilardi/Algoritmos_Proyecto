from Pilotos import Piloto
from Constructores import Constructors
from Circuitos import Circuitos
from Carreras import Carreras
from Podium import Podium
from Alimentos import Alimentos
from Restaurant import Restaurant

class Busquedas:
    def __init__(self, constructores, pilotos, carreras, circuito, restaurant):
        self.constructores = constructores
        self.pilotos = pilotos 
        self.carreras = carreras
        self.circuito = circuito
        self.restaurant = restaurant
    
    def buscar_conductores(self):
        pais =  input("Ingrese el país al que pertenecen los constructores: ")
        for constructor in self.constructores:
            if constructor.nacionalidad == pais:
                constructor.mostrar_constructores()
    
    def buscar_pilotos(self):
        nombre_constructor = input("Ingrese el nombre del constructor: ")
        for constructor in self.constructores:
            if constructor.nombre == nombre_constructor:
                for piloto in constructor.lista_pilotos:
                    piloto.mostrar_piloto()
    
    def buscar_carreras(self):
        pais_circuito = input("Ingrese el pais del circuito: ")

        for carrera in self.carreras:
            if carrera.circuito.pais == pais_circuito:
                carrera.mostrar_carreras()
    
    def buscar_carreras_mes(self):
        mes = input("Ingrese el mes: ")
        while (not mes.isnumeric()) or (not int(mes) in range(1,13)):
            print("Error!!! mes Inválido.")
            mes = input("Ingrese el mes: ")
        
        for carrera in self.carreras:
            date = carrera.fecha.split("-")
            date_final = date[len(date)-1]
            if date_final == mes:
                carrera.mostrar_carreras()

    def buscar_productos(self):
        while True:
            print("\n=====================")
            print("BUSCADOR DE PRODUCTOS")
            print("======================")
            print("1. Buscar por nombre\n2. Buscar tipo\n3. Buscar por rango de precio\n4.Salir")
            
            option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not option.isnumeric()) or (not int(option) in range(1,5)):
                    print("Error!!! Dato Inválido.")
                    option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            
            #Buscar productos según su nombre
            if option == "1":
                nombre_producto = input("Ingrese el nombre del producto: ")
                for rest in self.restaurant:
                    for product in rest.list_product:
                        if product.nombre == nombre_producto:
                            product.mostrar_producto()
                            break
                
            
            
            #Buscar producto según su tipo
            elif option == "2":
                
                print("\n------------------")
                print("TIPOS DE PRODUCTOS")
                print("-------------------")
                print("1. Comida\n2. Bebida")
                
                tipo_p = input("Ingrese el número correspondiente al tipo de producto que desea buscar: ")
                while (not tipo_p.isnumeric()) or (not int(tipo_p) in range(0,3)):
                    print("Error!!! Dato Inválido.")
                    tipo_p = input("Ingrese el número correspondiente al tipo de producto que desea buscar: ")
            
                if tipo_p == "1":
                    tipo_p = "food"
                    for rest in self.restaurant:
                        for product in rest.list_product:
                            if product.tipo == tipo_p:
                                product.mostrar_producto()
                
                
                else:
                    tipo_p = "drink"
                    for rest in self.restaurant:
                        for product in rest.list_product:
                            if product.tipo == tipo_p:
                                product.mostrar_producto()                    
        
            
            #Buscar productos en un rango de precio
            elif option == "3":
                print("Escoja el rango de precio del producto")
                
                inicio = input("De: ")
                while (not inicio.isnumeric()) or (not float(inicio) >= 0):
                    print("Error!!! El precio mínimo debe ser  o igual a 0")
                
                final = input("Hasta: ")
                while (not final.isnumeric()) or (not float(final) >= 0):
                    print("Error!!! El precio mínimo debe ser mayor o igual a 0")
                
                for rest in self.restaurant:
                    for product in rest.list_product:
                        if float(product.precio) >= float(inicio) and float(product.precio) <= float(final):
                            print(product.mostrar_producto())
