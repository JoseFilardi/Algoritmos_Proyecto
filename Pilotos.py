class Piloto:

    puntos = 0
    lugar = 0

    def __init__(self, nombre, apellido, fecha_nacimiento, lugar_nacimiento, numero):
        self.nombre = nombre
        self.apellido = apellido 
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.numero = numero

    #Funcion para mostrar los atributos de un jugador
    def mostrar_piloto(self):
        print(f"""
            - Nombre:{self.nombre}
            - Apellido:{self.apellido}
            - Fecha de Nacimiento: {self.fecha_nacimiento}
            - Lugar de Nacimiento: {self.lugar_nacimiento}
            - Numero: {self.numero}
            """)
    
    def mostrar_piloto2(self):
        print(f"""
            - {self.lugar}. {self.nombre} {self.apellido}, {self.puntos}
        """)