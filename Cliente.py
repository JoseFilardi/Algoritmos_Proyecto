class Cliente:
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
    
    def mostrar_cliente(self):
        print(f"""
        - Nombre: {self.nombre}
        - Edad: {self.edad}
        - Cédula: {self.cedula}
        """)
    
    
    
