class Constructors:

    puntos = 0

    def __init__(self, nombre, nacionalidad, team, lista_pilotos):
        self.nombre = nombre
        self.nacionalidad = nacionalidad 
        self.team = team
        self.lista_pilotos = lista_pilotos

    
    def mostrar_constructores(self):
        print(f"""
            - Nombre:{self.nombre}
            - Nacionalidad:{self.nacionalidad}
            - team: {self.team}
            - Lista de Pilotos:
            """)
        
        for x in self.lista_pilotos:
            x.mostrar_piloto()