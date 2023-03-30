class Carreras:
    estado = True

    def __init__(self, nombre, numero, fecha, circuito, podium):
        self.nombre = nombre
        self.numero = numero 
        self.fecha = fecha
        self.circuito = circuito
        self.podium = podium
    
    def mostrar_carreras(self):
        print("===========================")
        print(f"""
            - Nombre:{self.nombre}
            - Numero:{self.numero}
            - Fecha: {self.fecha}
            ------------------------
            - Cicuito:
        """)
        self.circuito.mostrar_circuito()
        print("-----------------------")
        print("- Podium:")
        self.podium.mostrar_mapa()
        print("===========================")


