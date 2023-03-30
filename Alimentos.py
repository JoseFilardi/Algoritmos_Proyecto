class Alimentos:
    def __init__(self, nombre,  tipo, tipo_especific, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.tipo_especific = tipo_especific
        self.precio = precio

    
    def mostrar_producto(self):
        return f"""
        - Nombre: {self.nombre}
        - Tipo: {self.tipo}, {self.tipo_especific}
        - Precio: {self.precio}
        """
    def mostrar_precio(self):
        return f"{self.precio}"