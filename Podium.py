class Podium:
    
    def __init__(self, mapa):
        self.mapa = mapa
    
    def mostrar_mapa(self):
        for mapa in self.mapa:
            if mapa == "general":
                fila = self.mapa[mapa][0]
                columna = self.mapa[mapa][1]
                for f in range(fila):
                    for c in range(columna):
                        print([f,c], end = " ")
                    print("")
        
        print("")
        
        for mapa in self.mapa:
            if mapa == "vip":
                fila = self.mapa[mapa][0]
                columna = self.mapa[mapa][1]
                for f in range(fila):
                    for c in range(columna):
                        print("V",[f,c], end = " ")
                    print("")
    
    def mostrar_mapa_general(self):
        for mapa in self.mapa:
            if mapa == "general":
                fila = self.mapa[mapa][0]
                columna = self.mapa[mapa][1]
                for f in range(fila):
                    for c in range(columna):
                        print([f,c], end = " ")
                    print("")
            
    def mostrar_mapa_vip(self):
        for mapa in self.mapa:
            if mapa == "vip":
                fila = self.mapa[mapa][0]
                columna = self.mapa[mapa][1]
                for f in range(fila):
                    for c in range(columna):
                        print("V",[f,c], end = " ")
                    print("")