from Factura import Factura

class Factura_Carrera(Factura):
    def __init__(self, clave, cliente, num_carrera, tipo_entrada, puesto):
        self.num_carrera = num_carrera
        self.tipo_entrada = tipo_entrada
        self.puesto = puesto
        super().__init__(clave, cliente)
    
    def mostrar_factura(self):
        print(f"""
        - Clave: {self.clave}
        - Cliente: {self.cliente.mostrar_cliente()}
        - Numero de carrera: {self.num_carrera}
        - Tipo de entrada: {self.tipo_entrada}
        - Puesto: {self.puesto}
        """)
    