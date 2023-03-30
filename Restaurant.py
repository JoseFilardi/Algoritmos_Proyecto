class Restaurant:
    def __init__(self, nombre, list_product, clave):
        self.nombre = nombre
        self.list_product = list_product
        self.clave = clave
    
    def mostrar_restaurant(self):
        print(f"""
            - Nombre:{self.nombre}
            - Lista de Productos:
            """)
        
        for prod in self.list_product:
            prod.mostrar_producto()