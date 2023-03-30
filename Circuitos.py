class Circuitos:
    def __init__(self, nombre, pais, localidad, lat_long):
        self.nombre = nombre
        self.pais = pais 
        self.localidad = localidad
        self.lat_long = lat_long

    def mostrar_circuito(self):
        print(f"""
            - Nombre:{self.nombre}
            - Pais:{self.pais}
            - Localidad: {self.localidad}
            - Longitud y latitud: {self.lat_long}
            """)
        
        
